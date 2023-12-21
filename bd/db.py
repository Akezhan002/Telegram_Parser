from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bd.orms.orm import Base

engine = create_engine(
    "postgresql+psycopg2://user:root@localhost:54332/postgres",
)

Session = sessionmaker(engine)

with Session.begin() as session:
    print('1')


Base.metadata.create_all(engine)
