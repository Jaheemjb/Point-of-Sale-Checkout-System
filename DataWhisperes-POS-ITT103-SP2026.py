#This is a Point Of Sale system (POS) that will allow a cashier to process the customer's Purchase

#This system provides an easy-to-use interface where the cashiers can add items to a shopping cart
# Remove items, view the cart, calculate the total bill, accept payment and Generates a receipt

print("====BEST BUY RETAIL STORE===")
print("Digital Checkout System")
print("-"*40)
print("Item")
print("-"*40)

#The program stores the information using a list of tuples (Items) as seen below

Items={
"Bread":{"price":220,"stock":20},
"Juice":{"price":250,"stock":15},
"Water":{"price" :150,"stock":25},
"Chicken":{"price":850, "stock":15},
"Fish":{"price": 1200,"stock":4},
"Rice":{"price":200,"stock":15},
"Oil":{"price":750,"stock":9},
"Seasoning":{"price":150,"stock":12},
"Detergent":{"price":650,"stock":4},
"Toilet Paper":{"price": 130,"stock":20},

}
# Items.Items() returns both the key and the value for each item entered in the dictionary
# Info represents both the stock and the price
for item, info in Items.items():
    print(f"{item:15} Price: {info['price']:5}   Stock: {info['stock']}")

# Variables stored before being used in a function
# Cart[] is a list that stores all the items
total=int()
cart=[]
cost_price = int()
stock_count = int()


# The Function add_to_cart () allows the user to add items based on the list and enter an amount , while also calculating
# the total items being selected
def add_to_cart():

# This loop allows the user to enter an item and select an amount based on the if statements created, it also allows
# the user to exit the program
     while True:

     # We ask the user to enter an item
        product = str(input("Enter a Item: ")).strip().title()
        print("\nType exit to leave !")
        # If the user enters "exit" instead of an item they will exit the program
        if product.lower()== "exit":
            print ("Exit system :)")
            break
         # The program uses exception to prevent crashing; non-numeric inputs cannot crash the function it simply asks
         # the user to re-enter
        try:
            # We ask the user to enter an Amount

            quantity = int(input("Amount is : "))
        except ValueError:
            print("Please Enter a number")
            continue
 # This if-else statement checks if the value stored in product exists inside the items Dictionary
    # If the user does not enter an item listed , the program will display "Item not found" and ask the user to re-enter

        if product in Items:
        # This declares that values of the price and the stock are stored in the variables cost_price and stock_count
        # so that they can be represented to the user along with the item entered

            cost_price=Items[product]["price"]
            stock_count = Items[product]["stock"]
        else:
            print ("Item not found")
            continue

      # If the amount of products stored in the cart is greater than the amount the user enters the program should display
        #"Item has been added to cart" else it will display "Item is out of stock"

        if stock_count>= quantity :
            print ("Item has been added to cart")
            # By using cart.append it displays the product,quantity and cost price the user enters
            cart.append([product, quantity, cost_price])

            # The stock will gradually decline as the user selects an item
            Items[product]["stock"]-=quantity
        else:
            print("Item is out of stock")
            continue
         #Calculating the total items stored in the cart and using subtotal to increment them
        sub_total=int()
        total = cost_price * quantity
        sub_total+=total

        #Displaying the price of the items and the amount of each item
        print("Price is :", cost_price)
        print("Amount is :", quantity)


#This indicates that if the items in stock is less than 5, the program should display a "Low stock alert"
        if stock_count <5:
            print ("Low stock alert !")






# The Function remove_item() allows the user to remove any item in the cart
def remove_item():
    #Removing items from cart
    #Item[0] = product name , Item[1]= quantity, Item[2]= cost price
# If the number of items in the list is equal to 0 then the program will ask the user to reprompt while displaying
#"Cart is empty" else the program will ask the user to remove an item

    if len(cart)==0:
        print ("Cart is empty")
        return
    item_remove=input("Enter item to remove :")
    # "item" displays one of the items shown in the list, so if the item in the list is = the item the user enters
    # the program will remove said item and display " Item removed"
    for item in cart :
        if item[0]== item_remove:
            cart.remove(item)
            print ("Item removed")
            return
    print ("Item not found")







 #The view_cart () function allows the user to look at the items stored in the cart
def view_cart():
    # If items stored in the cart is equal to 0 the program will reprompt , else the program will continue
    if len(cart)==0:
        print ("The cart is empty")
    else:
        print ("---Cart Items--")
        # Displays items stored in the cart based on the list and arranges them accordingly
        for item in cart:
            name = item[0]
            quantity = item[1]
            cost_price= item[2]
            print (name,"-", quantity,"-", cost_price ,"- Total:", quantity*cost_price )

# This loop forces the user to make a correct choice
while True:
# This allows the user to properly identify each option
    print("\n1.Add Item to Cart")
    print("2.Remove Items")
    print("3.View Cart")
    print("4.Exit")
    choice=input("Enter Choice (1-4):")
# The user can select a number from 1-4 and that number will allow them to select any option of their choice

    if choice=="1":
        add_to_cart()
    elif choice =="2":
        remove_item()
    elif choice =="3":
        view_cart()
    elif choice=="4":
        # Listing the name of the store and its location by printing it in a receipt format
        print("\n====BEST BUY RETAIL STORE====")
        print("Fairview shopping center, Montego Bay")
        print("-"*50)
        sub_total=0
# This loop allows the Total, Subtotal , Sales Tax and Total after tax to be calculated separately in the checkout system
        for item in cart:
            name= item[0]
            quantity=item[1]
            cost_price=item[2]
            total= quantity*cost_price
            sub_total += total
            print(name, "-", quantity, "-", cost_price)
            sales_tax= 0.10*total
            tax_total= sales_tax + sub_total
            #If the Subtotal is greater than $5000 then a discount of 5% will be added
            if sub_total>5000:
                discount= sub_total * 0.05
                tax_total-= discount
                print ("\n A 5% discount has been added")
# Displaying The Subtotal , Tax amount and Amount after tax in the checkout system
            print("Your Subtotal is:", sub_total)
            print("Your tax is:", sales_tax)
            print("Total amount after tax :", tax_total)
            #Cash received from the customer

# This function does three things; asks the cashier to enter the amount received from the customer, checks if the amount
# is less than the total of the items , then calculates the change
        while True:
#This if statement prevents the program from crashing if the user exits the program without adding an item

            if len(cart)==0:
                print("Have a nice day :)")
                break
            else:

# The exception handling prevents the program from crashing if the user does not enter a numeric value

                try:
                    cash=float(input("Enter amount received from customer:"))
                except ValueError:
                     print ("Enter a numeric value")
                     continue

                if cash<tax_total:
                   print("Not enough money")

                else:
                    change = cash-tax_total

                    print ("Your change is :", change)
                    print("Have a nice day :)")


                    break
        break


print("\nI CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT")

































































