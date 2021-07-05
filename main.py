import requests
from bs4 import BeautifulSoup
import sys


def get_and_write_data(url):
    # Получаем хтмл запрашиваемой страницы
    r = requests.get(url)
    parsed_html = BeautifulSoup(r.text, 'lxml')

    # Вычленяем карточки компаний
    elements = parsed_html.select(
        'div.styles_businessUnitCardsContainer__1ggaO a.link_internal__YpiJI.link_wrapper__LEdx5')

    file = open(f'results/{filename}', "a")
    # Записываем урлы из карточек в цикле
    for el in elements:
        file.write(el.get('href').split('/')[2] + '\n')

    file.close()

    # Ищем кнопку следующей страницы
    next_page = parsed_html.select('[name="pagination-button-next"]')

    # Если следующая страница существует, возвращаем её урл
    if next_page:
        print(f'Parsing {next_page[0].get("href")}')
        return base_url + next_page[0].get('href')
    return False


base_url = 'https://www.trustpilot.com'

# Получем стартовый урл из команды запуска скрипта и последний аргумент берем в качестве названия файла
start_url = sys.argv[1]
filename = start_url.split('/')[-1] + '.csv'

# очистка файла
file = open(f'results/{filename}', "w")
file.write("")
file.close()

# Парсим первую страницу
next_page_url = get_and_write_data(start_url)

# Если функция вернула урл следующей страницы, вызываем ее еще раз
while next_page_url:
    next_page_url = get_and_write_data(next_page_url)

print('finish')
