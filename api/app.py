from flask import Flask
from .routes import products

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


app = Flask(__name__)
app.register_blueprint(products.bp)

if __name__ == "__main__":
    app.run(debug=True)