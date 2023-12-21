from sqlalchemy import select, desc, asc

from App.repositories.laptopRepository import LaptopRepository
from bd.db import session
from bd.orms.orm import Product


class LaptopService:
    def __init__(self):
        self._laptop_repo = LaptopRepository()

    def priceDesc(self):
        laptops = self._laptop_repo.priceDesc()
        laptop_list = list()

        for laptop in laptops:
            laptop_list.append({
                "id": laptop.id, "name": laptop.name, "price": laptop.price, "description": laptop.description,
                "showcase": laptop.showcase, "discount": laptop.discount, "image": laptop.image
            })

        return laptop_list

    def priceAsc(self):
        laptops = self._laptop_repo.priceAsc()
        laptop_list = list()

        for laptop in laptops:
            laptop_list.append({
                "id": laptop.id, "name": laptop.name, "price": laptop.price, "description": laptop.description,
                "showcase": laptop.showcase, "discount": laptop.discount, "image": laptop.image
            })

        return laptop_list

    def find_one_by_name(self, laptop_name: str):
        laptops = self._laptop_repo.find_one_by_name(laptop_name)

        return laptops

    def sort_by_discount(self):
        laptops = self._laptop_repo.sort_by_discount()
        laptop_list = list()

        for laptop in laptops:
            laptop_list.append({
                "id": laptop.id, "name": laptop.name, "price": laptop.price, "description": laptop.description,
                "showcase": laptop.showcase, "discount": laptop.discount, "image": laptop.image
            })

        return laptop_list

    def get_by_name(self, laptop_name: str):
        laptops = self._laptop_repo.get_by_name(laptop_name)
        laptop_list = list()

        for laptop in laptops:
            laptop_list.append({
                "id": laptop.id, "name": laptop.name, "price": laptop.price, "description": laptop.description,
                "showcase": laptop.showcase, "discount": laptop.discount, "image": laptop.image
            })

        return laptop_list

    def create_laptop(self, name , price, description,showcase,discount,image):
        self._laptop_repo.create_laptop(name,price,description,showcase,discount,image)

    def get_all_laptops(self):
        heads = self._laptop_repo.get_all_laptops()
        print(heads)
        return heads
    def update(self):
        session.commit()

        return
