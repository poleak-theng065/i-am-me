products = [
    {"name": "Apple", "price": 1.50, "quantity": 100, "expired": True},
    {"name": "Banana", "price": 0.75, "quantity": 50, "expired": False},
    {"name": "Orange", "price": 1.25, "quantity": 80, "expired": True}
    ]
total = 0
for i in range(len(products)):
    if products[i]["expired"]== True:
        total += 1
print(total)