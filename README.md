Парсим [Steam](https://store.steampowered.com/) с помощью Scrapy!

Необходимо выбрать 3 запроса (indie, гонки, football)

* Все игры на первых 2 страницах

И для каждой игры вытащить:

* Название

* Категорию (весь путь, за исключением Все игры и самого названия игры)

* Число всех обзоров и общая оценка

* Дата выхода

* Разработчик

* Метки (тэги) игры

* Цена

* Доступные платформы

Сохраните игры в формате json, оставив только игры, выпущенные после 2000 года

Запустить:
```
scrapy crawl steam -O items.json
```
