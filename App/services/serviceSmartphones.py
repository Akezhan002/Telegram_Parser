from sqlalchemy import select, desc, asc

from App.repositories.smartphonesRepository import SmartPhonesRepository
from bd.db import session
from bd.orms.orm import HeadPhones, SmartPhones


class SmartPhonesService:
    def __init__(self):
        self._smartPhones_repo = SmartPhonesRepository()

    def priceDesc(self):
        smart_phones = self._smartPhones_repo.priceDesc()
        phones_list = list()

        for phones in smart_phones:
            phones_list.append({
                "id": phones.id, "name": phones.name, "price": phones.price, "description": phones.description,
                 "showcase": phones.showcase, "discount": phones.discount, "image": phones.image
            })

        return phones_list


    def priceAsc(self):
        smart_phones = self._smartPhones_repo.priceAsc()
        phones_list = list()

        for phones in smart_phones:
            phones_list.append({
                "id": phones.id, "name": phones.name, "price": phones.price, "description": phones.description,
                 "showcase": phones.showcase, "discount": phones.discount, "image": phones.image
            })

        return phones_list


    def find_one_by_name(self, phone_name: str):
        smart_phones = self._smartPhones_repo.find_one_by_name(phone_name)

        return smart_phones

    def sort_by_discount(self):
        smart_phones = self._smartPhones_repo.sort_by_discount()
        phones_list = list()

        for phones in smart_phones:
            phones_list.append({
                "id": phones.id, "name": phones.name, "price": phones.price, "description": phones.description,
                 "showcase": phones.showcase, "discount": phones.discount, "image": phones.image
            })

        return phones_list

    def get_by_name(self, phone_name: str):
        smart_phones = self._smartPhones_repo.get_by_name(phone_name)
        phones_list = list()

        for phones in smart_phones:
            phones_list.append({
                "id": phones.id, "name": phones.name, "price": phones.price, "description": phones.description,
                "showcase": phones.showcase, "discount": phones.discount, "image": phones.image
            })

        return phones_list

    def create_phones(self, name , price, description,showcase,discount,image):
        self._smartPhones_repo.create_phones(name,price,description,showcase,discount,image)


    def update(self):
        session.commit()

        return
