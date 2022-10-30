
from requests import get
from bs4 import BeautifulSoup

URL1 = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%C2%AB%D0%95%D0%B4%D0%B8%D0%BD%D0%BE%D0%B9_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8%C2%BB"
URL2 = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%D0%9B%D0%94%D0%9F%D0%A0"
URL3 = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%D0%BF%D0%B0%D1%80%D1%82%D0%B8%D0%B8_%D0%9D%D0%BE%D0%B2%D1%8B%D0%B5_%D0%BB%D1%8E%D0%B4%D0%B8"
URL4 = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%C2%AB%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%B5%D0%B4%D0%BB%D0%B8%D0%B2%D0%BE%D0%B9_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8%C2%BB"
URL_list = [URL1, URL2, URL3, URL4]

def next_pages(page:str) -> (str):
    '''
    Поиск гиперссылок для перехода на следующую страницу Википедии.

    Args:
        url (str): url текущей страницы
    Returns:
        next_url (str): url, ведущая на следующую страницу
    '''
    find_next_page = page.find("div", {"id": "mw-pages"}).find_all("a", href=True)

    if "Следующая страница" in find_next_page[1]:
        return str("https://ru.wikipedia.org/"+str(find_next_page[1]["href"]))
    elif "Следующая страница" in find_next_page[2]:
        return str("https://ru.wikipedia.org/"+str(find_next_page[2]["href"]))
    else:
        return None

def get_url(url:str, party_index:int) -> (list):
    page = BeautifulSoup(get(url).content, "html.parser")
    
    next_page_url = next_pages(page)
    if not next_page_url == None:
        get_url(next_page_url, party_index)

    lists = page.find("div", class_="mw-category mw-category-columns")
    persons_list = lists.find_all("a", href=True)

    party_list[party_index].extend(persons_list)
    return

ER = list()
LDPR = list()
NL = list()
SR = list()
party_list = [ER, LDPR, NL, SR]

get_url(URL1, 0)
print(len(ER))