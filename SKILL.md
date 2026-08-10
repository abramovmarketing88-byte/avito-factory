---
name: avito-factory
description: >-
  Полный пайплайн массовых объявлений для Авито: бриф → (опц.) конкурентный
  парсинг выдачи → ЦА → title/офферы → объявления → аудит → спинтекст → CSV и/или
  XLSX автозагрузки. Отдельные категории (кухни / шкафы-купе), уникализация
  моделями, когортные цены, гео МСК+МО, выгрузка через Avito API. Пресет
  Татарстан 200. Use when user says avito factory, /avito-factory, автозагрузка
  Авито, массовая генерация объявлений, спинтекст, CSV/XLSX для Авито, парсинг
  конкурентов Авито, Мебель Алирис, 1000/2000 объявлений.
disable-model-invocation: true
---

# Avito Factory

Оркестратор полного цикла: от брифа до файла для массовой загрузки на Авито.

**Финальные артефакты (по задаче):**
- CSV: `output/feeds/avito-ads-{slug}-{date}.csv` — Title, Description, Address
- XLSX автозагрузки: `output/feeds/основной-{slug}-{n}.xlsx` — листы категорий Авито
- Research: `output/research/{category}-{geo}/`
- Canvas (по желанию): конкурентный разбор рядом с чатом

## Быстрый старт

1. Прочитай бриф + карту проекта (`README.md` в корне, если есть).
2. Создай `output/session-{slug}.md` из [templates/session-state.md](templates/session-state.md).
3. Если категорий ≥2 (кухни + шкафы) — веди **отдельные треки** research/copy или явные секции в session.
4. Пройди этапы 0→7 (и 0.5 research при масштабе 200+). На чекпоинтах жди подтверждения.
5. Отдай файл(ы) + краткий отчёт (кол-во, цены, адреса, антидетект).

**Slug** — транслит услуги, lowercase, через дефис (`mebel-aliris`, `kuhni-moskva`).

---

## Рекомендуемая структура проекта

```
briefs/          ← бриф, контекст конкурента
sources/         ← отзывы, сырьё
templates/       ← чистый шаблон Авито (osnovnoy.xlsx)
output/
  session-*.md
  copy/          ← titles, models, spintax
  feeds/         ← csv/xlsx для автозагрузки
  research/      ← парсинг конкурентов по категориям
  data/          ← выгрузки API (items, reports)
  backups/
  images/
scripts/         ← генераторы
```

Не смешивай сайд-проекты с фидами основного бренда (`projects/` отдельно).

---

## Быстрый путь: Татарстан 200

Создай 200 объявлений РТ: **50** Казань / **20** Наб. Челны / **130** остальные города РТ.

1. Экспорт переписки → `data/avito-chat-export.txt`
2. [10-chat-export-brief.md](references/10-chat-export-brief.md)
3. `python scripts/generate_tatarstan_200.py --export … --output output/avito-ads-tatarstan-200.csv`
4. Проверь **ровно 200** и сплит 50/20/130

Гео: [11-tatarstan-geo-preset.md](references/11-tatarstan-geo-preset.md).

---

## Этапы пайплайна

```
0 Intake → [0.5 Research] → 1 ЦА → 2 Креативы → 3 Объявления
  → 4 Аудит → 5 Спинтекст → 6 Масштаб → 7 CSV/XLSX → [8 Фото]
```

| Этап | Что делать | Reference |
|------|------------|-----------|
| 0 | Бриф, API-ключи, шаблон xlsx | [01-brief-intake.md](references/01-brief-intake.md) |
| 0.5 | Парсинг выдачи Авито **по каждой категории отдельно** | [12-competitor-research.md](references/12-competitor-research.md) |
| 1 | ЦА | [02-audience-analysis.md](references/02-audience-analysis.md) + [03-avito-strategy.md](references/03-avito-strategy.md) |
| 2 | Title / офферы / углы (с учётом research) | [04-creatives-offers.md](references/04-creatives-offers.md) |
| 3 | 3–4 базовых объявления | [05-ad-writing.md](references/05-ad-writing.md) |
| 4 | Аудит 12 уровней | [06-audit-fix.md](references/06-audit-fix.md) |
| 5 | Спинтекст | [07-spintax.md](references/07-spintax.md) |
| 6 | Масштаб + уникализация | [14-uniquification.md](references/14-uniquification.md) |
| 7 | CSV и/или XLSX автозагрузки | [08-csv-export.md](references/08-csv-export.md) + [13-autoload-xlsx.md](references/13-autoload-xlsx.md) |
| 8 | Фото | [09-image-reverse.md](references/09-image-reverse.md) |
| — | Выгрузка объявлений через API | [15-avito-api-export.md](references/15-avito-api-export.md) |
| — | Экспорт переписки | [10-chat-export-brief.md](references/10-chat-export-brief.md) |
| — | Татарстан 200 | [11-tatarstan-geo-preset.md](references/11-tatarstan-geo-preset.md) |

---

## Этап 0: Intake

Прочитай [01-brief-intake.md](references/01-brief-intake.md).

Дополнительно спроси / зафиксируй (пакетно):
- Категории Авито **отдельно** (кухни / шкафы-купе / …) и целевое N на каждую
- Формат выдачи: CSV / **XLSX автозагрузки** / оба
- Длина Description (часто **300–400** символов plain)
- Антидетект vs соседний аккаунт (запрещённые фразы/эмодзи-шапки)
- Телефон, бренд в карточке, оставлять ли старые AvitoId
- Нужен ли парсинг конкурентов (этап 0.5)
- `client_id` / `client_secret` Авито API — только для выгрузки/отчётов, **не коммитить в git**
- Цены: коридор рынка ₽/п.м. **и/или** когортный разброс (100…100000)
- Гео: список адресов или правило (напр. Москва + ~20 км МКАД)

Не начинай этап 1 без: услуга, регион, количество (или сплит по категориям).

---

## Этап 0.5: Конкурентный research (рекомендуется при N≥200)

Прочитай [12-competitor-research.md](references/12-competitor-research.md).

**Правило:** кухни и шкафы-купе (и любая другая категория) — **отдельные** папки research и отдельные выводы по title.

Выход:
- `output/research/{category}-{geo}/` — methodology, competitor-analysis, popular keywords, titles, stats.json, README
- Опционально canvas с графиками частотностей
- В session: дыры спроса, медиана ₽/п.м., топ-формулы title, крючки текста

Без research на большом масштабе — высок риск копировать устаревшие шаблоны и промахнуться по ключам выдачи.

---

## Этап 1: Анализ ЦА

Как раньше + [02](references/02-audience-analysis.md) / [03](references/03-avito-strategy.md).

При нескольких категориях — сегменты/язык можно общие, но **боли и ключи title** уточняй per-category из research.

**Чекпоинт 1:** ЦА → жди «ок».

---

## Этап 2: Заголовки, спецофферы, креативы

[04-creatives-offers.md](references/04-creatives-offers.md) + выводы research.

### Формула title (из парсинга «на заказ»-ниш)

```
[ПРОДУКТ] + [на заказ | под заказ] + [ровно 1 усилитель]
```

Длина: **4–7 слов**, ≤50 символов. Не пихать бренд-селлера вместо продукта.

Усилители: размер / от производителя / форма / срок / под ключ / сценарий (студия, 2 м…) / **имя модели**.

**Дыры спроса:** ключи из блока «Популярные запросы» Авито, которых почти нет в топе «на заказ» (пример кухонь: маленький, в студию, 2–4 м, модульный) — закрывать в матрице title.

**Чекпоинт 2:** заголовки + углы → жди выбор.

---

## Этап 3–5: Объявления → аудит → спинтекст

Без изменений порядка: [05](references/05-ad-writing.md) → [06](references/06-audit-fix.md) → [07](references/07-spintax.md).

Для короткого формата 300–400:
- Первая фраза = CTA/доверие из research («Пришлите размеры — расчёт сегодня», «без роста цены на замере»)
- Один оффер-подарок (столешница / доводчики / доставка…) если это в брифе/рынке
- Рассрочка — упоминать, если релевантно (в выдаче кухонь Москва часто >50% карточек с бейджем)
- Факты бренда не выдумывать

---

## Этап 6: Масштабирование и уникализация

Прочитай [14-uniquification.md](references/14-uniquification.md).

Итого ≥ N. Для мультиаккаунта / антидетекта:
- **Модельные серии** (Кухня «Елена», шкаф-купе «Норд»…) — банк 80–120+ имён
- Разные характеристики (форма, створки, материал)
- **Разные адреса** (десятки–сотни по гео-правилу)
- **Цены:** ~50% в рыночном коридоре ₽/п.м. (из research) + хвосты для когорт Авито (низ/верх, вплоть до 100…100000 если просил пользователь)
- Уникальные Title (проверка коллизий) и Description (hash)

Категории в **разных листах** xlsx / отдельных генерациях.

---

## Этап 7: CSV и/или XLSX автозагрузки

- CSV: [08-csv-export.md](references/08-csv-export.md)
- XLSX: [13-autoload-xlsx.md](references/13-autoload-xlsx.md) — данные с **5-й строки**, не трогать строки 1–4 шаблона; `За что цена` = за погонный метр когда так в рынке; статус Активно; телефон/компания из брифа

Перед выдачей сверь фид с research/canvas (title-формула, дыры, CTA, коридор цен).

---

## Этап 8: Фото (опционально)

[09-image-reverse.md](references/09-image-reverse.md).

Из research: hero + ценник полной суммы проекта на фото; 5+ кадров; живой кадр / детали / цвета.

---

## Выгрузка текущего аккаунта (API)

Если пользователь дал `client_id` / `client_secret`:

Прочитай [15-avito-api-export.md](references/15-avito-api-export.md).

- Токен: `POST https://api.avito.ru/token`
- Фид последней выгрузки: `…/autoload/v2/reports/last_completed_report` → `feed_url` (скачать с Bearer)
- Все объявления: `GET /core/v1/items?status=active` и/или `active,old,blocked,rejected,removed`
- Сохранять в `output/data/` и `output/feeds/`; секреты не писать в репозиторий

---

## Session State

- Шаблон: [templates/session-state.md](templates/session-state.md)
- Путь: `output/session-{slug}.md`
- Обновляй после каждого этапа; для multi-category — секции Research/Title per category

---

## Субагенты

| Задача | Subagent | Тип |
|--------|----------|-----|
| Аудит объявлений | reviewer | `generalPurpose` |
| Спинтекст батчами | spintax-batch-* | `generalPurpose` |
| Реверс фото | image-analyst | `generalPurpose` |
| Парсинг N страниц выдачи | research-scrape | `generalPurpose` / browser |

Не делегируй: этапы 0–2 (диалог), финальную сборку CSV/XLSX.

---

## Чеклист перед выдачей

```
Task Progress:
- [ ] Session state заполнен
- [ ] ЦА утверждена
- [ ] Research по каждой категории (если N≥200) сохранён
- [ ] Title: продукт + на заказ + 1 усилитель; дыры спроса закрыты
- [ ] 3–4 базы прошли аудит
- [ ] Спинтекст / генератор масштаба готов
- [ ] CSV и/или XLSX: нужное N, отдельные листы категорий
- [ ] Цены: коридор рынка + когортные хвосты (если просили)
- [ ] Адреса разнообразны по гео-правилу
- [ ] Модельные имена / антидетект
- [ ] Description в заданном диапазоне длины
- [ ] Факты не искажены; секреты API не в git
```

---

## Пример: мебель, две категории, 2000 строк

> /avito-factory кухни и шкафы-купе отдельно, ~1000 каждого, модели в title, цены 100–100000, МСК+20км, докрути по парсингу

1. Session + бриф  
2. Research kitchens-moscow + wardrobes-moscow (или переиспользовать)  
3. Чекпоинты ЦА/углов  
4. Генерация xlsx: 1000+1000, модели, коридор+когорты, CTA из research  
5. Отчёт + пути к `output/feeds/`

---

## Дополнительные ресурсы

- CSV: [templates/csv-header.csv](templates/csv-header.csv), [templates/avito-bulk-upload-example.csv](templates/avito-bulk-upload-example.csv)
- Session: [templates/session-state.md](templates/session-state.md)
