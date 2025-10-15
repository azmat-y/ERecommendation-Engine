# E-commerce Product Recommender

This is a simple **E-commerce Product Recommendation** system that combines **user-product interaction data** with **LLM-powered explanations** for recommended products. It uses **SQLite** for storage and can generate explanations using the **Gemini model**.  

---

## Features

- Recommend products for a given user based on past interactions.
- Provide **natural language explanations** for each recommendation.
- Simple frontend to input a user ID and view top recommendations.
- Vanilla JS frontend, easily runnable without build tools.
- SQLite database for easy local setup.

---

## Tech Stack

- **Backend**: Python, Flask, SQLAlchemy, SQLite
- **LLM**: Gemini API 
- **Frontend**: Vanilla JavaScript, HTML, CSS
  
---

## Setup Instructions

```bash
git clone <repo-url>
cd ERecommendation-Engine/backend
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt

# populate db
python populate_db.py

# run backend
python -m app.main
```
To run the fronend just open the index.html I have used only vanila js so this should work fine.
Now, based on userid we can get recommendation with LLM explainations.

## Demo
A demo videos is available in the repo.
