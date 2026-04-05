# Point-of-Sale-Checkout-System
Authors: Jaheem Brown and Kemiesha Lewis
Date Created: April 5, 2026
Course: ITT103
GitHub Public URL to Code: https://github.com/Jaheemjb/Point-of-Sale-Checkout-System/blob/53f91870f7760474a67927a251967531928b56a3/DataWhisperes-POS-ITT103-SP2026.py

Purpose of the Program :

The program was created to simulate a real-world checkout system for a retail store. It allows a cashier to add items, remove items, and view the shopping cart. The system also calculates the total cost, adds a 10% sales tax, and generates a receipt. A 5% discount is applied if the subtotal exceeds $5000.

How to run the program :

•Open the python file and run the program

• A list of items with prices and stock will be displayed, along with the menu options:
(1.)Add Item to cart
(2.)Remove items
(3.)View Cart and 
(4.)Exit

•The user should select a number from 1-4 to choose any of these options

•If the user selects ("1.") they will be prompted to choose from any of the items listed

•The user should type each item as worded in the List , and should choose the quantity of that Item.

•When the user is satisfied with selection they can type "exit" in the section that says "Enter a item".

•If the user has no desires to remove an item or view cart they can select option ("4.") to checkout the items.

•The user will be prompted to enter the amount of cash received from the customer.

•The program will display the total cost and the change.


Program modification:

1. A dictionary is used to store item names, prices, and stock. 

2. A cart list is used to store selected items. 

3. A while loop was created to allow the user to enter a item , the amount and to also exit the program 

4. Stock availability is also checked to ensure that adequate amount of stock is there before an item is added

5. if-else statements and  loops are used to display the items and allow for removal.

6. Try-except is used to handle errors and prevent crashes

7. Total calculation is added to display the cost of the items before they are checked out

8. A payment system was implemented to ask the user to enter the amount received by customer

9. The change is calculated after the program checks that the amount received is not less than the total

10. A low stock alert is displayed when the quantity of an item falls below a certain level. 


Limitations:

•The user has to enter the item names correctly 
•The user has to be careful with spacing before inputing. 
•Once checkout starts the user cannot go back or exit until the transaction is completed

Assumptions:
The user understands english.

 

