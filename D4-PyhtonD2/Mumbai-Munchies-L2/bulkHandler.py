

class BulkHandler:
    def __init__(self):
        self.user_role = "Admin"

    
    def update_multiple_snacks(self, snack_inventory):
        # if self.user_role != "Admin":
        #     print("Access denied. Only Admins can perform bulk updates.")
        #     return

        try:
            print("\n=== Update Multiple Snacks in Inventory ===")
            num_snacks = int(input("Enter the number of snacks you want to update: "))

            for _ in range(num_snacks):
                snack_id_to_update = input("Enter the ID of the snack to update: ")
                if snack_id_to_update in snack_inventory:
                    snack = snack_inventory[snack_id_to_update]
                    print(f"Current Snack Details for ID {snack_id_to_update}:")
                    print(f"Name: {snack['name']}")
                    print(f"Category: {snack['category']}")
                    print(f"Price: ₹{snack['price']:.2f}")
                    print(f"Quantity: {snack['quantity']}")

                    attribute_to_update = input("Enter the attribute to update (name/price/quantity/category): ").lower()
                    if attribute_to_update in snack:
                        new_value = input(f"Enter the new value for {attribute_to_update}: ")
                        snack[attribute_to_update] = new_value
                        print(f"{attribute_to_update.capitalize()} updated successfully.")
                    else:
                        print("Invalid attribute. Please enter a valid attribute.")

                else:
                    print(f"Snack with ID {snack_id_to_update} not found in inventory.")

            print("\nSnacks updated successfully!")

        except ValueError:
            print("\nInvalid input. Please enter a valid ID and values for updating.")

    def add_multiple_snacks(self,snack_inventory):
        try:
            print("\n=== Add Multiple Snacks to Inventory ===")
            num_snacks = int(input("Enter the number of snacks you want to add: "))

            # Find the maximum existing ID and add 1 to it
            existing_ids = snack_inventory.keys()
            if existing_ids:
                new_id = str(max(map(int, existing_ids)) + 1)
            else:
                new_id = "1"  # Start with "1" as the initial ID

            for _ in range(num_snacks):
                # Get snack details from the user
                snack_name = input("Enter Snack Name You Want To Add: ")
                price = float(input("Enter the Price of the Snack: "))
                quantity = int(input("Enter Total Quantity of the Snacks: "))
                category = input("Enter the Category of the Snack: ")

                # Check if a snack with the same name and category already exists
                for snack_id, snack in snack_inventory.items():
                    if snack["name"] == snack_name and snack["category"] == category:
                        # Snack with the same name and category found, update quantity
                        snack["quantity"] += quantity
                        print("\nSnack already exists. Updated quantity.")
                        break
                else:
                    # If the loop didn't break, it means the snack doesn't exist, so add it.

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
                    print(f"Snack '{snack_name}' added successfully!")

                    # Increment the ID for the next snack
                    new_id = str(int(new_id) + 1)

            print("\nSnacks added successfully!")

        except ValueError:
            print("\nInvalid input. Please enter a valid price and quantity as numbers.")

   
    def remove_multiple_snacks(self, snack_inventory):
        # if self.user_role != "Admin":
        #     print("Access denied. Only Admins can perform bulk removals.")
        #     return

        try:
            print("\n=== Remove Multiple Snacks from Inventory ===")
            num_snacks = int(input("Enter the number of snacks you want to remove: "))

            for _ in range(num_snacks):
                snack_id_to_remove = input("Enter the ID of the snack to remove: ")
                if snack_id_to_remove in snack_inventory:
                    del snack_inventory[snack_id_to_remove]
                    print(f"Snack with ID {snack_id_to_remove} removed successfully.")
                else:
                    print(f"Snack with ID {snack_id_to_remove} not found in inventory.")

            print("\nSnacks removed successfully!")

        except ValueError:
            print("\nInvalid input. Please enter valid IDs for removing snacks.")
