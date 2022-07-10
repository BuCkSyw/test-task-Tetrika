# задача на моем устройстве решается примерно за 50 секунд
import requests
from bs4 import BeautifulSoup

# словарь для хранения буквы животных(ключ) и количества животных(значение)
d = {}
url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
page = requests.get(url).text
# счетчик для количества животных
counter = 0


# рекурсивная функция для парсинга страницы википедии
def pars_page(page, counter):
    soup = BeautifulSoup(page, 'lxml')
    # метод для поиска ссылок на животных со страницы и заголовков начальных букв названия животных
    names_animals = soup.find('div', class_='mw-category-columns').find_all(['a', 'h3'])
    # присваиваем первую букву заголовок на странице
    bukva = names_animals[0].text
    # цикл для прохода всех ссылок и подзаголовков на странице
    for name in names_animals:
        if len(name.text) == 1:
            if bukva != name.text:
                d[bukva] = counter
                counter = 0
            bukva = name.text
            if bukva in d:
                counter = d.get(bukva)
        elif bukva == name.text[0]:
            counter += 1
    d[bukva] = counter
    # проверяем страницу на ссылку-переход на следующую страницу
    next_page = soup.find('div', id='mw-pages').find_all('a', limit=2)
    # если ссылка есть, переходим на следующую страницу и запускаем функцию для парсинга страницы
    for j in next_page:
        if j.text == 'Следующая страница':
            new_url = 'https://ru.wikipedia.org/' + j.get('href')
            new_page = requests.get(new_url).text
            pars_page(new_page, counter)


pars_page(page, counter)
for keys, values in d.items():
    print(keys, ":", values)
