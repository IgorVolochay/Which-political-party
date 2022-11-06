
import json
import os

from requests import get
from bs4 import BeautifulSoup


def find_next_page(page:str) -> (str):
    '''
    Поиск гиперссылок для перехода на следующую страницу Википедии.

    Args:
        url (str): URL текущей страницы
    Returns:
        next_url (str): URL, ведущая на следующую страницу
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
    Поиск и запись всех URL ссылок в Википедии о членах партии.

    Args:
        url (str): URL страницы каталога членов партии
        party_list (list): список уже записанных членов (инициализируется пустым)
    Returns:
        party_list (list): список всех членов партии
    '''
    print(len(party_list))
    page = BeautifulSoup(get(url).content, "html.parser")
    
    lists = page.find("div", class_="mw-category mw-category-columns")

    persons_list = lists.find_all("a", href=True)
    party_list.extend(persons_list)

    next_page_url = find_next_page(page)
    if not next_page_url == None:
        get_url(next_page_url, party_list) # Организация рекурсии

    return party_list

def data_organization(party_name:str, raw_data:list) -> (dict):
    '''
    Организация данных для последующей упаковки в JSON файл.

    Args:
        party_name (str): имя текущей партии
        raw_data (list): список членов текущей партии
    Returns:
        party_dict (dict): словарь типа {"Партия": {"ФИО": "URL"}}
    '''
    subject_dict = dict()

    for subject in raw_data:
        subject_dict[str(subject.string)] = "https://ru.wikipedia.org" + str(subject["href"])

    party_dict = {party_name: subject_dict}
    return party_dict

def create_json(party_dict:dict, all_dict = dict()) -> (None):
    '''
    Запись информации о партии, ФИО членов партий и их URL ссылок.

    Args:
        subjects_dict (dict): общий словарь типа {"party": {"name": "url"}}
    Returns:
        None
    '''
    if not "datasets" in os.getcwd():
        os.chdir(os.getcwd() + "/datasets")

    if "subjects.json" in os.listdir():
        with open("subjects.json", "r", encoding='utf-8') as old_file:
            all_dict = json.load(old_file)

    all_dict.update(party_dict)
    with open("subjects.json", "w", encoding='utf8') as JSON:
        json.dump(all_dict, JSON, indent=4, ensure_ascii=False)

    return