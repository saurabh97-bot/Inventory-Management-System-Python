from models.product import Product
from models.sale import Sale
from models._return import Return

class Inventory:
    def __init__(self):
        self.product = {} # Initializers products as empty dictionary to store products using id as their key and Product obj as their value
        self.sales = [] # Initializing as an empty list to store all recorded transactions
        self.returns = [] # Initializes returns as an empty list to store all recorded product returns

    
    def add_product(self,product): # Method add_product adds a product to the inventory class.method takes one argument product which is an instance of inventory class
        self.product[product.id] = product

    def update_product(self,product_id,quantity):# method called update product that updates the quantity of product in the inventory.It takes two arguments product_id(to identify the product) and quantity to add quantity new value
        if product_id in self.product:# If the product exists,it updates the product quantity to the new value provided by quantity argument.This directly modifies the qauantity attribute of the Product stored in dictionary
            self.product[product_id].quantity = quantity
        else:
            print("Product not found.")


    def delete_product(self,product_id):
        if product_id in self.product:
            del self.product[product_id]
        else:
            print("Product not found")


    def view_products(self):
        for product in self.product.values():
            print(product)

    def get_product(self,product_id):  # Product1.get_product("101")
        return self.product.get(product_id)
    

    def record_sale(self,product_id,quantity,price): # product_id (to identify the product has been sold) quantity  (how many units of products has been sold) price (the selling price per unit))
        product = self.get_product(product_id)
        if product:
            if product.quantity >= quantity: # Check if there is enough stock in inventory to fulfill the sale. It compares the current quantity of product with requested quantity for sale
                sale = Sale(len(self.sales) + 1, product_id,quantity,price)
                product.quantity -= quantity
                self.sales.append(sale)
                return sale
            else:
                print("Not enough quantity in stock")
        else:
            print("Product not found")


    def record_return(self,product_id,quantity,reason): # product_id to identify the product quantity the number of units returned reason the return for reason
        product = self.get_product(product_id)
        if product:
            return_obj = Return(len(self.returns)+1,product_id,quantity,reason)
            product.quantity += quantity
            self.returns.append(return_obj)
        else:
            print("Product not found...")


    def view_sales(self):
        for sale in self.sales:
            print(sale)

        
    def view_returns(self):
        for return_obj in self.returns:
            print(return_obj)


