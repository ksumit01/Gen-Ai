from flask import Blueprint, render_template, request, redirect, url_for
from app.routes.utils import load_menu_data, load_orders_data, save_data_to_json

customer_bp = Blueprint('customer', __name__, url_prefix='/customer')

# Route to display the customer dashboard and menu
@customer_bp.route('/')
def customer_dashboard():
    # Load menu data
    menu = load_menu_data()
    
    return render_template('customer/customer_dashboard.html', menu=menu)

# Route to place a new order
@customer_bp.route('/place_order', methods=['GET', 'POST'])
def place_order():
    if request.method == 'POST':
        customer_name = request.form.get('customer_name')
        dish_ids = request.form.getlist('dish_ids')
        
        # Load menu and orders data
        menu = load_menu_data()
        orders = load_orders_data()
        
        # Create a new order and add it to the orders data
        order = {'customer_name': customer_name, 'dishes': []}
        for dish_id in dish_ids:
            if dish_id in menu and menu[dish_id]['available']:
                order['dishes'].append({'dish_id': dish_id, 'status': 'received'})
        
        if order['dishes']:
            order_id = str(len(orders) + 1)
            orders[order_id] = order
            save_data_to_json(menu, orders)
            
            return f"Order placed successfully! Your order ID is: {order_id}"
        else:
            return "Invalid dish selection. Please try again."
    
    # Load menu data for displaying the menu
    menu = load_menu_data()
    
    return render_template('customer/place_order.html', menu=menu)

# Add more routes for viewing orders, updating order status, and other customer functionalities
