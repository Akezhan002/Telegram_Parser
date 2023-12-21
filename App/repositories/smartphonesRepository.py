from sqlalchemy import select, desc, asc

from bd.db import session
from bd.orms.orm import HeadPhones, SmartPhones


class SmartPhonesRepository:

    def priceDesc(self):
        products = select(SmartPhones).order_by(desc(SmartPhones.price)).limit(5)
        productRes = session.execute(products).scalars().all()

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result


    def priceAsc(self):
        products = select(SmartPhones).order_by(asc(SmartPhones.price)).limit(5)
        productRes = session.execute(products).scalars().all()

        result = []
        print(productRes)
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result


    def find_one_by_name(self, phone_name: str):
        stmt = select(SmartPhones).where(SmartPhones.name == phone_name)
        result = session.execute(stmt)

        return result.scalars().first()

    def sort_by_discount(self):
        products = select(SmartPhones).order_by(asc(SmartPhones.discount)).limit(5)
        productRes = session.execute(products).scalars().all()

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result

    def get_by_name(self, phone_name: str):
        products = select(SmartPhones).where(SmartPhones.name == phone_name)
        productRes = session.execute(products).scalars().all()

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result

    def create_phones(self, name , price, description,showcase,discount,image):
        phones = SmartPhones(name=name, price=price, description=description, showcase=showcase, discount=discount, image=image)
        session.add(phones)
        session.commit()


    def update(self):
        session.commit()

        return
