# Avito Автозагрузка — индекс базы знаний

Срез 19.10.2026. Источник: [SOURCE.md](SOURCE.md).

## Как пользоваться (агент)

1. Открой этот индекс.
2. Найди **направление / category ID** клиента.
3. Если статус **ready** — читай файл шаблона в `templates/` (обязательные поля, enums, PriceList).
4. Если **pending** — читай `_pending/{id}.md` и страницу Авито по ссылке; не выдумывай значения списков.
5. Общие правила загрузки/фото/Id → [01-instruction.md](01-instruction.md), [02-faq.md](02-faq.md), [04-common-params.md](04-common-params.md) + `../18-autoload-rules-ru.md`.
6. Каталог всех категорий Авито → `../../data/categories-3029.csv` (поиск по ID или названию).

Фото: скилл **`avito-photos`**.

## Корневые документы

| Файл | Содержание |
|------|------------|
| [01-instruction.md](01-instruction.md) | Как работает автозагрузка: файл, фото, видео, продвижение, загрузка, отчёты, Яндекс Диск |
| [02-faq.md](02-faq.md) | FAQ: связка AvitoId, публичные/приватные ссылки Диска, IP, stop, реактивация |
| [04-common-params.md](04-common-params.md) | Общие параметры (Id, DateBegin/End, ImageUrls, Promo…) и отличия между категориями |

## 14 направлений агентства → категория → файл

| # | Направление | Категория Авито | ID | Формат | Статус | Файл |
|---|-------------|-----------------|----|--------|--------|------|
| 1 | Строительство и продажа домов | Услуги > … > Строительство домов под ключ | 77213 | Excel/CSV | ready | [templates/77213-stroitelstvo-domov-pod-klyuch.md](templates/77213-stroitelstvo-domov-pod-klyuch.md) |
| 1 | Строительство и продажа домов | Недвижимость > Дома, дачи, коттеджи > Продам | 67060 | Excel/CSV | ready | [templates/67060-prodam-doma-dachi.md](templates/67060-prodam-doma-dachi.md) |
| 2 | Недвижимость и юр. сопровождение | Квартиры > Продам > Новостройка | 67066 | Excel/CSV | ready | [templates/67066-novostrojka.md](templates/67066-novostrojka.md) |
| 2 | Недвижимость и юр. сопровождение | Квартиры > Продам > Новостройка | 67066 | XML | ready | [templates/67066-novostrojka-xml.md](templates/67066-novostrojka-xml.md) |
| 2 | Недвижимость и юр. сопровождение | Деловые услуги > Консультации по недвижимости | 113772 | Excel/CSV | ready | [templates/113772-konsultacii-po-nedvizhimosti.md](templates/113772-konsultacii-po-nedvizhimosti.md) |
| 3 | Бухгалтерские услуги | Бухгалтерия > Бухгалтерское сопровождение | 160324 | Excel/CSV | ready | [templates/160324-buhgalterskoe-soprovozhdenie.md](templates/160324-buhgalterskoe-soprovozhdenie.md) |
| 4 | Юридические услуги | Юр. услуги > Сопровождение бизнеса | 160039 | Excel/CSV | ready | [templates/160039-soprovozhdenie-biznesa.md](templates/160039-soprovozhdenie-biznesa.md) |
| 4 | Юридические услуги | Юр. услуги > Услуги для физлиц | 160040 | Excel/CSV | ready | [templates/160040-uslugi-dlya-fizlic.md](templates/160040-uslugi-dlya-fizlic.md) |
| 5 | Продажа готового бизнеса | Готовый бизнес > Другое | 95759 | — | pending | [templates/_pending/95759.md](templates/_pending/95759.md) |
| 5 | Продажа готового бизнеса | Готовый бизнес > Сфера услуг > Деловые услуги | 108737 | Excel/CSV | ready | [templates/108737-gotovyj-biznes-delovye-uslugi.md](templates/108737-gotovyj-biznes-delovye-uslugi.md) |
| 6 | Производство и продажа мебели | Мебель > Кухонные гарнитуры > Кухни | 95712 | Excel/CSV | ready | [templates/95712-kuhni.md](templates/95712-kuhni.md) |
| 6 | Производство и продажа мебели | Изготовление изделий | 133602 | — | pending | [templates/_pending/133602.md](templates/_pending/133602.md) |
| 7 | Аренда автомобилей | Аренда авто > Авто для личного использования | 66880 | Excel/CSV | ready | [templates/66880-arenda-avto-lichnoe.md](templates/66880-arenda-avto-lichnoe.md) |
| 8 | Подбор персонала и вакансии | Работа > Вакансии | 67095 | Excel/CSV | ready | [templates/67095-vakansii.md](templates/67095-vakansii.md) |
| 9 | Фулфилмент / WB-Ozon | Грузчики, склад > Фулфилмент | 71663 | — | pending | [templates/_pending/71663.md](templates/_pending/71663.md) |
| 10 | Косметология | Красота > Косметология | 68122 | — | pending | [templates/_pending/68122.md](templates/_pending/68122.md) |
| 11 | Макияж, причёски, визажисты | Красота > Макияж | 66919 | — | pending | [templates/_pending/66919.md](templates/_pending/66919.md) |
| 11 | Макияж, причёски, визажисты | Красота > Услуги парикмахера | 66918 | Excel/CSV | ready | [templates/66918-uslugi-parikmahera.md](templates/66918-uslugi-parikmahera.md) |
| 12 | Психологи и коучи | Здоровье > Психология | 121172 | — | pending | [templates/_pending/121172.md](templates/_pending/121172.md) |
| 13 | Онлайн-образование, ЕГЭ/ОГЭ | Обучение > Предметы школы и вуза | 147898 | Excel/CSV | ready | [templates/147898-predmety-shkoly-i-vuza.md](templates/147898-predmety-shkoly-i-vuza.md) |
| 14 | Обучение авитолога / нейросети | Обучение > Профессии и бизнес | 68218 | Excel/CSV | ready | [templates/68218-professii-i-biznes.md](templates/68218-professii-i-biznes.md) |
| 14 | Обучение авитолога / нейросети | IT > ИИ-решения, нейросети | 149652 | — | pending | [templates/_pending/149652.md](templates/_pending/149652.md) |

## Быстрый lookup по ID

| ID | Файл |
|----|------|
| 66880 | templates/66880-arenda-avto-lichnoe.md |
| 66918 | templates/66918-uslugi-parikmahera.md |
| 66919 | templates/_pending/66919.md |
| 67060 | templates/67060-prodam-doma-dachi.md |
| 67066 | templates/67066-novostrojka.md (+ xml) |
| 67095 | templates/67095-vakansii.md |
| 68122 | templates/_pending/68122.md |
| 68218 | templates/68218-professii-i-biznes.md |
| 71663 | templates/_pending/71663.md |
| 77213 | templates/77213-stroitelstvo-domov-pod-klyuch.md |
| 95712 | templates/95712-kuhni.md |
| 95759 | templates/_pending/95759.md |
| 108737 | templates/108737-gotovyj-biznes-delovye-uslugi.md |
| 113772 | templates/113772-konsultacii-po-nedvizhimosti.md |
| 121172 | templates/_pending/121172.md |
| 133602 | templates/_pending/133602.md |
| 147898 | templates/147898-predmety-shkoly-i-vuza.md |
| 149652 | templates/_pending/149652.md |
| 160039 | templates/160039-soprovozhdenie-biznesa.md |
| 160040 | templates/160040-uslugi-dlya-fizlic.md |
| 160324 | templates/160324-buhgalterskoe-soprovozhdenie.md |
