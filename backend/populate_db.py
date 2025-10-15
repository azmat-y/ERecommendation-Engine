# populate_db.py
import random
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.db import SessionLocal, Base, engine
from app.models import Product, Event

# Create tables if not exist
Base.metadata.create_all(bind=engine)

# Electronics product names
electronics_products = [
    "Samsung M35",
    "Realme T300",
    "iPhone 14",
    "OnePlus 12",
    "Sony WH-1000XM5",
    "Apple AirPods Pro",
    "Lenovo ThinkPad X1",
    "Logitech MX Master 3",
    "Dell XPS 13",
    "HP Spectre x360",
    "Asus ZenBook 14",
    "Canon EOS R5",
    "Nikon D850",
    "GoPro Hero 11",
    "Samsung Galaxy Tab S9",
    "iPad Pro 2023",
    "Microsoft Surface Pro 9",
    "Amazon Echo Dot",
    "Google Nest Hub",
    "Sony PlayStation 5",
    "Xbox Series X",
    "Nintendo Switch OLED",
    'Samsung QLED TV 55"',
    'LG OLED TV 65"',
    "Bose QuietComfort 45",
    "JBL Flip 6",
    "Anker PowerCore 26800",
    "Razer DeathAdder V3",
    "Corsair K95 Keyboard",
    "Logitech G502 Mouse",
    "Sony Alpha A7 III",
    "DJI Mini 4 Pro",
    "Fitbit Charge 6",
    "Garmin Fenix 7",
    "Samsung Galaxy Watch 6",
    "Apple Watch Series 9",
    "Kindle Paperwhite 5",
    "Ring Video Doorbell 4",
    "Nest Thermostat E",
    "Philips Hue Starter Kit",
    "Dyson Supersonic Hair Dryer",
    "iRobot Roomba i7+",
    "Canon PIXMA TS8320",
    "HP Envy 6055",
    "LG Soundbar SN7Y",
    "Samsung T7 SSD 2TB",
    "Seagate Expansion 5TB",
    "Western Digital My Passport 4TB",
    "Logitech StreamCam",
    "Elgato Key Light Air",
]

event_types = ["click", "view", "purchase"]

NUM_PRODUCTS = 50
NUM_USERS = 10
NUM_EVENTS = 300


def populate_products(session: Session):
    products = []

    # Shuffle and pick NUM_PRODUCTS
    random.shuffle(electronics_products)
    selected_products = electronics_products[:NUM_PRODUCTS]

    for name in selected_products:
        price = round(random.uniform(50, 2000), 2)  # realistic electronics price
        product = Product(name=name, category="Electronics", price=price)
        session.add(product)
        products.append(product)

    session.commit()
    print(f"Inserted {len(products)} products.")
    return products


def populate_events(session: Session, products):
    events = []
    for _ in range(NUM_EVENTS):
        event = Event(
            user_id=random.randint(1, NUM_USERS),
            product_id=random.choice(products).id,
            event_type=random.choice(event_types),
            timestamp=datetime.utcnow() - timedelta(days=random.randint(0, 30)),
        )
        session.add(event)
        events.append(event)

    session.commit()
    print(f"Inserted {len(events)} events.")


def main():
    with SessionLocal() as session:
        products = populate_products(session)
        populate_events(session, products)
    print("Database population complete.")


if __name__ == "__main__":
    main()
