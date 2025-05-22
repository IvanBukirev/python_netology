import json
import os

import sqlalchemy as sq
from dotenv import load_dotenv
from models import Book, Publisher, Sale, Shop, Stock, create_tables
from sqlalchemy.orm import sessionmaker

load_dotenv("../../.env")

database_name = os.getenv("DATABASE_NAME")
user_name = os.getenv("USER_NAME")
password = os.getenv("USER_PASSWORD")
db_port = os.getenv("DB_PORT")
db_host = os.getenv("DB_HOST")

DSN = "postgresql://{}:{}@{}:{}/{}".format(
    user_name, password, db_host, db_port, database_name
)
engine = sq.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open("test_data.json", "r") as f:
    data = json.load(f)

    for item in data:
        model = {
            "publisher": Publisher,
            "book": Book,
            "shop": Shop,
            "stock": Stock,
            "sale": Sale,
        }[item.get("model")]
        session.add(model(id=item.get("pk"), **item.get("fields")))
    session.commit()


def get_puplisher_sales(publisher_input):

    if publisher_input.isdigit():
        publisher = (
            session.query(Publisher)
            .filter(Publisher.id == int(publisher_input))
            .first()
        )
    else:
        publisher = (
            session.query(Publisher)
            .filter(Publisher.name.ilike(f"%{publisher_input}%"))
            .first()
        )

    if not publisher:
        print("Издатель не найден")
        return

    sales = (
        session.query(
            Book.title.label("book_title"),
            Shop.name.label("shop_name"),
            Sale.price,
            Sale.date_sale,
        )
        .join(Stock, Stock.id_book == Book.id)
        .join(Shop, Stock.id_shop == Shop.id)
        .join(Sale, Sale.id_stock == Stock.id)
        .filter(Book.id_publisher == publisher.id)
        .order_by(Sale.date_sale)
    ).all()
    if not sales:
        print(f"Продажи книг издателя '{publisher.name}' не найдены")
        return

    print(f"\nПродажи книг издателя '{publisher.name}':")
    print("-" * 90)
    print(f"{'Название книги':<40} | {'Магазин':<20} | {'Цена':<10} | {'Дата продажи'}")
    print("-" * 90)
    for sale in sales:
        print(
            f"{sale.book_title:<40} | {sale.shop_name:<20} | {sale.price:<10.2f} | {sale.date_sale.strftime('%Y-%m-%d')}"
        )


session.close()


def demo():
    print("Поиск продаж книг по издателю")
    publisher_input = input("Введите название издателя или его идентификатор:").strip()
    get_puplisher_sales(publisher_input)


if __name__ == "__main__":
    demo()
