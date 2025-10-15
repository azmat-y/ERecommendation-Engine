from flask import Flask
from flask_cors import CORS
from .db import Base, engine
from .routes.recommend import recommend_bp


Base.metadata.create_all(bind=engine)


app = Flask(__name__)
CORS(app)
app.register_blueprint(recommend_bp)


@app.get("/")
def root():
    return {"message": "E-commerce recommender is running (SQLite + Gemini)."}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
