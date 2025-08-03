# 7.2: Simple Inventory

inventory = {
    "apple" : 50,
    "banana" : 30,
    "orange" : 20
 }


while True:
   
    print ("\n========================================\n What would you like to do? \n A - Check stock \n B - Change the stock for an item to the inventory \n C - Remove an item from the inventory \n Q - Quit \n========================================\n")
    user_input = input("Enter an option(A/B/C/Q): ").upper()

    if user_input == 'A':
        check_item = input ("Enter the name of an item - to check its stock: ").lower()
        stock_count = inventory.get(check_item)
        print(f"For {check_item}, the stock is: {stock_count}")

        if stock_count == None:
            answer = input ("Would you like to add this item to the inventory [Y/N]?: ")
            if answer == 'Y':
                inventory[check_item] = 1
                print (f"{check_item} added.")
                print(inventory)

    if user_input == 'B':
        item_to_increase = input("Enter item name to increase/decrease stock: ").lower()
        value_of_increase = input ("How many?: ")
        if int(value_of_increase) > 0:
            inventory[item_to_increase] = int(value_of_increase)
            print ("value changed.")
            print(inventory)
        elif int(value_of_increase) < 0:
            print ("Invalid value. Back to menu.")

    if user_input == 'C':
        item_to_remove = input ("Enter the item name you want to remove from inventory: ").lower()
        del inventory[item_to_remove]
        print ('Inventory changed: ', inventory)

    elif user_input == 'Q':
        print ("Exiting inventory manager. Goodbye!")
        break

    


