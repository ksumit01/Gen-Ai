from admin import Admin
from canteen_staff import CanteenStaff
from cashier import Cashier
# from main import  display_menu
from prettytable import PrettyTable
from pyfiglet import figlet_format 
from bulkHandler import BulkHandler
import os

import json

def load_snack_inventory_from_file():
    try:
        with open("snack_inventory.json", "r") as file:
            # Attempt to load data from the file
            snack_inventory = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        # If the file doesn't exist or is empty, initialize an empty dictionary
        snack_inventory = {}
    return snack_inventory


def save_snack_inventory_to_file(snack_inventory):
    with open("snack_inventory.json", "w") as file:
        json.dump(snack_inventory, file, indent=4)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art(text):
    banner = figlet_format(text, font="slant")
    print(banner)
bulkHandler = BulkHandler()
def main():
    # snack_inventory = {}  # Create an empty dictionary to store snack inventory 
    
    canteen_staff = CanteenStaff()  # Create an instance of the CanteenStaff class
    cashier = Cashier()  # Create an instance of the Cashier class
    admin = Admin(canteen_staff, cashier)# Create an instance of the Admin class
    snack_inventory = load_snack_inventory_from_file()

    while True:
        clear_screen()  # Clear the screen before displaying the menu

        # Print an ASCII art header
        print_ascii_art("Mumbai Munchies Canteen")
        print("*********************************************")

        # Display the menu options
        print("\n*** Snack Inventory Management ***")
        print("1. Admin")
        print("2. Canteen Staff")
        print("3. Cashier")
        print("4. Exit")

        role_choice = input("Enter your role (1/2/3/4): ")

        if role_choice == "1":
            # Admin role
            admin_menu(admin, snack_inventory)
            save_snack_inventory_to_file(snack_inventory)
        elif role_choice == "2":
            # Canteen Staff role
            canteen_staff_menu(canteen_staff, snack_inventory)
            save_snack_inventory_to_file(snack_inventory)
        elif role_choice == "3":
            # Cashier role
            cashier_menu(cashier, snack_inventory)
            save_snack_inventory_to_file(snack_inventory)
        elif role_choice == "4":
            print("Goodbye!")
            save_snack_inventory_to_file(snack_inventory)
            break
        else:
            clear_screen()  # Clear the screen for an invalid choice
            print("Invalid choice. Please select a valid option.")

def admin_menu(admin, snack_inventory):
    # Admin menu options
    while True:
        # clear_screen()
        print("Admin Menu")
        print("1. Add Snack")
        print("2. Remove Snack")
        print("3. Update Snack")
        print("4. View Snack Inventory")
        print("5. View Sales Records")
        print("6. Bulk Operations")
        print("7. Exit (Log Out)")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            admin.add_snack(snack_inventory)
            save_snack_inventory_to_file(snack_inventory)
        elif choice == "2":
            snack_id_to_remove = input("Enter the ID of the snack to remove: ")
            admin.remove_snack(snack_id_to_remove, snack_inventory)
            save_snack_inventory_to_file(snack_inventory)
        elif choice == "3":
            snack_id_to_update = input("Enter the ID of the snack to update: ")
            admin.update_snack(snack_id_to_update, snack_inventory)
            save_snack_inventory_to_file(snack_inventory)
        elif choice == "4":
            admin.check_stock_levels(snack_inventory)
            save_snack_inventory_to_file(snack_inventory)
        elif choice == "5":
            admin.view_sales_records()
            save_snack_inventory_to_file(snack_inventory)
        elif choice == "6":
    # Bulk Operations Menu
          while True:
              print("\n*** Bulk Operations ***")
              print("1. Add Snacks in Bulk")
              print("2. Update Snacks in Bulk")
              print("3. Remove Snacks in Bulk")
              print("4. Back to Admin Menu")
              
              bulk_choice = input("Enter your bulk operation choice (1/2/3/4): ")
              
              if bulk_choice == "1":
                  # admin.1bulk_add_snacks(snack_inventory)
                  bulkHandler.add_multiple_snacks(snack_inventory)
                  save_snack_inventory_to_file(snack_inventory)
              elif bulk_choice == "2":
                  bulkHandler.update_multiple_snacks(snack_inventory)
                  
                  save_snack_inventory_to_file(snack_inventory)

              elif bulk_choice == "3":
                  bulkHandler.remove_multiple_snacks(snack_inventory)
                  save_snack_inventory_to_file(snack_inventory)
              elif bulk_choice == "4":
                  break

              else:
                  clear_screen()
                  print("Invalid choice. Please select a valid option.")

        elif choice == "7":
            print("Logging out.")
            break
        else:
            clear_screen()
            print("Invalid choice. Please select a valid option.")

def canteen_staff_menu(canteen_staff, snack_inventory):
        while True:
            # clear_screen()
            print(f"{canteen_staff.role_name} Menu")
            print("1. Mark Snack Out of Stock")
            print("2. Check Stock Levels")
            print("3. View Snack Details")
            print("4. Exit (Log Out)")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                canteen_staff.mark_snack_out_of_stock(snack_inventory)
                save_snack_inventory_to_file(snack_inventory)
            elif choice == "2":
                canteen_staff.check_stock_levels(snack_inventory)
                save_snack_inventory_to_file(snack_inventory)
            elif choice == "3":
                canteen_staff.view_snack_details(snack_inventory)
                save_snack_inventory_to_file(snack_inventory)
            elif choice == "4":
                print("Logging out.")
                break
            else:
                clear_screen()
                print("Invalid choice. Please select a valid option.")

# Similar menu functions for Canteen Staff and Cashier roles can be defined here
def cashier_menu(cashier, snack_inventory):
    while True:
        # clear_screen()
        print(f"{cashier.role_name} Menu")
        print("1. Make Sale")
        print("2. View Sales Records")
        print("3. Exit (Log Out)")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            cashier.make_sale(snack_inventory)
            save_snack_inventory_to_file(snack_inventory)
        elif choice == "2":
            cashier.view_sales_records()
            save_snack_inventory_to_file(snack_inventory)
        elif choice == "3":
            print("Logging out.")
            save_snack_inventory_to_file(snack_inventory)
            break
        else:
            # clear_screen()
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
