from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

# DATABASE = {
#     'drivername': 'postgres', #Тут можно использовать MySQL или другой драйвер
#     'host': 'localhost',
#     'port': '5432',
#     'username': 'app',
#     'password': '1234',
#     'database': 'test'
# }
#
# engine = create_engine(URL(**DATABASE))
DeclarativeBase = declarative_base()

class Advertisement(DeclarativeBase):
    __tablename__ = 'advertisement'

    id = Column(Integer, primary_key=True)
    heading = Column('heading', String)
    description = Column('description', String)
    date_of_creation = Column('date', String)
    owner = Column('owner', String)

    def __repr__(self):
        return "".format(self)

def main():
    engine = create_engine('postgresql+psycopg2://postgres:Komar529+@localhost/test')
    # engine = create_engine('postgresql://app:1234@localhost:5444/test')
    DeclarativeBase.metadata.create_all(engine)

    # Создаем фабрику для создания экземпляров Session. Для создания фабрики в аргументе
    # bind передаем объект engine
    Session = sessionmaker(bind=engine)

    # Создаем объект сессии из вышесозданной фабрики Session
    session = Session()

    # Создаем новую запись.
    new_post = Advertisement(heading='Auto', description='Cool', date_of_creation='Today', owner='Vasya')
    new_post2 = Advertisement(heading='Auto2', description='Cool2', date_of_creation='Today2', owner='Vasya2')
    # Добавляем запись
    session.add(new_post)
    session.add(new_post2)

    # Благодаря этой строчке мы добавляем данные а таблицу
    session.commit()

    # А теперь попробуем вывести все посты , которые есть в нашей таблице
    for post in session.query(Advertisement):
        print(post)


if __name__ == "__main__":
    main()