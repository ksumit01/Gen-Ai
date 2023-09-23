from flask import Blueprint, render_template, request, redirect, url_for
# from utils import load_menu_data, load_orders_data, save_data_to_json
from utils import load_menu_data, load_orders_data, save_data_to_json


admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Route to display the admin dashboard
@admin_bp.route('/')
def admin_dashboard():
    # Load menu and orders data
    menu = load_menu_data()
    orders = load_orders_data()
    
    return render_template('admin/admin_dashboard.html', menu=menu, orders=orders)

# Route to add a new dish to the menu
@admin_bp.route('/add_dish', methods=['GET', 'POST'])
def add_dish():
    if request.method == 'POST':
        dish_name = request.form.get('dish_name')
        price = float(request.form.get('price'))
        available = request.form.get('available') == 'on'
        
        # Load menu data, add the new dish, and save it back to the JSON file
        menu = load_menu_data()
        dish_id = str(len(menu) + 1)
        menu[dish_id] = {'dish_name': dish_name, 'price': price, 'available': available}
        save_data_to_json(menu, load_orders_data())
        
        return redirect(url_for('admin.admin_dashboard'))
    
    return render_template('admin/manage_menu.html')

# Add more routes for updating, removing dishes, and managing orders as needed


