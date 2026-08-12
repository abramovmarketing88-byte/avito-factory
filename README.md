# Avito Factory

Cursor Agent Skill: полный цикл массовых объявлений Авито — от брифа до CSV/XLSX автозагрузки.

Стартовая точка: [`SKILL.md`](SKILL.md)

## Скиллы Авито в экосистеме

| Скилл | Репозиторий | Задача |
|-------|-------------|--------|
| **avito-factory** | [avito-factory](https://github.com/abramovmarketing88-byte/avito-factory) | бриф → research → тексты → спинтекст → CSV/XLSX |
| **avito-photos** | [avito-photos](https://github.com/abramovmarketing88-byte/avito-photos) | ImageUrls через Яндекс.Диск, CTR-оверлеи 4:3 |
| **avito-api** | [avito-api-skill](https://github.com/abramovmarketing88-byte/avito-api-skill) | OAuth, выгрузка/загрузка через API автозагрузки |
| **avito-search-audit** | [avito-search-audit](https://github.com/abramovmarketing88-byte/avito-search-audit) | парсинг выдачи Авито, анализ конкурентов, Canvas |

### Связка пайплайна

```
avito-search-audit  →  research / конкуренты
avito-factory       →  тексты + CSV/XLSX
avito-photos        →  фото + ImageUrls в фид
avito-api           →  выгрузка/загрузка через API
```

Локально скиллы лежат в `~/.cursor/skills/{name}/`.
