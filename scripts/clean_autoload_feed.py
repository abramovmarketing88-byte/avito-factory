#!/usr/bin/env python3
"""Clean autoload xlsx: drop foreign sheets, compact data rows. Template — edit config."""

from __future__ import annotations

import json
import shutil
from datetime import date
from pathlib import Path

import pandas as pd

# --- Edit for project ---
KEEP_SHEETS_PREFIX = (
    "Инструкция",
)
DROP_SHEETS: tuple[str, ...] = ()
DATA_SHEETS: tuple[str, ...] = ()  # sheets to compact (non-empty Title only)

ROOT = Path(__file__).resolve().parent.parent
FEED_DIR = ROOT / "output" / "feeds"
BACKUP_DIR = ROOT / "output" / "backups"
REPORT_DIR = ROOT / "output" / "reports"
DATA_START = 4


def compact_data_sheet(df: pd.DataFrame) -> pd.DataFrame:
    col = {str(df.iloc[1, i]).strip(): i for i in range(df.shape[1]) if pd.notna(df.iloc[1, i])}
    if "Title" not in col:
        return df
    header = df.iloc[:DATA_START].copy()
    data_rows = []
    for idx in range(DATA_START, len(df)):
        val = df.iat[idx, col["Title"]]
        if pd.notna(val) and str(val).strip():
            data_rows.append(df.iloc[idx].copy())
    if not data_rows:
        return header
    body = pd.DataFrame(data_rows).reset_index(drop=True)
    ncols = max(header.shape[1], body.shape[1])
    for frame in (header, body):
        for c in range(frame.shape[1], ncols):
            frame[c] = pd.NA
    header = header.reindex(columns=range(ncols))
    body = body.reindex(columns=range(ncols))
    return pd.concat([header, body], ignore_index=True)


def main() -> None:
    feeds = sorted(FEED_DIR.glob("*.xlsx"))
    if not feeds:
        raise SystemExit("No feed xlsx in output/feeds/")
    feed_path = feeds[-1]

    today = date.today().isoformat()
    backup_path = BACKUP_DIR / f"{feed_path.stem}-before-clean-{today}.xlsx"
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(feed_path, backup_path)

    xl = pd.ExcelFile(feed_path)
    removed: list[str] = []
    kept: dict[str, dict] = {}

    for name in xl.sheet_names:
        if name in DROP_SHEETS:
            removed.append(name)
            continue
        if not any(name.startswith(p) for p in KEEP_SHEETS_PREFIX):
            removed.append(name)
            continue
        df = pd.read_excel(feed_path, sheet_name=name, header=None)
        before = len(df)
        if name in DATA_SHEETS:
            df = compact_data_sheet(df)
        kept[name] = {"before_rows": before, "after_rows": len(df), "frame": df}

    with pd.ExcelWriter(feed_path, engine="openpyxl") as writer:
        for name, info in kept.items():
            info["frame"].to_excel(writer, sheet_name=name, index=False, header=False)

    summary = {
        "feed": str(feed_path),
        "backup": str(backup_path),
        "removed_sheets": removed,
        "sheets": {n: {"before_rows": i["before_rows"], "after_rows": i["after_rows"]} for n, i in kept.items()},
    }
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "feed-clean-report.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
