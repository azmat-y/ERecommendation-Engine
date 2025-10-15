from sqlalchemy import text
from ..db import SessionLocal


def rank_products(uid: int):
    with SessionLocal() as session:
        results = []
        product_ids = [1, 2, 3]

        for pid in product_ids:
            count_stmt = text("SELECT count(*) FROM events WHERE product_id = :p")
            click_stmt = text(
                "SELECT count(*) FROM events WHERE user_id = :u AND product_id = :p"
            )

            count = session.execute(count_stmt, {"p": pid}).scalar_one_or_none() or 0
            clicks = (
                session.execute(click_stmt, {"u": uid, "p": pid}).scalar_one_or_none()
                or 0
            )

            score = clicks / (count + 1)
            results.append((pid, score))

        results.sort(key=lambda x: x[1], reverse=True)
        return results
