import json
import os

import sqlalchemy as sq
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

load_dotenv('../../.env')

database_name = os.getenv("DATABASE_NAME")
user_name = os.getenv("USER_NAME")
password = os.getenv("USER_PASSWORD")

DSN = 'postgresql://{}:{}@localhost:5432/{}'.format(user_name, password, database_name)
engine = sq.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('test_data.json', 'r') as f:
    data = json.load(f)

    for item in data:
        model = {
                'publisher': Publisher,
                'book':      Book,
                'shop':      Shop,
                'stock':     Stock,
                'sale':      Sale
        }[item.get('model')]
        model_id = f'{model}_id'
        session.add(model(id=item.get('pk'), **item.get('fields')))
    session.commit()


def get_puplisher_sales(publisher_input):
    if publisher_input.isdigit():
        publisher = session.query(Publisher).filter(Publisher.id == publisher_input).first()
    else:
        publisher = session.query(Publisher).filter(Publisher.name.ilike(f'%{publisher_input}%')).first()

    if not publisher:
        print("Издатель не найден")
        return

    sales = ((session.query(
            Book.title.label('book_title'),
            Shop.name.label('shop_name'),
            Sale.price,
            Sale.date_sale)
              .join(Stock, Stock.id_book == Book.id)
              .join(Shop, Shop.id == Stock.id_shop)
              .join(Sale, Sale.id_stock == Stock.id)
              .filter(Book.id_publisher == publisher.id)
              .order_by(Sale.date_sale))
             .all())
    if not sales:
        print(f"Продажи книг издателя '{publisher.name}' не найдены")
        return

    print(f"\nПродажи книг издателя '{publisher.name}':")
    print("-" * 80)
    print(f"{'Название книги':<40} | {'Магазин':<20} | {'Цена':<10} | {'Дата продажи'}")
    print("-" * 80)
    for sale in sales:
        print(f"{sale.book_title:<40} | {sale.shop_name:<20} | {sale.price:<10.2f} | {sale.date_sale.strftime('%Y-%m-%d')}")


session.close()


def demo():
    print("Поиск продаж книг по издателю")
    print("Введите ID или имя издателя:")
    publisher_input = input().strip()
    get_puplisher_sales(publisher_input)

if __name__ == "__main__":
    demo()
