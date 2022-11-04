
from requests import get
from bs4 import BeautifulSoup

URL1 = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%C2%AB%D0%95%D0%B4%D0%B8%D0%BD%D0%BE%D0%B9_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8%C2%BB"
URL2 = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%D0%9B%D0%94%D0%9F%D0%A0"
URL3 = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%D0%BF%D0%B0%D1%80%D1%82%D0%B8%D0%B8_%D0%9D%D0%BE%D0%B2%D1%8B%D0%B5_%D0%BB%D1%8E%D0%B4%D0%B8"
URL4 = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%C2%AB%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%B5%D0%B4%D0%BB%D0%B8%D0%B2%D0%BE%D0%B9_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8%C2%BB"

def find_next_page(page:str) -> (str):
    '''
    Поиск гиперссылок для перехода на следующую страницу Википедии.

    Args:
        url (str): url текущей страницы
    Returns:
        next_url (str): url, ведущая на следующую страницу
    '''
    next_page = page.find("div", {"id": "mw-pages"}).find_all("a", href=True)

    if "Следующая страница" in next_page[1]:
        return str("https://ru.wikipedia.org/"+str(next_page[1]["href"]))
    elif "Следующая страница" in next_page[2]:
        return str("https://ru.wikipedia.org/"+str(next_page[2]["href"]))
    else:
        return None

def get_url(url:str, party_list = list()) -> (list):
    '''
    Поиск и запись всех url ссылок в Википедии о членах партии.

    Args:
        url (str): url страницы каталога членов партии
        party_list (list): список уже записанных членов (инициализируется пустым)
    Returns:
        party_list (list): список всех членов партии
    '''
    page = BeautifulSoup(get(url).content, "html.parser")
    
    lists = page.find("div", class_="mw-category mw-category-columns")

    persons_list = lists.find_all("a", href=True)
    party_list.extend(persons_list)

    next_page_url = find_next_page(page)
    if not next_page_url == None:
        get_url(next_page_url, party_list) # Организация рекурсии

    return party_list