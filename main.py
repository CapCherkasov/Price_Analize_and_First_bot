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


def collect_data():
    s = requests.Session()
    responce = s.get(url="https://salomon.ru/catalog/muzhchiny/obuv/filter/size-is-8.5%20uk/apply/?PAGEN_1=1", headers=headers)

    data = responce.json()
    pagination_count = data.get("pagination").get("pageCount")

    result_data = []
    items_urls = []
    for page_count in range (1, pagination_count+1):
        url = f"https://salomon.ru/catalog/muzhchiny/obuv/filter/size-is-8.5%20uk/apply/?PAGEN_1={page_count}"
        r = s.get(url=url, headers=headers)

        data = r.json()
        products = data.get("products")

        for product in products:
            product_colours = product.get("colors")

            for pc in product_colours:
                dicount_percent = pc.get("price").get("discountPercent")

                if dicount_percent >= 50 and pc.get("link") not in items_urls:
                    items_urls.append(pc.get("link"))
                    result_data.append(
                        {
                            "title": pc.get("title"),
                            "category": pc.get("category"),
                            "link":f'https://salomon.ru{pc.get("link")}',
                            "price_base": pc.get("price").get("base"),
                            "price_sale": pc.get("price").get("sale"),
                            "discount_percent": dicount_percent
                        }
                    )
            print(f"{page_count}/{pagination_count}")
        with open("result_data.json", "w", encoding="utf-8") as file:
            json.dump(result_data, file, indent=4, ensure_ascii=False)



def main():
    # get_json(url="https://salomon.ru/catalog/muzhchiny/obuv/filter/size-is-8.5%20uk/apply/?PAGEN_1=2")
    collect_data()

if __name__ == '__main__':
    main()
