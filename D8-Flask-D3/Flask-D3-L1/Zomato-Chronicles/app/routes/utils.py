import json

def load_orders_data():
    try:
        with open("orders.json", "r") as orders_file:
            return json.load(orders_file)
    except FileNotFoundError:
        return {}

def load_menu_data():
    try:
        with open("menu.json", "r") as menu_file:
            return json.load(menu_file)
    except FileNotFoundError:
        return {}

def save_data_to_json(menu, orders):
    try:
        with open("menu.json", "w") as menu_file:
            json.dump(menu, menu_file, indent=4)
    except Exception as e:
        print(f"Error saving menu data: {str(e)}")

    try:
        with open("orders.json", "w") as orders_file:
            json.dump(orders, orders_file, indent=4)
    except Exception as e:
        print(f"Error saving orders data: {str(e)}")
