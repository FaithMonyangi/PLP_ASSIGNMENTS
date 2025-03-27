def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        price = price - ((discount_percent/100) * price)
    else:
        return price
    
price = float(input("Enter the price of the item:"))
discount_percent = float(input("Enter the percentage discount:"))
    
print(price)