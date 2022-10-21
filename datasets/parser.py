import requests

from bs4 import BeautifulSoup

URL1 = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%C2%AB%D0%95%D0%B4%D0%B8%D0%BD%D0%BE%D0%B9_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8%C2%BB"
URL2 = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%D0%9B%D0%94%D0%9F%D0%A0"
URL3 = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%D0%BF%D0%B0%D1%80%D1%82%D0%B8%D0%B8_%D0%9D%D0%BE%D0%B2%D1%8B%D0%B5_%D0%BB%D1%8E%D0%B4%D0%B8"
URL4 = "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%C2%AB%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%B5%D0%B4%D0%BB%D0%B8%D0%B2%D0%BE%D0%B9_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8%C2%BB"

all_persons = list()

def next_pages(url):
    page = BeautifulSoup(requests.get(url).content, "html.parser")
    find_next_page = page.find("div", {"id": "mw-pages"}).find_all("a", href=True)
    if "Следующая страница" in find_next_page[1]:
        #print("YES!", str(find_next_page[1]["href"]), sep="  ---  ")
        next_pages("https://ru.wikipedia.org/"+str(find_next_page[1]["href"]))
    elif "Следующая страница" in find_next_page[2]:
        #print("YES!", str(find_next_page[1]["href"]), sep="  ---  ")
        next_pages("https://ru.wikipedia.org/"+str(find_next_page[2]["href"]))
    else:
        pass
        #print("NO!")

    lists = page.find("div", class_="mw-category mw-category-columns")
    
    all_persons.extend(lists.find_all("a", href=True))
    pass

next_pages(URL1)

print(len(all_persons))