from flask import Flask, render_template, request, redirect, url_for,flash
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy

# from wtforms import StringField, 
from wtforms import StringField, DecimalField, TextAreaField, BooleanField, IntegerField,SubmitField
# from flask_flash import Flash
from wtforms.validators import DataRequired
from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/GA201_Zomato'
db = SQLAlchemy(app)
# db.init_app(app)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

#create model

class Menu(db.Model):
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Make item_id the primary key
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))
    price = db.Column(db.Float)
    availability = db.Column(db.Boolean)

    def __init__(self, name, description, price, availability):
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability


#create a form class
class ItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired()])
    availability = BooleanField('Availability')
    submit = SubmitField('Submit')



# Create the UpdateForm class
class UpdateForm(FlaskForm):
    menu_id = IntegerField('Menu ID', validators=[DataRequired()])
    # Add additional fields for the details you want to update (e.g., name, description, price, availability)
    name = StringField('New Item Name')
    description = TextAreaField('New Description')
    price = DecimalField('New Price')
    availability = BooleanField('New Availability')
    submit = SubmitField('Update')


# Create the DeleteForm class
class DeleteForm(FlaskForm):
    menu_id = IntegerField('Menu ID', validators=[DataRequired()])
    submit = SubmitField('Delete')

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', user_name=name)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

app.errorhandler(500)
def page_not_found(e):
  return render_template('500.html'), 500
'''
# @app.route('/menu', methods=['GET', 'POST'])
# def addItem():
    form = ItemForm()
    item = None
    if form.validate_on_submit():
        # Retrieve data from the form
        item_id = form.item_id.data
        item = Menu.query.filter_by(name=form.name.data).first()
        if item is None:
            item = Menu(item_id, form.name.data, form.description.data, form.price.data, form.availability.data)
            db.session.add(item)
            db.session.commit()
        item = form.name.data
        form.name.data = ''
        form.description.data = ''
        form.price.data = ''
        form.availability.data = False


        # You can perform further processing or database operations here with the form data

        # flash(f'Item added: {name}', 'success')  # Flash a success message
        flash("Item added successfully", 'success')
        # return redirect(url_for('home'))
    item_inventory = Menu.query.order_by(Menu.item_id).all()
    return render_template('menuItem.html', form=form, item=item, item_inventory=item_inventory)

'''
@app.route('/menu', methods=['GET', 'POST'])
def addItem():
    form = ItemForm()
    item_inventory = Menu.query.order_by(Menu.item_id).all()

    if form.validate_on_submit():
        # Retrieve data from the form
        name = form.name.data

        # Check if an item with the same name already exists
        existing_item = Menu.query.filter_by(name=name).first()

        if existing_item:
            flash("Item with the same name already exists", 'danger')
        else:
            description = form.description.data
            price = form.price.data
            availability = form.availability.data

            # Create a new menu item
            new_item = Menu(name=name, description=description, price=price, availability=availability)
            db.session.add(new_item)
            db.session.commit()

            # Clear the form input fields
            form.name.data = ''
            form.description.data = ''
            form.price.data = ''
            form.availability.data = False

            # Flash a success message
            flash("Item added successfully", 'success')
    
    return render_template('menuItem.html', form=form, item_inventory=item_inventory)

@app.route('/update_item', methods=['GET', 'POST'])
def updateItem():
    form = UpdateForm()
    if form.validate_on_submit():
        menu_id = form.menu_id.data
        # Retrieve the menu item based on the menu_id
        # Update the menu item details with the values from the form fields (name, description, price, availability)
        # Save the updated menu item to the database or perform other necessary actions
        # flash(f'Menu item with ID {menu_id} updated successfully', 'success')
        return redirect(url_for('home'))
    return render_template('updateItem.html', form=form)

@app.route('/delete_item', methods=['GET','POST'])
def deleteItem():
    form = DeleteForm()
    if form.validate_on_submit():
        menu_id = form.menu_id.data
        # Find and delete the menu item based on the menu_id
        # Perform any additional cleanup or database operations
        # flash(f'Menu item with ID {menu_id} deleted successfully', 'success')
        return redirect(url_for('home'))
    return render_template('deleteItem.html', form=form)

if __name__ == '__main__':
  app.run(debug=True)