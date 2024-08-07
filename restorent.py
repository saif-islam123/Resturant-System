menu = {
    'Pizza': 50,
    'Pasta': 60,
    'Burger': 70,
    'Salad': 80,
    'Coffee': 90,
    'Sandwich': 100,
    'Juice': 120,
    'Tea': 40,
    'Cake': 150,
    'Fries': 35,
    'Soda': 45,
    'Ice Cream': 110,
    'Steak': 200,
    'Soup': 65,
    'Milkshake': 95,
    'Smoothie': 130,
    'Waffles': 150
}
print('Welcome to PYTHON Restaurant')
print('Here is the items list:')
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

# Function to handle item orders
def order_item(order_total):
    item = input("Enter the item you want to order: ").capitalize()
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print("This item is not available yet.")
    return order_total

# Handle first item order
order_total = order_item(order_total)

# Ask if user wants to add another item
while True:
    another_order = input("Do you want to add another item? (Yes/No): ").strip().capitalize()
    if another_order == 'Yes':
        order_total = order_item(order_total)
    else:
        break

print(f"The total amount to pay is Rs {order_total}.")
