from sqlalchemy import select, desc, asc

from bd.db import session
from bd.orms.orm import Product


class LaptopRepository:
    def priceDesc(self):
        products = select(Product).order_by(desc(Product.price)).limit(5)
        productRes = session.execute(products).scalars().all()

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result


    def priceAsc(self):
        products = select(Product).order_by(asc(Product.price)).limit(5)
        productRes = session.execute(products).scalars().all()

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result


    def find_one_by_name(self, name: str):
        stmt = select(Product).where(Product.name == name)
        result = session.execute(stmt)

        return result.scalars().first()

    def sort_by_discount(self):
        products = select(Product).order_by(asc(Product.discount)).limit(5)
        productRes = session.execute(products).scalars().all()

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })

        return result

    def get_by_name(self, name: str):
        products = select(Product).where(Product.name == name)
        productRes = session.execute(products).scalars().all()
        print(productRes)

        result = []
        for product in productRes:
            result.append({
                "id": product.id, "name": product.name, "price": product.price, "description": product.description,
                 "showcase": product.showcase, "discount": product.discount, "image": product.image
            })
        return result

    def create_laptop(self, name , price, description,showcase,discount,image):
        laptops = Product(name=name, price=price, description=description, showcase=showcase, discount=discount, image=image)
        session.add(laptops)
        session.commit()

    def get_all_laptops(self):
        products = select(Product).limit(5)
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
