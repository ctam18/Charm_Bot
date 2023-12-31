# Charm bot program 
# 05/07/23
#Bugs - phone number input allows letters
#     - Name input allows numbers

# Known Bugs
# 23/03/23 - Final printout is not printing customer details correctly

import sys
import random 
from random import randint
# Constants
LOW = 1
HIGH = 2
PH_LOW = 7
PH_HIGH = 10

# List of random names
names = ["Mark", "Pheobe", "Sally", "Michael", "Niall", "Rocky", "Abby", "Ross", "Ian", "Aroha"]
# List of charm names
charm_names = ['Ariel Charm', 'Mickey & Minnie Padlock Charm', 'Dancing Groot Charm', 'Spider-Man Charm', 'Star Wars 3D Charm', 'BB-8 Charm', 'Compass Medallion Charm', 
               'Broken Heart Charm', 'Glass Sea Turtle Charm', 'Kiwi and Fern Charm', 'Pave Heart Charm', 'Circle of Pave Charm' ]
# List of charm prices
charm_prices = [129, 129, 89, 119, 30, 40, 59, 45, 89, 59, 59, 79]

# List to store ordered Charms
order_list =[]
# List to store Charm prices
order_cost = []

# Customer details dictionary
customer_details = {}

# Validates inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")

# validates string input to check if they are alphaetical
def check_string(question):
    while True:
        response = input(question)
        x = response .isalpha()
        if x == False:
            print("Input must only contain letters ")
        else: 
            return (response.title())

# Validates inputs to check if they are blank
def val_int(low,high,question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"Please enter a number between {low} and {high}")
        except ValueError:
            print("That was not a valid input")
            print(f"Please enter a number between {low} and {high} ")

# Valdates phone number to check if it is between 7 and 10 digits
def check_phone(question, PH_LOW, PH_HIGH):
    while True:
        try: 
            num = int(input(question))
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= PH_LOW and count <= PH_HIGH:
                return str(num)
            else:
                print("NZ phone numbers have between 7 and 10 digits")
        except ValueError:
            print("Please enter a number")


# Welcome message with random name
def welcome():
    '''
    Purpose: To generate random name from the list and print out
    a welcome message 
    Parameters: None
    Returns: None 
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Weclome to Pandora***")
    print("*** My name is", name, "***")
    print("*** I will be here to help you order your favourite Jewelry Charms***")


# List for click and collect or delivery
def order_type():
    del_click = ""
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Is your order for click and collect or delivery?")
    print ("For click and collect please enter 1")
    print ("For delivery please enter 2")
    delivery = val_int(LOW,HIGH,question)
    if delivery == 1:
        print()
        print ("Click and collect")
        del_click = "Click and Collect"
        collect_info()
    else:
        print ("Delivery")
        delivery_info()
        del_click = "delivery"
    return del_click


# Click and collect information - name and phone number
def collect_info():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    print (customer_details['phone'])
    print(customer_details)


# Delivery information - name address and phone
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = check_string(question)
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)
    print (customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question )
    print (customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = check_string(question)
    print (customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = check_string(question) 
    print (customer_details['suburb'])



# Charm list
def list():
    number_charms = 12

    for count in range (number_charms):
        print("{} {} ${:.2f}" .format(count+1, charm_names[count],charm_prices[count]))


# Choose total number of Charms - max 5
# Charm order - from list - print each charm oreder with cost
def order_charm():
    # Ask for total number of charms for order
    num_charms = 0
    NUM_LOW = 1
    NUM_HIGH = 12
    MENU_LOW = 1
    MENU_HIGH = 12
    question = (f"Enter a number between {NUM_LOW} and {NUM_HIGH} ")
    print("How many Charms do you want to order? ")
    num_charms = val_int(NUM_LOW,NUM_HIGH,question)
    # Choose charm from menu
    for item in range(num_charms):
        while num_charms > 0:
            print("Please choose your charms by entering "
                  "the number from the list")
            question = (f"Enter a number between {MENU_LOW} and {MENU_HIGH} ")
            charm_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            charm_ordered = charm_ordered -1
            order_list.append(charm_names[charm_ordered]) 
            order_cost.append(charm_prices[charm_ordered])
            print("{} ${:.2f}" .format(charm_names[charm_ordered],charm_prices[charm_ordered]))
            num_charms = num_charms-1



# Print order out - including if order is del or click and collect and names and prices of each charm - total cost including any delivery charge
def print_order(del_click):
    print()
    total_cost = sum(order_cost)
    print ("Your Details")
    if del_click == "Click and Collect":
        print("Your order is for Click and Collect")
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_click == "delivery":
        if len(order_list) >= 5:
            print("Your order will be delivered to you for free")
        elif len(order_list) < 5:
            total_cost = total_cost + 9
        print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Your Order Details")
    print("Due to the fact that you have ordered less than 5 items, there is a $9.00 surcharge for delivery")
    count = 0
    for item in order_list:
        print("Ordered: {}   Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Order Cost Details")
    print(f"${total_cost:.2f}")




# Ability to cancel or proceed with order
def confirm_cancel():
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Please Confirm Your Order?")
    print ("To confirm please enter 1")
    print ("To cancel please enter 2")

    confirm = val_int(LOW,HIGH,question)
    if confirm == 1:
        print ("Order Confirmed")
        print ("Your Order has been sent to our shop")
        print ("Your Jewelry Charms will be with you shortly")
        new_exit()

    elif confirm == 2:
        print ("Your Order as been Cancelled")
        print ("You can restart your order or exit the BOT")
        new_exit()


# Option for new order or to exit
def new_exit():
    print()
    question = (f"Enter a number between {LOW} and {HIGH} ")
    print ("Do you want to start another Order or Exit")
    print ("To start another order enter 1")
    print ("To exit the BOT please enter 2")
    confirm = val_int(LOW,HIGH,question)
                     
    if confirm == 1:
        print ("New Order")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()

    elif confirm == 2:
        print ("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit

\
# Main Function
def main():
    '''
    Purpose: To run all functions
    a welcome message 
    Parameters: None
    Returns: None 
    '''
    welcome()
    del_click = order_type()
    list()
    order_charm()
    print_order(del_click)
    confirm_cancel()

main()