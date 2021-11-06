import requests
import json

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "bx-ajax": "true"
}


def get_page(url):
    s = requests.Session ()
    response = s.get(url=url, headers=headers)

    with open("index.html", "w", encoding="utf-8") as file:
        file.write(response.text)

def get_json(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

def main():
    get_json(url="https://salomon.ru/catalog/muzhchiny/obuv/?utm_source=google&utm_medium=cpc&utm_campaign=Salomon_rf_poisk_brand&utm_term=%D1%81%D0%B0%D0%BB%D0%BE%D0%BC%D0%BE%D0%BD&gclid=EAIaIQobChMI86z0mu6D9AIVC553Ch1x8A5wEAAYASABEgKCxvD_BwE&PAGEN_1=2")

if __name__ == '__main__':
    main()
