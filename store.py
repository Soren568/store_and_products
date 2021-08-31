# import products
# prod = products.Product
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += self.price*percent_change
        else:
            self.price -= self.price*percent_change

    def print_info(self):
        print(f"Product name: {self.name} || Price: ${self.price} || Category: {self.category}")

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        self.products.remove(self.products[id])

    def inflation(self, percent_increase):
        for i in self.products:
            self.products[i] = Product.update_price(self.products[i], percent_change=percent_increase, is_increased=True)

# Creating an instance of the store
store = Store("SevenEleven")
# Adding products to the store
store.add_product(Product("RedBull", "2", "Drinks"))
store.add_product(Product("Corn", "8", "Canned"))
store.add_product(Product("Beer", "12", "Drinks"))
store.add_product(Product("Beans", "2", "Canned"))
store.add_product(Product("Chili", "5", "Canned"))
store.add_product(Product("Nuts", "5", "Snacks"))
store.add_product(Product("Chips", "3", "Snacks"))
store.add_product(Product("Pretzels", "4", "Snacks"))

# Selling a product - should remove corn 
store.sell_product(1)

for i in store.products:
    Product.print_info(i)

# ! EXTRAS 
# Inflation - 10% increase
store.inflation(.10)




