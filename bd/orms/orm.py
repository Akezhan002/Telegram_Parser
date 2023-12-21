from sqlalchemy import Column, VARCHAR, Float, INTEGER
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'Laptops'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    price = Column(INTEGER)
    description = Column(VARCHAR(255))
    showcase = Column(VARCHAR(225))
    discount = Column(INTEGER)
    image = Column(VARCHAR(255))

class HeadPhones(Base):
    __tablename__ = 'HeadPhones'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    price = Column(INTEGER)
    description = Column(VARCHAR(255))
    showcase = Column(VARCHAR(225))
    discount = Column(INTEGER)
    image = Column(VARCHAR(255))

class SmartPhones(Base):
    __tablename__ = 'SmartPhones'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255))
    price = Column(INTEGER)
    description = Column(VARCHAR(255))
    showcase = Column(VARCHAR(225))
    discount = Column(INTEGER)
    image = Column(VARCHAR(255))


