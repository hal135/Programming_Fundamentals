products = input()
quantity = int(input())

def total_price(products, quantity):
    if products == "coffee":
        price = 1.50
    elif products == "water":
        price = 1.00
    elif products == "coke":
        price = 1.40
    elif products == "snacks":
        price = 2.00
    total_price = price * quantity
    return total_price

price = total_price(products, quantity)
print(f"{price:.2f}")

