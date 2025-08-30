# Create a tuple named product containing the following items: 
# "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple.
# Access and print the second element of the tuple product.
# Slice and print the last two elements of the product tuple.
# Check whether "Electronics" is present in the product tuple and print a message.
# Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). 
# Count how many times 1000 appears.
# Find and print the maximum and minimum price from the prices tuple.
# Use a loop to print each item from the product tuple on a new line.
# Convert the product tuple to a list. Change the price to 55000, 
# then convert it back to a tuple. Print the updated tuple.
# Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
# Remove "Electronics" from the product tuple 
# (by converting to list, removing, and converting back).
# Unpack the tuple product into three variables and print each variable.
#Create a nested tuple that contains three product tuples inside it. 
# Access and print the name of the second product in the nested tuple.

product_tuple = ("Laptop", 50000, "Black", 'Samsung', "Electronics")
print("Product Tuple:", product_tuple)

#printing second element
print("Second element of product tuple:", product_tuple[1])

#printing last two elements
print("Last two elements of the product list", product_tuple[-2:])

#check ELectronics in the tuple
if "Electronics" in product_tuple:
    print("Electronics is present in the product tuple")

#Procuct prices tuple
Procuct_prices = (1000, 1500, 1200, 1100, 900)
count = Procuct_prices.count(1000) # count of 1000
print("Count of 1000 in the prices tuple:", count)

#print max and min price
print("Max price:", max(Procuct_prices)) # maximum price
print("Min price:", min(Procuct_prices)) # minimum price

#iterating through tuple
for item in product_tuple:
    print(f"Item:{product_tuple.index(item)}", item)

#COnvert to list and modify
product_list = list(product_tuple) # convert to list
product_list[1] = 55000 # change price
Updatedproduct_tuple = tuple(product_list) # convert back to tuple
print("Updated Product Tuple:", Updatedproduct_tuple)
#Add new item by concatenation
stock = ("In Stock",)   
Updatedproduct_tuple = Updatedproduct_tuple + stock # add new item
print("Product Tuple after adding In Stock:", Updatedproduct_tuple)

#Remove Electronics
Newproduct_list = list(Updatedproduct_tuple) # convert to list
Newproduct_list.remove("Electronics") # remove Electronics
newProductTuple = tuple(Newproduct_list) # convert back to tuple
print("Product Tuple after removing Electronics:", newProductTuple)

#unpack
name, price, *rest = newProductTuple
print("Unpacked values:")
print("Name:", name)
print("Price:", price)
print("Rest:", rest)

#nested tuple\
product1 = ("Laptop", 50000, "Black", 'Samsung', "Electronics")
product2 = ("Smartphone", 20000, "White", 'Apple', "Electronics")
product3 = ("Tablet", 15000, "Gray", 'Lenovo', "Electronics")
nested_tuple = (product1, product2, product3)
print("Nested Tuple:", nested_tuple)
print("Name of the second product in the nested tuple:", nested_tuple[1][0])