"""
Scenario:
 
You are building the backend logic of a product and order management system for an e-commerce platform like Amazon or Flipkart. The system needs to handle products, users, payments, discounts, and different order behaviors dynamically.
 
Q1. Product Search System (Static Polymorphism)
 
Problem Statement:

Implement a class ProductSearch that allows searching products with different combinations of criteria (name, category, price range).
 
Requirements:
 
Use default arguments and/or *args, **kwargs to simulate method overloading.
 
Allow the following types of searches:
 
Only by name
 
Name and category
 
Name, category, and price range
 
 
Q2. Cart System with Quantity Variations (Static Polymorphism)
 
Problem Statement:

Design a class Cart that can add multiple products with variable quantities using *args or **kwargs.
 
Requirements:
 
Add multiple products at once with name and quantity
 
Simulate static polymorphism using variable arguments
 
 
Q3. Discount Application (Static Polymorphism)
 
Problem Statement:

Create a class Discount that allows applying different types of discounts:
 
Flat discount
 
Percentage discount
 
Buy One Get One
 
Use static polymorphism to overload the method using default parameters or *args
 
 
Q4. Payment System (Dynamic Polymorphism)
 
Problem Statement:

Implement a base class Payment and subclasses CreditCardPayment, UPIPayment, and CODPayment. Each should override a method pay().
 
Requirements:
 
Override pay() method in each class to simulate different payment methods
 
"""

# Q1. Product Search System (Static Polymorphism)

productlist = [
{
        "Name" : "Laptop",
        "Category" : "Electronic",
        "Price" : 50000
},
{
        "Name" : "Bicycle",
        "Category" : "Vehicle",
        "Price" : 3000
},
{
        "Name" : "Table",
        "Category" : "Home",
        "Price" : 10000
},
]

class ProductSearch:
    def search(self, name = None, category = None, price = None):
        found = False
        for product in productlist:
            if name is not None and category is not None and price is not None:
                if (product["Name"] == name and product["Category"] == category and product["Price"] == price):
                    found = True
                    break
            elif name is not None and category is not None:
                 if (product["Name"] == name and product["Category"] == category):
                    found = True
                    break
            elif name is not None:
                 if (product["Name"] == name):
                    found = True
                    break
        if found:
            print(f"Product : {product['Name']} Category : {product['Category']} Price : {product['Price']}")
        else:
            print(f"Product Not found")

psearch =  ProductSearch()
psearch.search("Table")
psearch.search("Bicycle",  "Vehicle")
psearch.search("Laptop",  "Electronic", 50000)
psearch.search("X")

# Q2. Cart System with Quantity Variations (Static Polymorphism)
print("#################################################")

class Cart:
    cartlist = []
    def addcart(self, *products):
        for item in products:
            self.cartlist.append({"Name" : item[0], "Quantity" : item[1]})
    def __repr__(self):
        return f"Cart list \n{self.cartlist}"

cart = Cart()
cart.addcart(("Laptop", 40), ("Table", 10))
cart.addcart(("Bicycle", 20))
print(cart)

# Q3. Discount Application (Static Polymorphism)
print("#################################################")
class Discount:
    def ApplyDiscount(self, *dicountTypes):
        if len(dicountTypes) > 1:
            if dicountTypes[0] is not None and dicountTypes[1] is not None:
                if str(dicountTypes[0]).__contains__("Percentage"):
                    print(f"Discount Type : {dicountTypes[0]} Percentage : {dicountTypes[1]}%")
                else:
                    print(f"Discount Type : {dicountTypes[0]} Amount : Rs {dicountTypes[1]}")
        elif len(dicountTypes) > 0:
                print(f"Discount Type : {dicountTypes[0]}")
        else:
            print(f"No discount provided")

dicount = Discount()
dicount.ApplyDiscount("Flat Discount" , 200)
dicount.ApplyDiscount("Percentage Discount" , 20)
dicount.ApplyDiscount("Buy one Get One")
dicount.ApplyDiscount()

#Q4. Payment System (Dynamic Polymorphism)
print("#################################################")

class Payment:
    def pay(self):
        print("Base class payement")

class CreditCardPayment(Payment):
    def pay(self):
        print("Credit Card Payment")

class UPIPayment(Payment):
    def pay(self):
        print("UPI Payment")

class CODPayment(Payment):
    def pay(self):
        print("COD Payment")

payment = Payment()
payment.pay()
payment = CreditCardPayment()
payment.pay()
payment = UPIPayment()
payment.pay()
payment = CODPayment()
payment.pay()