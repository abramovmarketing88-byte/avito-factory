# Этап 7.5: Clean autoload XLSX

Перед загрузкой в автозагрузку Авито — **очистить** xlsx от мусора исходного аккаунта.

## Когда нужно

- Фид собран из **полной выгрузки** кабинета (много категорий)
- После **scale** до N строк: не выбранные строки обнулены NA, но **физически остались** (1093 строк вместо 304)
- В файле есть **аренда**, товары, другие услуги — не из текущего брифа

## Что делать

### 1. Удалить лишние листы

Оставить только:

- `Инструкция`
- Data-листы **целевых** категорий (напр. «Деловые услуги-Бухгалтерия, фин», «IT…Программирование»)
- Справочники `Спр-*` **только** для оставшихся data-листов

Удалить примеры: `Сдам-Посуточно`, `Спр-Сдам-…`, мебель, авто — если не в брифе.

### 2. Уплотнить data-листы (compact)

**Не** обрезать по `last_data_row` — после scale пустые строки могут быть **между** объявлениями.

Правило: **header rows 1–4** + все строки, где **Title не пустой**.

```python
def compact_data_sheet(df):
    col = header_map(df)
    header = df.iloc[:4]
    body = [df.iloc[i] for i in range(4, len(df))
            if pd.notna(df.iat[i, col["Title"]]) and str(df.iat[i, col["Title"]]).strip()]
    return pd.concat([header, pd.DataFrame(body)], ignore_index=True)
```

### 3. Бэкап и отчёт

- Бэкап: `output/backups/{feed-stem}-before-clean-{date}.xlsx`
- Отчёт: `output/reports/feed-clean-report.json` — removed_sheets, before/after rows, totals per sheet

## Конфиг под проект

В `scripts/clean_autoload_feed.py` задай:

```python
KEEP_SHEETS_PREFIX = (
    "Инструкция",
    "Деловые услуги-Бухгалтерия, фин",
    "Спр-Деловые услуги-Бухгалтерия,",
    "IT, дизайн, тек-Программировани",
    "Спр-IT, дизайн, тек-Программиро",
)
DROP_SHEETS = ("Сдам-Посуточно", "Спр-Сдам-Посуточно")
DATA_SHEETS = (...)  # листы для compact
```

Любой лист **не** из `KEEP_SHEETS_PREFIX` → удалить.

## Pre-launch check

После clean + photos:

- [ ] `ads` count на листе = ожидаемому N
- [ ] `no_imageurls` = 0 (или только у locked active)
- [ ] sheets list без чужих категорий
- [ ] Яндекс.Диск синхронизирован — см. `avito-photos` prelaunch-checklist

## Связь с scale

При написании **нового** scale-скрипта предпочтительно:

- либо **физически вырезать** только selected rows в новый frame,
- либо **обязательно** вызывать clean после scale.

Не отдавать пользователю xlsx с 1000+ строк и 700+ пустых дыр.
