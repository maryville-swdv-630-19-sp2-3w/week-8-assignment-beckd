#David Beck SWDV 630 - OOP Architecture
#Final Project - Pizza Ordering System
import pandas as pd
import collections
from random import *

class Pizza:
    def __init__(self, kind, cheese, crust, sauce):
        self.kind = kind
        self.cheese = cheese
        self.crust = crust
        self.sauce = sauce
    
    def get_Kind(self):
        return self.kind
    
    def get_Cheese(self):
        return self.cheese
    
    def update_Cheese(self, value):
        update = value
        self.cheese = update
        return self.cheese
    
    def get_Crust(self):
        return self.crust
    
    def update_Crust(self, value):
        update = value
        self.crust = update
        return self.crust
    
    def get_Sauce(self):
        return self.sauce
    
    def update_Sauce(self, value):
        update = value
        self.sauce = update
        return self.sauce
        
class Hawaiian(Pizza):
    def __init__(self):
        self.toppings = ["Ham", "Pineapple"]
        Pizza.__init__(self, "Hawaiian", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class Supreme(Pizza):
    def __init__(self):
        self.toppings = ["Pepperoni", "Mushroom", "Olives", "Onion", "Bell Pepper", "Sausage"]
        Pizza.__init__(self, "Supreme", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class Combination(Pizza):
    def __init__(self):
        self.toppings = ["Pepperoni", "Olives", "Onion", "Bell Pepper"]
        Pizza.__init__(self, "Combination", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class Pepperoni(Pizza):
    def __init__(self):
        self.toppings = ["Pepperoni"]
        Pizza.__init__(self, "Pepperoni", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class Cheese(Pizza):
    def __init__(self):
        self.toppings = ["Extra Cheese"]
        Pizza.__init__(self, "Cheese", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class Sausage(Pizza):
    def __init__(self):
        self.toppings = ["Sausage"]
        Pizza.__init__(self, "Sausage", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class BBQChicken(Pizza):
    def __init__(self):
        self.toppings = ["BBQ Chicken", "Onion", "Tomato"]
        Pizza.__init__(self, "BBQ Chicken", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class Deluxe(Pizza):
    def __init__(self):
        self.toppings = ["Pepperoni", "Mushroom", "Olives", "Onion", "Bell Pepper", "Sausage", "Tomato", "Garlic"]
        Pizza.__init__(self, "Deluxe", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class MeatLovers(Pizza):
    def __init__(self):
        self.toppings = ["Pepperoni", "Sausage", "Ham", "Bacon"]
        Pizza.__init__(self, "Meat Lovers", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class Margarita(Pizza):
    def __init__(self):
        self.toppings = ["Tomato", "Basil"]
        Pizza.__init__(self, "Margarita", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class Veggie(Pizza):
    def __init__(self):
        self.toppings = ["Tomato", "Basil", "Onion", "Olives", "Bell Pepper"]
        Pizza.__init__(self, "Veggie", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class Anchovies(Pizza):
    def __init__(self):
        self.toppings = ["Anchovies"]
        Pizza.__init__(self, "Anchovies", "normal", "thin", "normal")
        
    def get_Toppings(self):
        return self.toppings

class CreditCard():
    def __init__(self, number, address, expiration):
        self.number = number
        self.address = address
        self.expiration = expiration
        
    def get_number(self):
        return self.number
    
    def get_address(self):
        return self.address
    
    def get_expiration(self):
        return self.expiration
    
    def masked_cc_number(self):
        masked_cc_number = self.number[-4:] #gets the last 4 digits
        return masked_cc_number

class Person():
    def __init__(self, name, password, address, phone, email):
        self.name = name
        self.password = password
        self.address = address
        self.phone = phone
        self.email = email
        
    def get_Name(self):
        return self.name

    def get_Password(self):
        return self.password
    
    def get_Address(self):
        return self.address
    
    def get_Phone(self):
        return self.phone
    
    def get_Email(self):
        return self.email
    
    def update_Name(self, value):
        newName = value
        self.name = newName
        return self.name
    
    def update_Address(self, value):
        newAddress = value
        self.address = newAddress
        return self.address
    
    def update_Phone(self, value):
        newPhone = value
        self.phone = newPhone
        return self.phone
    
class Employee(Person):
    MANAGER, CASHIER, COOK, DELIVERY = range(4)
    def __init__(self, employee_type, employeeID, storeNumber, *args, **kwargs):
        self.employee_type = employee_type
        self.employeeID = employeeID
        self.storeNumber = storeNumber
        super(Employee, self).__init__(*args, **kwargs)
        
    def get_Type(self):
        return self.employee_type
    
    def get_EmployeeID(self):
        return self.employeeID
    
    def get_storeNumber(self):
        return self.storeNumber
    
    def manager_Discount(self, order_bill, discount_percent): #manager can give discounts, they provide the percent
        if self.employee_type == 0:
            order_bill = order_bill - (order_bill / discount_percent)
            return order_bill
        
    def cashier(self):
        if self.employee_type == 1:
            print("{} will be your Cashier, ask for them when you arrive at {}!".format(self.get_Name(), self.get_storeNumber()))
            
    def cook(self):
        if self.employee_type == 2:
            print("{} is cooking your pizza to perfection!".format(self.get_Name()))
            
    def delivery(self):
        if self.employee_type == 3:
            print("{} is your delivery person, they are on the way!".format(self.get_Name()))
    
    def delivery_Contact(self):
        if self.employee_type == 4:
            print("If you need to contact {} for any reason regarding your order, their number is {}.".format(self.get_Phone()))
            

class Customer(Person):
    def __init__(self, orderID, userID, *args, **kwargs):
        self.orderID = orderID
        self.userID = userID
        super(Customer, self).__init__(*args, **kwargs)
        
    def get_userID(self):
        return self.userID

class Guest():
    def __init__(self, guestID, orderID):
        self.guestID = guestID
        self.orderID = orderID
        
    def get_GuestID(self):
        return self.guestID
    
    def get_OrderID(self):
        return self.orderID

class Order():
    def __init__(self, order_items, order_bill, orderID):
        self.order_items = order_items
        self.order_bill = order_bill
        self.orderID = orderID
    
    def get_order_items(self):
        return self.order_items
    
    def get_order_bill(self):
        return self.order_bill
    
    def get_orderID(self):
        return self.orderID
    
def Intro(): #prints a welcome message to the user
    print("-----------------------------------------------")
    print("|          Welcome to Dave's Pizzeria         |")
    print("| Where we only use the freshest ingredients, |")
    print("|     And your satisfaction is guaranteed!    |")
    print("-----------------------------------------------")
    print()

def menu():
    pizzas = [
        "Hawaiian",
        "Supreme",
        "Combination",
        "Pepperoni",
        "Cheese",
        "Sausage",
        "BBQ Chicken",
        "Deluxe",
        "Meatlovers",
        "Margarita",
        "Veggie",
        "Anchovies"
        ]

    df = pd.DataFrame(pizzas, columns=["Pizzas"])
    df.loc[:8, "Prices"] = 7.50     # First 7 items.
    df.loc[8:, "Prices"] = 13.50    # All the rest.
    df.index += 1                   # So that it's not zero-indexed.
    total_bill = 0.0  
    total_items = []
    pizza_count = 0

    print()
    print("Here's our menu!")
    print()

    print(df.to_string(justify='left', header=False, formatters={'Pizzas':'{{:<{}s}}'.format(df['Pizzas'].str.len().max()).format,'Prices':'     ${:.2f}'.format}))
    print()
    print("Input a number and press enter to select an item.")
    print("Input 'done' to finish your order and calculate your bill.")
    print("Input 'exit' to cancel your orders.")

    while True:

        order = input(">>>  ")

        if order == 'exit':
            break
        elif order == 'done':
            print("You've ordered {} pizzas, your total bill is ${:.2f}.".format(len(total_items), total_bill))
            for pizza in total_items:
                if pizza == "Hawaiian":
                    pizza = Hawaiian()
                elif pizza == "Supreme":
                    pizza = Supreme()
                elif pizza == "Combination":
                    pizza = Combination()
                elif pizza == "Pepperoni":
                    pizza = Pepperoni()
                elif pizza == "Cheese":
                    pizza = Cheese()
                elif pizza == "Sausage":
                    pizza = Sausage()
                elif pizza == "BBQ Chicken":
                    pizza = BBQChicken()
                elif pizza == "Deluxe":
                    pizza = Deluxe()
                elif pizza == "Meatlovers":
                    pizza = Meatlovers()
                elif pizza == "Margarita":
                    pizza = Margarita()
                elif pizza == "Veggie":
                    pizza = Veggie()
                elif pizza == "Anchovies":
                    pizza = Anchovies()
            input("Press any key to continue.")
            return total_items, total_bill
        elif int(order) in df.index:
            item = df.loc[int(order), "Pizzas"]     # Get the respective items
            price = df.loc[int(order), "Prices"]    # by indexing order input.
            print("You've selected {}! That would be ${:.2f}.".format(item, price)) #confirm their selection
            total_bill += price #add it to the bill
            total_items.append(item) #append it to our list
            continue
        else:
            print("Please type 'done' all in lower case.") 
            input("Press any key to continue.")
            break
        
def userInfo(): #starts gathering user info so we can create the appropriate classes later
    valid_userType = ["y", "n"] #an array with the only valid inputs
    userType = input("Is this your first time dining with us?(y/n): ") #gets input
    lower_userType = userType.lower() #converts to lower case
    while lower_userType not in valid_userType:
        print()
        print("That is not a valid option, you must put in either 'y' for yes or 'n' for no, please try again.")
        userType = input("Is this your first time dining with us?(y/n): ")
        lower_userType = userType.lower()
    
    if lower_userType == "n":
        return "n"
    else:
        return "y"
    
def new_or_guest(): #starts gathering user info so we can create the appropriate classes later
    valid_userType = ["n", "g"] #an array with the only valid inputs
    userType = input("Would you like to create an account or continue as a guest?(n/g): ") #gets input
    lower_userType = userType.lower() #converts to lower case
    while lower_userType not in valid_userType:
        print()
        print("That is not a valid option, you must put in either 'n' for new account or 'g' for guest, please try again.")
        userType = input("Would you like to create an account or continue as a guest?(n/g): ")
        lower_userType = userType.lower()
    
    if lower_userType == "n":
        return "n"
    else:
        return "g"

def newUser():
    print("Thank you for creating an account with us! Let's get started!")
    print()
    newUsername = input("Please enter a username: ")
    print()
    newPassword = input("Please enter a password: ")
    print()
    confirmPassword = input("Please confirm the password: ")
    print()
    newAddress = input("Enter your address: ")
    print()
    newPhone = input("Enter your phone: ")
    print()
    newEmail = input("Enter your email: ")
    print()
    while newPassword != confirmPassword:
        print("The passwords do not match, please try again.")
        newPassword = input("Please enter a password: ")
        print()
        confirmPassword = input("Please confirm the password: ")
    else:
        return newUsername, newPassword, newAddress, newPhone, newEmail
    
def existingUser():
    print("Thanks for coming back!")
    print()
    print("Let's get logged in, shall we.")
    print()
    existingUsername = input("username: ")
    existingPassword = input("password: ")
    print()
    print("login successful! welcome back {}!".format(existingUsername))
    print()
    return existingUsername, existingPassword

def pickup_or_delivery():
    print()
    valid_receivingOrder = ["p", "d"]
    receivingOrder = input("How would you like to receive your order? Pick Up or Delivery? (p/d): ")
    lower_receivingOrder = receivingOrder.lower()
    while lower_receivingOrder not in valid_receivingOrder:
        print()
        print("That is not a valid option, you must put in either 'p' for pick up or 'd' for delivery, please try again.")
        receivingOrder = input("How would you like to receive your order? Pick Up or Delivery? (p/d): ")
        lower_receivingOrder = receivingOrder.lower()
    return lower_receivingOrder

def pickUp():
    print()
    print("Got it. You have chosen to pick up your order.")
    
def delivery(customerType, existingCustomer): #We'll check the customerType variable to see where we should pull the address from, and display accordingly
    print()
    print("You have chosen to have your order delivered. Let's confirm your address.")
    print()
    confirmed_address = []
    if customerType == 1 or customerType == 2: #If the customer is New or Existing
        valid_address = ["y", "n"]
        get_address = existingCustomer.get_Address()
        address = input("Would you like to have the order delivered to {}?(y/n): ".format(get_address))
        lower_valid_address = address.lower()
        while lower_valid_address not in valid_address:
            print("That is not a valid option. Please put either 'y' for yes or 'n' for no. Please try again.")
            address = input("Would you like to have the order delivered to {}?(y/n): ".format(get_address))
            lower_valid_address = address.lower()
            
        if lower_valid_address == "y":
            print()
            print("Thank you. We've got it.")
            confirmed_address.append(existingCustomer.get_Address())
            return confirmed_address
        else:
            print()
            delivery_address = input("Where would you like it delivered?: ")
            confirmed_address.append(delivery_address)
            print("We got it. We have your address as {}.".format(confirmed_address))
            return confirmed_address
    else: #Customer Type must be a guest
        print()
        delivery_address = input("Where would you like it delivered?: ")
        delivery_phone = input("A phone number we we can reach you?: ")
        confirmed_address.append(delivery_address)
        print("We got it. We have your address as {}.".format(confirmed_address))                  
        return confirmed_address
    
def cash_or_cc():
    print()
    valid_cash_cc = ["cash", "cc"]
    cash_or_cc = input("How would you like to pay? Cash or Credit Card?(cash/cc): ")
    lower_cass_cc = cash_or_cc.lower()
    while lower_cass_cc not in valid_cash_cc:
        print()
        print("That's not a valid input. Please put either 'cash' for cash, or 'cc' for credit card.")
        cash_or_cc = input("How would you like to pay? Cash or Credit Card?(cash/cc): ")
        lower_cass_cc = cash_or_cc.lower()
    return cash_or_cc

def pay_cc():
    print()
    get_cc_name = input("Name on the card: ")
    get_cc_number = input("Credit Card Number: ")
    get_cc_address = input("Address for that card: ")
    get_cc_expire = input("The expiration for that card: ")
    return get_cc_number, get_cc_address, get_cc_expire, get_cc_name
       
def main():
    Intro()
    customerType = 0
    #Driver to get Customer Order and Instantiate an Order Object Class
    order = menu() #Shows our menu and gets the user's item inputs
    order_items = order[0] #Creates a variable for our total bill price
    order_bill = order[1] #Creats a variable with an array of our pizzas
    orderID = randint(100, 1000) #Generates a 3 digits number to use as our order ID
    order1 = Order(order_items, order_bill, orderID)
    order1_items = order1.get_order_items()
    count_items = collections.Counter(order1_items)
    order1_items_len = len(order1_items)
    
    #Driver to Determine User Account Status as Existing, New, or Guest
    new_or_existing = userInfo() #Tells us if they are an existing user or not and directs them accordingly
    if new_or_existing == "y": #User indicates that they are not an existing user
        new_or_guest_value = new_or_guest()
        #if they are not an existing user, we ask them if they want to create an account or sign on as a guest
        if new_or_guest_value == "n": #Indicates they want to create a new account
            customerType = 1
            newUser_value = newUser()
            newUserName = newUser_value[0]
            newUserPassword = newUser_value[1]
            newAddress = newUser_value[2]
            newPhone = newUser_value[3]
            newEmail = newUser_value[4]
            newUserID = randint(100, 1000) #We'll generate an ID for them
            #Now that we have all the required information, we can instantiate a new Customer Class object associated with our order number
            existingCustomer = Customer(orderID, newUserID, newUserName, newUserPassword, newAddress, newPhone, newEmail)
            
            
        else: #They do not want to sign up for an acccount, so we'll give them a GuestID 
            guestID = "Guest1234"
            customerType = 3
            guestCustomer = Guest(guestID, orderID)
    else:
        existingUser_value = existingUser() #User indicates they are an existing user, so we direct them there
        customerType = 2
        existingUsername = existingUser_value[0]
        existingPassword = existingUser_value[1]
        existingAddress = "123 Main St. Whoville USA, 12345" #We'll give them some fake info, because is they were an exsiting customer we'd already have it.
        existingPhone = "123-867-5309"
        existingEmail = "fakie@fakeemail.com"
        existingUserID = "123456789"
        #We've validated they are an existing customer, now we can create and Customer Class object associated with our order number  
        existingCustomer = Customer(orderID, existingUserID, existingUsername, existingPassword, existingAddress, existingPhone, existingEmail)
        print(existingCustomer.get_Address())

    
    #Driver to Create Employee Class and Sub-Classes
    employee1 = Employee(Employee.MANAGER, "456", "Store - 120 9876 Penny Ln. Anytown USA 65432", "John", "12345", "345 Broadway", "987-987-4321", "john@davespizza.com")
    employee2 = Employee(Employee.CASHIER, "678", "Store - 120 9876 Penny Ln. Anytown USA 65432", "Paul", "12345", "911 Maple", "987-693-1234", "paul@davespizza.com")
    employee3 = Employee(Employee.COOK, "901", "Store - 120 9876 Penny Ln. Anytown USA 65432", "George", "12345", "42 A Ave", "987-489-5678", "george@davespizza.com")
    employee4 = Employee(Employee.DELIVERY, "321", "Store - 120 9876 Penny Ln. Anytown USA 65432", "Ringo", "12345", "446 Birch", "987-879-8765", "ringo@davespizza.com")
        
    #Driver to determine the mode of receiving their order
    receive_order = pickup_or_delivery() #gets their preference for receiving their order
    if receive_order == "p":
        pickUp()
    elif customerType == 3:
        get_address = delivery(customerType, guestCustomer)
        confirmed_delivery_address = get_address[0]
    else:
        get_address = delivery(customerType, existingCustomer)
        confirmed_delivery_address = get_address[0]
        
    #Driver to Payment Class, gets payment method then creates a class of that object
    payment_method = cash_or_cc()
    if payment_method == "cash":
        print("Your total will be ${:.2f}, payable on receiving your order.".format(order1.get_order_bill()))
    else:
        credit_card_payment = pay_cc()
        make_cc_payment = CreditCard(credit_card_payment[0], credit_card_payment[1], credit_card_payment[2]) #creates a Credit Card class object with the info we received.
        print()
        print("We've charged the card ending in {} the amount ${:.2f}, thank your for your order!".format(make_cc_payment.masked_cc_number(),order1.get_order_bill()))
              
    #Let's print out a final message to our customer
    print()
    print("Thank your for ordering with Dave's Pizza!")
    print("Here is your order:")
    print()
    print("Your order number is {}.".format(order1.get_orderID())) #order number
    for pizza_kind in count_items:
        print('{} {}'.format(count_items[pizza_kind], pizza_kind)) #nice printout of their order
    print()
    print("Your total comes out to ${:.2f}".format(order1.get_order_bill())) #include the total
    print()
    #Let's format some print outs based on their mode of receiving the order and payment
    if receive_order == "p" and payment_method == "cash": #pickup and cash
        print("You've chosen to pay cash on pickup")
        employee2.cashier()
    elif receive_order == "p" and payment_method != "cash": #pickup and credit card
        print("You've chosen to pick up your order.")
        employee2.cashier()
        print("We've charged the card ending in {} the amount of ${:.2f}!".format(make_cc_payment.masked_cc_number(),order1.get_order_bill()))
    elif receive_order != "p" and payment_method == "cash": #delivery and cash
        print("You've chose to have your order delivered to {} and pay cash.".format(confirmed_delivery_address,order1.get_order_bill))
        employee4.delivery()
        employee4.delivery_Contact()
    elif receive_order != "p" and payment_method != "cash": #delivery and credit card
        print("You've chose to have your order delivered to {} and pay with a credit card.".format(confirmed_delivery_address,order1.get_order_bill))
        employee4.delivery()
        employee4.delivery_Contact()
        print("We've charged the card ending in {} the amount ${:.2f}!".format(make_cc_payment.masked_cc_number(),order1.get_order_bill()))
    
    print()
    print("Thank you so much for your order, it's a pleasure serving you! Enjoy!")
        
main()