def add_item(cart):
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: "))
    cart[item_name] = item_price
    print(f"{item_name} added to the cart.\n")

def view_cart(cart):
    if not cart:
        print("The cart is empty.\n")
    else:
        print("Cart items:")
        for item_name, item_price in cart.items():
            print(f"{item_name}: {item_price}")
        print()

def calculate_total(cart):
    total_price = sum(cart.values())
    print(f"The total price is: {total_price}\n")

def shopping_cart():
    cart = {}
    while True:
        print("Shopping Cart Menu:")
        print("1. Add item")
        print("2. View cart")
        print("3. Calculate total price")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_item(cart)
        elif choice == '2':
            view_cart(cart)
        elif choice == '3':
            calculate_total(cart)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

# Run the shopping cart program
shopping_cart()
