from prettytable import PrettyTable 
class CanteenStaff:
    def __init__(self):
        self.role_name = "Canteen Staff"

    def mark_snack_out_of_stock(self, snack_inventory):
        try:
            snack_id = int(input("Enter the snack's ID to mark as out of stock: "))
            
            if snack_id not in snack_inventory:
                print("Snack not found in inventory.")
                return
            
            snack_inventory[snack_id]["available"] = False
            print("Snack marked as out of stock.")
        
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
    
    def check_stock_levels(self, snack_inventory):
      table = PrettyTable()
      # Define the column names based on the keys in the dictionaries
      table.field_names = ["ID", "Name", "Quantity"]

      for snack_id, snack in snack_inventory.items():
          table.add_row([snack_id, snack['name'], snack['quantity']])

      # Print the table
      print(table)

    
    def view_snack_details(self, snack_inventory):
      try:
          snack_id = int(input("Enter the snack's ID to view details: "))
          
          if snack_id not in snack_inventory:
              print("Snack not found in inventory.")
              return
          
          snack = snack_inventory[snack_id]
          table = PrettyTable()
          table.field_names = ["Item", "Value"]
          table.add_row(["Name", snack['name']])
          table.add_row(["Price", f"₹{snack['price']:.2f}"])
          table.add_row(["Quantity", snack['quantity']])
          table.add_row(["Available", 'Yes' if snack['available'] else 'No'])
          # Add a description field if available in your inventory data structure
          if 'description' in snack:
              table.add_row(["Description", snack['description']])
          
          # Print the table
          print(table)
      
      except ValueError:
          print("Error: Invalid input. Please enter a valid number.")

