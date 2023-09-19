from prettytable import PrettyTable
from cashier import Cashier


class Admin:
    def __init__(self, canteen_staff, cashier):
        self.role_name = "Admin"
        self.canteen_staff = canteen_staff
        self.cashier = cashier
    
    cashier_instance = Cashier()

    def add_snack(self, snack_inventory):
      try:
          print("\n=== Add Snack to Inventory ===")
          
          # Get snack details from the user
          snack_name = input("Enter Snack Name You Want To Add: ")
          price = float(input("Enter the Price of the Snack: "))
          quantity = int(input("Enter Total Quantity of the Snacks: "))
          category = input("Enter the Category of the Snack: ")  # Prompt for category

          # Check if a snack with the same name and category already exists
          for snack_id, snack in snack_inventory.items():
              if snack["name"] == snack_name and snack["category"] == category:
                  # Snack with the same name and category found, update quantity
                  snack["quantity"] += quantity
                  print("\nSnack already exists. Updated quantity.")
                  break
          else:
              # If the loop didn't break, it means the snack doesn't exist, so add it.
              
              # Generate a unique ID for the new snack
              new_id = 1  # Start with an initial ID of 1

              # Find the maximum existing ID and add 1 to it
              existing_ids = [int(id) for id in snack_inventory.keys()]  # Convert to integers
              if existing_ids:
                  new_id = max(existing_ids) + 1

              # Create a new snack entry in the inventory with category
              new_snack = {
                  "name": snack_name,
                  "price": price,
                  "available": True,
                  "quantity": quantity,
                  "category": category  # Include the category field
              }

              # Add the new snack to the inventory with the unique ID
              snack_inventory[new_id] = new_snack
              print("\nSnack added successfully!")

          print("\nSnacks added successfully!")

      except ValueError:
          print("\nInvalid input. Please enter a valid price and quantity as numbers.")

    def remove_snack(self, snack_id, snack_inventory):
        try:
            # snack_id = int(snack_id)  # Convert input to integer
            # Check if the provided snack_id exists in the inventory
            if snack_id in snack_inventory:
                snack_to_remove = snack_inventory[snack_id]
                print("\nSnack Details:")
                print(f"Name: {snack_to_remove['name']}")
                print(f"Price: ₹{snack_to_remove['price']:.2f}")
                print(f"Quantity: {snack_to_remove['quantity']}")
                print(f"Available: {'Yes' if snack_to_remove['available'] else 'No'}")

                # Ask for confirmation
                confirmation = input("Are you sure you want to delete this snack? (yes/no): ").strip().lower()

                if confirmation == 'yes':
                    # Remove the snack with the provided ID
                    removed_snack = snack_inventory.pop(snack_id)
                    print("\nSnack removed successfully!")
                    print(f"Removed Snack Details:")
                    print(f"Name: {removed_snack['name']}")
                    print(f"Price: ₹{removed_snack['price']:.2f}")
                    print(f"Quantity: {removed_snack['quantity']}")
                    print(f"Available: {'No' if removed_snack['available'] else 'Yes'}")
                else:
                    print("Snack not deleted.")
            else:
                print("\nSnack not found in the inventory. Please check the ID and try again.")
        except ValueError:
            print("\nInvalid input. Please enter a valid ID as a number.")

    def update_snack(self, snack_id, snack_inventory):
        # Check if the snack_id exists in the inventory
        # snack_id = int(snack_id)
        if snack_id not in snack_inventory:
            print(f"Snack with ID {snack_id} does not exist in the inventory.")
            return

        while True:
            try:
                print(f"Snack ID: {snack_id}")
                print("What do you want to update?")
                print("1. Price")
                print("2. Quantity")
                print("3. Name")
                print("4. Done")
                
                choice = input("Enter your choice (1/2/3/4): ")

                if choice == "1":
                    new_price = float(input("Enter the new price: "))
                    snack_inventory[snack_id]["price"] = new_price
                elif choice == "2":
                    new_quantity = int(input("Enter the new quantity: "))
                    snack_inventory[snack_id]["quantity"] = new_quantity
                elif choice == "3":
                    new_name = input("Enter the new name: ")
                    snack_inventory[snack_id]["name"] = new_name
                elif choice == "4":
                    print("Update complete.")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid input.")

    def check_stock_levels(self, snack_inventory):
        # Delegate the check_stock_levels method to CanteenStaff
        self.canteen_staff.check_stock_levels(snack_inventory)

    def view_sales_records(self):
        # Delegate the view_sales_records method to Cashier
        self.cashier.view_sales_records()



