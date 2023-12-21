from sqlalchemy import select, desc, asc
import sys
sys.setrecursionlimit(50000)
from bd.db import session
from bd.orms.orm import HeadPhones


class HeadPhonesRepository:
    def priceDesc(self):
        products = select(HeadPhones).order_by(desc(HeadPhones.price)).limit(5)
        productRes = session.execute(products).scalars().all()

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result


    def priceAsc(self):
        products = select(HeadPhones).order_by(asc(HeadPhones.price)).limit(5)
        productRes = session.execute(products).scalars().all()

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result


    def find_one_by_name(self, name: str):
        stmt = select(HeadPhones).where(HeadPhones.name == name)
        result = session.execute(stmt)

        return result.scalars().first()

    def sort_by_discount(self):
        products = select(HeadPhones).order_by(asc(HeadPhones.discount)).limit(5)
        productRes = session.execute(products).scalars().all()

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result

    def get_by_name(self, name: str):
        products = select(HeadPhones).where(HeadPhones.name == name)
        productRes = session.execute(products).scalars().all()

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result

    def create_head(self, name , price, description,showcase,discount,image):
        head_phones = HeadPhones(name=name, price=price, description=description, showcase=showcase, discount=discount, image=image)
        session.add(head_phones)
        session.commit()

    def get_all_heads(self):
        products = select(HeadPhones).limit(5)
        productRes = session.execute(products).scalars().all()

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result



    def update(self):
        session.commit()

        return

