# Выгрузка объявлений и фида через Avito API

Нужны `client_id` и `client_secret` из кабинета Pro → API.  
**Не коммитить секреты** в git; хранить в env / локальном скрипте вне репо.

## Токен

```
POST https://api.avito.ru/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id=…
&client_secret=…
```

Заголовок далее: `Authorization: Bearer {access_token}`

## Профиль автозагрузки

```
GET /autoload/v2/profile
```

В ответе `feeds_data[].feed_url` — URL фида, который Авито забирает по расписанию  
(может быть внешний хостинг; иногда недоступен из среды агента).

## Файл последней выгрузки (надёжнее)

```
GET /autoload/v2/reports/last_completed_report
# или /autoload/v3/… / v4 uploads last_successful
```

Поле `feed_url` / `feeds_urls[].url` вида:

`https://api.avito.ru/autoload/v2/feed/content/{…}`

Скачать **с тем же Bearer** → сохранить как  
`output/feeds/avito-autoload-feed-from-report.xlsx`

## Список объявлений аккаунта

```
GET /core/v1/items?per_page=100&page={n}&status=active
GET /core/v1/items?per_page=100&page={n}&status=active,old,blocked,rejected,removed
```

Пагинация до пустой страницы. Сохранить:

- `output/data/avito-items-active.json` / `.xlsx` / `.csv`
- `output/data/avito-items-all-statuses.json` / `.xlsx`

Поля карточки ограничены (id, title, price, address, category, status, url).  
Полный автозагрузочный Excel = feed content выше, не `/items`.

## Фильтр фида только active

Сопоставить AvitoId в фиде с id из `status=active` →  
`output/feeds/avito-autoload-ACTIVE-only.xlsx`

## Аккаунт / self

```
GET /core/v1/accounts/self
```

## Замечания

- Лимиты rate-limit: паузы между страницами
- Deprecated: часть `/autoload/v2/reports*` → смотреть successor в `_deprecation`
- Внешний feed_url (catbox и т.п.) может таймаутиться — предпочитай Avito-hosted feed content
