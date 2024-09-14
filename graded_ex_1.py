
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_categories():
    print("Available Categories:")
    categories = list(products.keys())
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    try:
        category_index = int(input("Select a category by entering the number: ")) - 1
        if 0 <= category_index < len(categories):
            return category_index
        else:
            print("Invalid category number. Please try again.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def display_products(products_list):
    print("Available Products:")
    for i, (product, price) in enumerate(products_list, 1):
        print(f"{i}. {product} - ${price}")

def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        sorted_list = sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        sorted_list = sorted(products_list, key=lambda x: x[1], reverse=True)
    else:
        return products_list
    return sorted_list

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    print("\nYour Shopping Cart:")
    for product, price, quantity in cart:
        cost = price * quantity
        total_cost += cost
        print(f"{product} - ${price} x {quantity} = ${cost}")
    print(f"Total cost: ${total_cost}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print("\n----- Receipt -----")
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("\nItems Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")

def validate_name(name):
    parts = name.split()
    if len(parts) == 2 and all(part.isalpha() for part in parts):
        return True
    return False

def validate_email(email):
    return "@" in email

def main():
    cart = []
    name = input("Enter your name (First Last): ")
    while not validate_name(name):
        print("Invalid name. Please enter your first and last name using alphabets only.")
        name = input("Enter your name (First Last): ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address with '@'.")
        email = input("Enter your email address: ")

    while True:
        category_index = display_categories()
        if category_index is not None:
            categories = list(products.keys())
            category_name = categories[category_index]
            product_list = products[category_name]
            while True:
                display_products(product_list)
                print("\nOptions:")
                print("1. Select a product to buy")
                print("2. Sort the products by price")
                print("3. Go back to category selection")
                print("4. Finish shopping")
                option = input("Choose an option: ")

                if option == '1':
                    product_choice = input("Enter the product number to buy: ")
                    try:
                        product_index = int(product_choice) - 1
                        if 0 <= product_index < len(product_list):
                            quantity = input(f"Enter the quantity of {product_list[product_index][0]}: ")
                            if quantity.isdigit() and int(quantity) > 0:
                                add_to_cart(cart, product_list[product_index], int(quantity))
                            else:
                                print("Invalid quantity. Please enter a positive number.")
                        else:
                            print("Invalid product number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                elif option == '2':
                    sort_order = input("Sort by price: ascending (1) or descending (2): ")
                    if sort_order == '1':
                        sorted_list = display_sorted_products(product_list, "asc")
                    elif sort_order == '2':
                        sorted_list = display_sorted_products(product_list, "desc")
                    else:
                        print("Invalid option.")
                        continue
                    display_products(sorted_list)

                elif option == '3':
                    break

                elif option == '4':
                    if cart:
                        total_cost = display_cart(cart)
                        address = input("Enter the delivery address: ")
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    return  

                else:
                    print("Invalid option. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
