# Define a data structure for sales records
from prettytable import PrettyTable
import datetime

sales_records = []

# Function to handle sales
def make_sale(snack_inventory):
    # Prompt staff for snack ID and quantity sold
    try:
        snack_id = int(input("Enter the snack's ID: "))
        
        if snack_id not in snack_inventory:
            print("Snack not found in inventory.")
            return
        
        available_quantity = snack_inventory[snack_id]["quantity"]
        
        while True:
            quantity_sold = int(input(f"Enter the quantity sold (Available: {available_quantity} units): "))
            if quantity_sold <= available_quantity:
                break
            else:
                print(f"Error: Quantity sold cannot exceed available quantity ({available_quantity} units).")
        
        # Calculate total amount received
        price_per_unit = snack_inventory[snack_id]["price"]
        total_amount = price_per_unit * quantity_sold
        
        # Update inventory
        snack_inventory[snack_id]["quantity"] -= quantity_sold
        
        # Create a sales record and add it to the sales_records list
        sales_record = {
            "date_time": datetime.datetime.now(),  
            "snack_id": snack_id,
            "quantity_sold": quantity_sold,
            "total_amount": total_amount
        }
        sales_records.append(sales_record)
        
        print(f"Sale complete. Total amount received: ${total_amount}")
    
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")




# Function to display sales records
from prettytable import PrettyTable

def view_sales_records():
    if not sales_records:
        print("No sales records available.")
    else:
        table = PrettyTable()

        # Define the column names based on the keys in the dictionaries
        table.field_names = ["Date/Time", "Snack Id", "Quantity Sold", "Total Amount"]

        # Initialize a variable to store the grand total
        grand_total = 0

        # Add rows from the list of dictionaries and calculate the grand total
        for record in sales_records:
            table.add_row([record["date_time"], record["snack_id"], record["quantity_sold"], record["total_amount"]])
            grand_total += record["total_amount"]

        # Print the table
        print(table)

        # Print the grand total
        print(f"Grand Total: ${grand_total}")




