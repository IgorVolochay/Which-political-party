from tools import parser

def main() -> None:
    party_catalog = {
     "Единая Россия":       "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%C2%AB%D0%95%D0%B4%D0%B8%D0%BD%D0%BE%D0%B9_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8%C2%BB",
     "ЛДПР":                "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%D0%9B%D0%94%D0%9F%D0%A0",
     "Новые люди":          "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%D0%BF%D0%B0%D1%80%D1%82%D0%B8%D0%B8_%D0%9D%D0%BE%D0%B2%D1%8B%D0%B5_%D0%BB%D1%8E%D0%B4%D0%B8",
     "Справедливая Россия": "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%C2%AB%D0%A1%D0%BF%D1%80%D0%B0%D0%B2%D0%B5%D0%B4%D0%BB%D0%B8%D0%B2%D0%BE%D0%B9_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8%C2%BB",
     "КПРФ":                "https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A7%D0%BB%D0%B5%D0%BD%D1%8B_%D0%9A%D0%9F%D0%A0%D0%A4"
    }

    for party_name in party_catalog:
        party_list = parser.get_url(party_catalog[party_name])
        party_dict = parser.data_organization(party_name, party_list)
        parser.create_json(party_dict)

if __name__ == "__main__":
    main()