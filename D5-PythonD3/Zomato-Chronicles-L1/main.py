import json

def load_orders_data():
    try:
        with open("orders.json", "r") as orders_file:
            return json.load(orders_file)
    except FileNotFoundError:
        return {}  # Return an empty orders dictionary if the file doesn't exist

def load_menu_data():
    try:
        with open("menu.json", "r") as menu_file:
            return json.load(menu_file)
    except FileNotFoundError:
        return {}  # Return an empty orders dictionary if the file doesn't exist


def save_data_to_json(menu, orders):
    try:
        # Save menu to menu.json
        with open("menu.json", "w") as menu_file:
            json.dump(menu, menu_file, indent=4)
    except Exception as e:
        print(f"Error saving menu data: {str(e)}")

    try:
        # Save orders to orders.json
        with open("orders.json", "w") as orders_file:
            json.dump(orders, orders_file, indent=4)
    except Exception as e:
        print(f"Error saving orders data: {str(e)}")

def add_dish(menu, dish_name, price, available=True):
    # Find the next available dish ID
    next_dish_id = max(int(key) for key in menu.keys()) + 1 if menu else 1
    menu[str(next_dish_id)] = {"dish_name": dish_name, "price": price, "available": available}
    return f"Dish '{dish_name}' (ID: {next_dish_id}) added successfully."

def update_dish_availability(menu, dish_id, available):
    if dish_id in menu:
        menu[dish_id]["available"] = available
        return f"Dish ID {dish_id} availability updated successfully."
    else:
        return f"No dish found with ID {dish_id}."

def view_all_orders(orders):
    if not orders:
        print("No orders yet.")
    else:
        print("All Orders:")
        for order_id, order in orders.items():
            print(f"Order ID: {order_id}, Customer Name: {order['customer_name']}")
            print("Dishes:")
            for dish in order["dishes"]:
                print(f"Dish ID: {dish['dish_id']}, Status: {dish['status']}")

def filter_orders_by_status(orders, status):
    filtered_orders = {}
    for order_id, order in orders.items():
        if any(dish["status"] == status for dish in order["dishes"]):
            filtered_orders[order_id] = order
    return filtered_orders

def update_order_status(orders):
    order_id = input("Enter Order ID to update status: ")
    if order_id in orders:
        order = orders[order_id]
        print("Current Order Status:")
        for i, dish in enumerate(order["dishes"]):
            print(f"{i + 1}. Dish ID: {dish['dish_id']}, Status: {dish['status']}")
        
        new_status = input("Enter the new status for the order: ")
        for dish in order["dishes"]:
            dish["status"] = new_status

        print(f"Order ID {order_id} status updated successfully.")
    else:
        print(f"No order found with ID {order_id}.")

def calculate_order_total(order, menu):
    total_price = sum(menu[dish["dish_id"]]["price"] for dish in order["dishes"])
    return total_price

def admin(menu, orders):
    while True:
        print("Select Your Choice")
        print("1. Add Dish")
        print("2. Update Dish Availability")
        print("3. Remove Dish")
        print("4. View Menu")
        print("5. Update Order Status")
        print("6. View All Orders")
        print("7. Filter Orders by Status")
        print("0. Back")
        print("8. Exit")

        admin_input = input("Enter Your Choice (1/2/3/4/5/6/7/8/0): ")

        if admin_input == "1":
            dish_name = input("Enter Dish Name: ")
            price = float(input("Enter Price: "))
            available = input("Is the dish available? (yes/no): ").lower() == "yes"
            print(add_dish(menu, dish_name, price, available))

        elif admin_input == "2":
            dish_id = input("Enter Dish ID to update availability: ")
            available = input("Is the dish available? (yes/no): ").lower() == "yes"
            print(update_dish_availability(menu, dish_id, available))

        elif admin_input == "3":
            dish_id = input("Enter Dish ID to remove: ")
            if dish_id in menu:
                del menu[dish_id]
                print(f"Dish ID {dish_id} removed successfully.")
            else:
                print(f"No dish found with ID {dish_id}.")

        elif admin_input == "4":
            # View Menu
            view_menu(menu)

        elif admin_input == "5":
            # Update Order Status
            update_order_status(orders)

        elif admin_input == "6":
            # View All Orders
            view_all_orders(orders)

        elif admin_input == "7":
            # Filter Orders by Status
            status = input("Enter Status to filter by: ")
            filtered_orders = filter_orders_by_status(orders, status)
            print(f"Orders with status '{status}':")
            for order_id, order in filtered_orders.items():
                print(f"Order ID: {order_id}, Customer Name: {order['customer_name']}")
        elif admin_input == "0":
            return
        elif admin_input == "8":
            print("Thank you for using our service.")
            save_data_to_json(menu, orders)  # Save data to JSON files before exiting
            exit()

        else:
            print("Invalid choice. Please try again.")

def view_menu(menu):
    if not menu:
        print("The menu is currently empty.")
    else:
        print("Available Menu:")
        for dish_id, details in menu.items():
            if details["available"]:
                print(f"Dish ID: {dish_id}, Dish Name: {details['dish_name']}, Price: ₹{details['price']}")

def customer(menu, orders):
    while True:
        print("Select Your Choice")
        print("1. Show Menu")
        print("2. Order Dish")
        print("3. See Status")
        print("4. Cancel Dish")
        print("5. Filter Orders by Status")
        print("6. Calculate Order Total")
        print("0. Back")
        print("7. Exit")

        customerInput = input("Enter Your Choice (1/2/3/4/5/6/7/8/0): ")

        if customerInput == "1":
            # Show Menu
            view_menu(menu)

        elif customerInput == "2":
            # Order Dish
            customer_name = input("Enter your name: ")
            dish_ids = input("Enter dish IDs (comma-separated): ").strip().split(',')
            order = {"customer_name": customer_name, "dishes": []}

            for dish_id in dish_ids:
            
                if dish_id in menu and menu[dish_id]["available"]:
                    order["dishes"].append({"dish_id": dish_id, "status": "received"})

            order_id = len(orders) + 1  # Generate a unique order ID
            orders[order_id] = order
            print("Order placed successfully! Your order ID is: ", order_id)

        elif customerInput == "3":
            # See Status
            order_id_str = input("Enter your order ID: ")  # Get order ID as a string
            order_id = order_id_str
            if order_id in orders:
                order = orders[order_id]
                print(f"Order Status for Order ID {order_id}:")
                for dish in order["dishes"]:
                    print(f"Dish ID: {dish['dish_id']}, Status: {dish['status']}")
            else:
                print("Order not found.")


        elif customerInput == "4":
            # Cancel Dish
            order_id = input("Enter your order ID: ")
            if order_id in orders:
                order = orders[order_id]
                print("Dishes in your order:")
                for i, dish in enumerate(order["dishes"]):
                    print(f"{i + 1}. Dish ID: {dish['dish_id']}, Status: {dish['status']}")

                dish_to_cancel = int(input("Enter the number of the dish to cancel: ")) - 1
                if 0 <= dish_to_cancel < len(order["dishes"]):
                    dish_id_to_cancel = order["dishes"][dish_to_cancel]["dish_id"]
                    for dish in order["dishes"]:
                        if dish["dish_id"] == str(dish_id_to_cancel):
                            dish["status"] = "canceled"
                            print("Dish canceled successfully!")
                else:
                    print("Invalid selection.")

        elif customerInput == "5":
            # Filter Orders by Status
            status = input("Enter Status to filter by: ")
            filtered_orders = filter_orders_by_status(orders, status)
            print(f"Orders with status '{status}':")
            for order_id, order in filtered_orders.items():
                print(f"Order ID: {order_id}, Customer Name: {order['customer_name']}")

        elif customerInput == "6":
            # Calculate Order Total
            order_id = input("Enter your order ID: ")
            if order_id in orders:
                order = orders[order_id]
                total_price = calculate_order_total(order, menu)
                print(f"Total Price for Order ID {order_id}: ₹{total_price}")
            else:
                print("Order not found.")
        
        # elif customerInput == "7":
        #     # View All Orders
        #     view_all_orders(orders)
        
        elif customerInput == "0":
            return
        
        elif customerInput == "7":
            print("Thank you for using our service")
            save_data_to_json(menu, orders)  # Save data to JSON files before exiting
            exit()

        else:
            print("Invalid choice, Try again.")

def main():
    # Load menu from menu.json
    menu = load_menu_data()
    
    
    # Load orders from orders.json
    orders = load_orders_data()

    while True:
        print("Select Your Choice")
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")

        choice = input("Enter Your Choice (1/2/3): ")

        if choice == "1":
            admin(menu, orders)
        elif choice == "2":
            customer(menu, orders)
        elif choice == "3":
            print("Thank you for using our service")
            save_data_to_json(menu, orders)  # Save data to JSON files before exiting
            break
        else:
            print("Invalid choice, Try again.")

if __name__ == "__main__":
    main()
