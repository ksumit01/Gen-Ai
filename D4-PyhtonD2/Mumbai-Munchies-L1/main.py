from prettytable import PrettyTable
import saleRecord

import datetime


#Function For Adding The Snacks
def add_snack(snack_inventory):
    try:
        print("\n=== Add Snack to Inventory ===")
        
        # Get snack details from user
        snack_name = input("Enter Snack Name You Want To Add: ")
        price = float(input("Enter the Price of the Snack: "))
        quantity = int(input("Enter Total Quantity of the Snacks: "))

        # Check if a snack with the same name already exists
        for snack_id, snack in snack_inventory.items():
            if snack["name"] == snack_name:
                # Snack with the same name found, update quantity
                snack["quantity"] += quantity
                print("\nSnack already exists. Updated quantity.")
                # print(f"Snack already exists. Updated quantity.: {snack['quantity']}")
                break
        else:
            # If the loop didn't break, it means the snack doesn't exist, so add it.
            # Generate a unique ID for the new snack
            new_id = len(snack_inventory) + 1

            # Create a new snack entry in the inventory
            new_snack = {
                "name": snack_name,
                "price": price,
                "available": True,
                "quantity": quantity
            }

            # Add the new snack to the inventory with the unique ID
            snack_inventory[new_id] = new_snack
            print("\nSnack added successfully!")

        print("\nUpdated Inventory:")
        
        # Print the updated inventory with better formatting
        for snack_id, snack in snack_inventory.items():
            print(f"ID: {snack_id}")
            print(f"Name: {snack['name']}")
            print(f"Price: ₹{snack['price']:.2f}")
            print(f"Quantity: {snack['quantity']}")
            print(f"Available: {'Yes' if snack['available'] else 'No'}")
            print('-' * 30)

    except ValueError:
        print("\nInvalid input. Please enter a valid price and quantity as numbers.")



#Function For Deleting the Snack From The Inventory
def remove_snack(snack_id,snack_inventory):
    try:
        snack_id = int(snack_id)  # Convert input to integer
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


#Function for updating the Snack

def update_snack(snack_id, snack_inventory):
    # Check if the snack_id exists in the inventory
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



#Function For View Inventory Using PrettyTable

from prettytable import PrettyTable

def view_inventory(snack_inventory):
    if not snack_inventory:
        print("Inventory is empty.")
        return

    table = PrettyTable()
    table.field_names = ["ID", "Name", "Price", "Quantity"]

    for snack_id, snack_info in snack_inventory.items():
        table.add_row([snack_id, snack_info["name"], snack_info["price"], snack_info["quantity"]])

    print(table)




#Main Runner Function
def mainFunction():
    snack_inventory = {}  # Create an empty dictionary to store snack inventory
    
    while True:
        print("\n*** Snack Inventory Management ***")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Snack")
        print("4. View Snack Inventory")
        print("5. Make Sell ")
        print("6. View Sale Records")
        print("7. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == "1":
            add_snack(snack_inventory)
        elif choice == "2":
            snack_id_to_remove = input("Enter the ID of the snack to remove: ")
            remove_snack(snack_id_to_remove,snack_inventory)
        elif choice == "3":
            snack_id_to_update = int(input("Enter the ID of the snack to update: "))
            update_snack(snack_id_to_update, snack_inventory)
        # In your main function
        elif choice == "4":
             view_inventory(snack_inventory)
        elif choice == "5":
              saleRecord.make_sale(snack_inventory)
        elif choice == "6":
              saleRecord.view_sales_records()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")



# Call the main function to start the program
if __name__ == "__main__":
    mainFunction()



