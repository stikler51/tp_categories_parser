# tp_categories_parser

Парсер категорий для сайта https://www.trustpilot.com/

Установка: pip install -r requirements.txt

Использование: py main.py <category_url>

Пример использования: py main.py https://www.trustpilot.com/categories/travel_insurance_company

В данном случае распарсится указанная категория. Результат будет сохранен в файл results/travel_insurance_company.csv

ВАЖНО: <category_url> НЕ ДОЛЖЕН содержать get параметр страницы (?page=12), иначе парсинг начнется не с первой страницы, а с указанной