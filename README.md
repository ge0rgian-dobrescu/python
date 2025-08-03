# python - a repository made for scripts, projects and other cool stuff.
## This repository will store a list of all projects I create.
### 
### 1. Simple Inventory Manager (SIM)
### 

#### 1. Simple Inventory Manager (SIM):
- This is a simple Python program which purpose is to understand the dictionary rules and ways of working. It is also a pretty good practice for the if/else statements.
The program begins by initializing an "inventory" dictionary to allow for modifications. It starts with three objects, each with a unique key-value pair.
A straightforward command-line interface (CLI) GUI makes it easy for users to test:
 The menu looks something like this in the command line:
 ========================================
  What would you like to do? 
  A - Check stock 
  B - Change the stock for an item to the inventory 
  C - Remove an item from the inventory 
  Q - Quit 
 ========================================
 It let's the user perform 3 actions(Check/Change/Remove) on the "key:value" pair mentioned earlier. These actions are the easiest to implement and also the most common uses for this type of program.

How it works? Well, let's explain a bit:
 A - Let's say the user wants to check the number of "apples" in the inventory. The program will ask the user what's the fruit's name. There are two scenarios:
    1. The fruit exists: The program outputs the stock number of that fruit.
    2. The fruit doesn't exist: The program asks the user if they want to add it to the inventory. If the answer is positive, the fruit will be added to the inventory, and its stock value will be set to 1.
 B - It works similarly to 'A', but instead, the user inputs a specific stock value for the fruit.
 C - The program asks for the item to remove from the inventory and then deletes both the fruit's name and its stock number (the key-value pair).
 Q - This action allows you to quit the program. Simply press 'Q' when you're done with the inventory, and the program will close.
