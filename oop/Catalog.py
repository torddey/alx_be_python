# class products:
#     def __init__(self, name, price, quantity):
#         self.name = name 
#         self.price = price 
#         self.quantity = quantity

#     def total_value(self): 
#         return self.price * self.quantity

#     def display_info(self):
#         print(f"Product name is: {self.name}")
#         print(f"Product price is: {self.price}")
#         print(f"Quantity in stock: {self.quantity}")
#         print(F"Total value is : {self.total_value}")



# product1 = products("T-shirt", 100, 10) 
# product1.total_value()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity in Stock: {self.quantity}")
        print(f"Total Value in Stock: ${self.total_value():.2f}")

product1 = Product("T-Shirt", 9.99, 10)
product1.display_info()

