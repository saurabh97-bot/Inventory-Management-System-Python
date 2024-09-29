from flask import Blueprint, request, jsonify
from models.product import Product
from models.inventory import Inventory

bp = Blueprint('products', __name__)

# Create an inventory instance (or get it from a database in real cases)
inventory = Inventory()

# Route to get all products in the inventory
@bp.route('/products', methods=['GET'])
def get_all_products():
    products = [product.__dict__ for product in inventory.products.values()]  # Assuming inventory stores products in a dict
    return jsonify(products), 200

# Route to create a new product and add it to the inventory
@bp.route('/create_products', methods=['POST'])
def create_product():
    data = request.get_json()
    
    # Create a Product object using the incoming JSON data
    product = Product(**data)
    
    # Add the product to the inventory
    inventory.add_product(product)
    
    # Return the created product's data
    return jsonify(product.__dict__), 201

# Route to get a product by ID
@bp.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = inventory.get_product(product_id)
    if product:
        return jsonify(product.__dict__), 200
    else:
        return jsonify({"error": "Product not found"}), 404

# Route to update an existing product
@bp.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = inventory.get_product(product_id)

    if product:
        # Update the product fields with the new data (if provided)
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        product.category = data.get('category', product.category)
        product.quantity = data.get('quantity', product.quantity)
        
        # Return the updated product data
        return jsonify(product.__dict__), 200
    else:
        return jsonify({"error": "Product not found"}), 404

# Route to delete a product by ID
@bp.route('/product/<int:product_id>', methods=['DELETE'])
def remove_product(product_id):
    success = inventory.remove_product(product_id)
    
    if success:
        return jsonify({"message": "Product removed successfully"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404
