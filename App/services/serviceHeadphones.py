import time

from sqlalchemy import select, desc, asc

from App.repositories.headphonesRepository import HeadPhonesRepository
from bd.db import session
from bd.orms.orm import HeadPhones


class HeadPhonesService:
    def __init__(self):
        self._headPhones_repo = HeadPhonesRepository()

    def priceDesc(self):
        head_phones = self._headPhones_repo.priceDesc()
        head_list = list()

        for head in head_phones:
            head_list.append({
                "id": head.id, "name": head.name, "price": head.price, "description": head.description,
                "showcase": head.showcase, "discount": head.discount, "image": head.image
            })

        return head_list

    def priceAsc(self):
        head_phones = self._headPhones_repo.priceAsc()
        head_list = list()

        for head in head_phones:
            head_list.append({
                "id": head.id, "name": head.name, "price": head.price, "description": head.description,
                "showcase": head.showcase, "discount": head.discount, "image": head.image
            })

        return head_list

    def find_one_by_name(self, headphones_name: str):
        head_phones = self._headPhones_repo.find_one_by_name(headphones_name)

        return head_phones

    def sort_by_discount(self):
        head_phones = self._headPhones_repo.sort_by_discount()
        head_list = list()

        for head in head_phones:
            head_list.append({
                "id": head.id, "name": head.name, "price": head.price, "description": head.description,
                "showcase": head.showcase, "discount": head.discount, "image": head.image
            })

        return head_list

    def get_by_name(self, headphones_name: str):
        head_phones = self._headPhones_repo.get_by_name(headphones_name)
        head_list = list()

        for head in head_phones:
            head_list.append({
                "id": head.id, "name": head.name, "price": head.price, "description": head.description,
                "showcase": head.showcase, "discount": head.discount, "image": head.image
            })

        return head_list

    def create_head(self, name,price,description,showcase,discount,image):
        self._headPhones_repo.create_head(name,price,description,showcase,discount,image)

    def get_all_heads(self):
        heads = self._headPhones_repo.get_all_heads()
        print(heads)
        return heads

    def update(self):
        session.commit()

        return

a = HeadPhonesService()
print(a.get_all_heads())
