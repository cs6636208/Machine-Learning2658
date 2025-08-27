import numpy as np

products = ["mouse", "keyboard", "monitor"]

sales_data = [
    [5, 7, 6],
    [3, 2, 4],
    [2, 1, 3]
]

sales_dict = {}
for i in range(len(products)):
    sales_dict[products[i]] = sales_data[i]

print(sales_dict)
print()

total_sales = []
for i in range(len(products)):
    total = sum(sales_data[i])
    print(f"{products[i]} ยอดขายรวมทั้งหมด: {total}")
    total_sales.append(total)
    # total_sales[products[i]] = total

print(total_sales)
print()

max_sales = 0
best_product = ""

for i in range(len(products)):
    total = sum(sales_data[i])
    if total > max_sales:
        max_sales = total
        best_product = products[i]

print(f"สินค้าที่มียอดขายรวมมากที่สุดคือ: {best_product} ({max_sales} ชิ้น)")

