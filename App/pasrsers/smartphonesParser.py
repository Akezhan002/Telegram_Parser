import requests
from bs4 import BeautifulSoup as Bs
from App.services.serviceSmartphones import SmartPhonesService


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'kk-KZ,ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Google/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
}

for count in range(1, 8):
    url = requests.get(f"https://www.sulpak.kz/f/naushniki?page={count}")
    soup = Bs(url.text, "lxml")
    data = soup.find_all("div", class_="product__item product__item-js tile-container")

    for el in data:
        photo = el.find("img", class_="image-size-cls")
        name = el.find("div", class_="product__item-name").text
        price = el.find("div", class_="product__item-price").text
        desc = el.find("div", class_="product__item-description").text
        dis = el.find("div", class_="product__label-discount")
        showCase = el.find("div", class_="product__item-showcase").text


        nameR = name[8:]
        s1 = "".join(c for c in price if c.isalnum())
        priceR = ''.join(i for i in s1 if not i.isalpha())
        res = int(priceR)
        descR = desc.split('\n')
        photo = str(photo.get("src"))

        phones_service = SmartPhonesService()
        productHistory = phones_service.find_one_by_name(nameR)
        if productHistory is None:
            if not (dis is None):
                for a in dis:
                    s1 = "".join(c for c in a if c.isdecimal())
                    phones_service = SmartPhonesService()
                    phones_service.create_phones(nameR,res,descR[0],showCase,s1,photo)
            elif not (not (dis is None)):
                phones_service = SmartPhonesService()
                phones_service.create_phones(nameR, res, descR[0], showCase, 0, photo)
        else:
            print('parser')

