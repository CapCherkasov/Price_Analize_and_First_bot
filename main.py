import requests

headers = {
    "accept" = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    "user_agent" = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}


def get_page(url):
    s = requests.Session ()
    response = s.get(url=url, headers=headers)

    with open("index.html", "w") as file

def main():
    get_page(url="")


if __name__ == '__main__':
    main()
