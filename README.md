# VK_apartments_posts_parcer
Скрипт на Python, позволяющий спарсить данные с нужной страницы человека или группы для получения данных о постах 
связанных с арендой квартиры.

## Как использовать?
1. Для запуска скрипта потребуется Python от версии 3.11, который можно установить с помощью [pyenv](https://habr.com/ru/articles/599441/)
2. В проекте есть файл `pyproject.toml`, вам необходимо установить все необходимые библиотеки с помощью [poetry](https://python-poetry.org/):
```bash
poetry install
```
3. Настройте `config.json`
Файл конфигурации `config.json` используется для настройки работы программы под нужды пользователя. 
Он содержит в себе:
- `api_version`: версия VK API;
- `post_per_time`: количество постов, которое должно получать VK API за одно обращение;
- `access_token`: ваш [токен доступа](https://vkhost.github.io/) (для vk.com) к методам VK API;
- `domains`: список страниц или групп ВКонтакте;
- `post_number`: число извлекаемых постов. Если указан `0`, то извлекаются все посты страницы или группы;
- `post_filter`: фильтр постов, который включает в себя:
  - `restricted_words`: список запрещённых слов;
  - `contains_words`: список слов для поиска;
4. Запустите `main.py`:
  ```bash
  python3 main.py
  ```
5. В консоли выведется краткая статистика по каждому домену в таком формате:
 ```bash
Domain = {str}
Count of all {str} posts: {int}
Count of apartments posts: {int}
Percent of apartments to all posts: {float}%
Count of {type_of_data} and percents to apartments posts count:
Count and percents of empty money: {int} - {float}%
Count and percents of duplicates: {int} - {float}%
Count and percents of blowouts: {int} - {float}%
Count and percents of losses: {int} - {float}%
Count and percents of cleared data: {int} - {float}%
```
6. Результаты будут храниться в папках с id группы или страницы в следующем формате:
- `{domain}_clear_{today_date}.csv`: csv-файл с очищенными(валидными) данными;
- `{domain}_with_blowouts.csv`: csv-файл с полными постами без дубликатов, но с выбросами цен(>40k и <5k рублей);
- `{domain}_with_duplicates.csv`: csv-файл с полными постами в которых есть дубликаты;
- `{domain}_with_empty_cost.csv`: csv-файл с постами из которых не получилось спарсить цену;

Этот репозиторий открыт для вкладов. Так что не стесняйтесь открывать issues и делать pull requests.
