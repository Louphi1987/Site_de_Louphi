from flask_frozen import Freezer
from app import app  # Remplace 'app.py' par le nom du fichier Flask (sans l'extension .py)

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
