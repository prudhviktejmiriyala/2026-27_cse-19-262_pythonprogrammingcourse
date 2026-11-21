def shopping_cart(**products):
    total = 0

    print("Items in Shopping Cart:")
    for item, price in products.items():
        print(f"{item}: ₹{price}")
        total += price

    print(f"\nTotal Amount: ₹{total}")
shopping_cart(apple=15, orange=12, mango=10)