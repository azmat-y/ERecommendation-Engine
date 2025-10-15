from flask import Blueprint, request, jsonify
from ..recommender.recommender import get_recommendations_for_user
from ..recommender.llm import explain_recommendation


recommend_bp = Blueprint("recommend", __name__)


@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    user_id = data.get("user_id")

    products = get_recommendations_for_user(user_id)
    behavior_summary = f"User recently interacted with {len(products)} products."

    output = []
    for product in products:
        explanation = explain_recommendation(user_id, product.name, behavior_summary)
        output.append(
            {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "category": product.category,
                    "price": product.price,
                },
                "explanation": explanation,
            }
        )

    return jsonify(output)
