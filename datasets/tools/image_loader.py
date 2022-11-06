import json
import os
import time

from requests import get
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def json_load() -> (dict):
    '''
    Загрузка информации о партиях из JSON файла.

    Args:
        None
    Returns:
        all_partys (dict): общий словарь типа {"party": {"name": "url"}}
    '''
    if not "datasets" in os.getcwd():
        os.chdir(os.getcwd() + "/datasets")
    
    try:
        with open("subjects.json", "r", encoding='utf8') as JSON:
            all_partys = json.load(JSON)
    except:
        print(" ! \'subjects.json\' file is missing from: ~/Which-political-party/datasets")
        return

    return all_partys

def photo_search(url:str) -> (str):
    '''
    Проверка наличия изображения члена партии на странице в Википедии.

    Args:
        usr (str): URL адрес страницы в Википедии
    Returns:
        img_url (str): URL адрес изображения
    '''
    try:
        page = BeautifulSoup(get(url, headers={'User-Agent': 'PseudoBot/1.0 (pseudo.developer.ru@gmail.com) bot'}).content, "html.parser")
    except:
        print("! INTERRUPT !\n! Too Many Requests !")
        time.sleep(60)
        page = BeautifulSoup(get(url, headers={'User-Agent': 'PseudoBot/1.0 (pseudo.developer.ru@gmail.com) bot'}).content, "html.parser")

    img_zone = page.find("tbody")
    if img_zone == None:
        return None
    else:
        img_zone = img_zone.find("td", class_="infobox-image")

    if img_zone == None:
        return None
    else:
        img = img_zone.find("img", src=True)
        if img == None:
            return None
        else:
            img_url = "https:" + img["src"]

        return img_url

def photo_install(party_name:str, person_name:str, url:str) -> (None):
    '''
    Загрузка изображения члена партии из Википедии.
    Изображения имеют названия, соответствующие ФИО членов партии.
    Название папок совпадает с названием партий.

    Args:
        party_name (str): имя текущей партии
        person_name (str): ФИО текущего члена партии
        url (str): ссылка в Википедии на текущего члена партии
    Returns:
        None
    '''
    # Перемещение в директорию /datasets
    if not "datasets" in os.getcwd():
        os.chdir(os.getcwd() + "/datasets")

    # Создание директории с названием партии, при её отсутствии
    if not party_name in os.listdir():
        os.mkdir(party_name) 

    img_url = photo_search(url)
    if not img_url == None:
        try:
            urlretrieve(img_url, f'{party_name}/{person_name}.jpg')
        except:
            pass
    return