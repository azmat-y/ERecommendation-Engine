from .ranker import rank_products
from ..models import Product
from ..db import SessionLocal


def get_recommendations_for_user(user_id: int) -> list[Product]:
    ranked = rank_products(user_id)
    top_ids = [pid for pid, _ in ranked[:10]]

    with SessionLocal() as session:
        products = session.query(Product).filter(Product.id.in_(top_ids)).all()
        return products
