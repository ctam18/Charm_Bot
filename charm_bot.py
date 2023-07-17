# Charm bot program 
# 05/07/23
#Bugs - phone number input allows letters
#     - Name input allows numbers

import random 
from random import randint

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
    print ("Is your order for click and collect or delivery?")
    print ("For click and collect please enter 1")
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Click and collect")
                    del_click = "Click and Collect"
                    collect_info()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    del_click = "delivery"
                    break
            else: 
                print("Number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")
    return del_click


# CLick and collect information - name and phone number
def collect_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question )
    print (customer_details['phone'])
    print(customer_details)


# Delivery information - name address and phone
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print (customer_details['name'])

    question = ("Please enter your phone number ")
    customer_details['phone'] = not_blank(question )
    print (customer_details['phone'])

    question = ("Please enter your house number ")
    customer_details['house'] = not_blank(question )
    print (customer_details['house'])

    question = ("Please enter your street name ")
    customer_details['street'] = not_blank(question )
    print (customer_details['street'])

    question = ("Please enter your suburb ")
    customer_details['suburb'] = not_blank(question )
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
    while True:
        try:
            num_charms = int(input("How many Charms do you want to order? "))
            if num_charms >= 1 and num_charms <= 12:
                break
            else:
                print("Your order must be between 1 and 12")
        except ValueError:
            print("That is not a valid number")
            print("Please enter a number between 1 and 12")
    # Choose charm from menu
    for item in range(num_charms):
        while num_charms > 0:
            while True:
                try:
                    charm_ordered = int(input("Please choose your Charms by entering the number from the list "))
                    if charm_ordered >= 1 and charm_ordered <= 12:
                        break
                    else:
                        print("Your charm order must be between 1 and 12")
                except ValueError:
                    print("That is not a valid number")
                    print("Please enter a number between 1 and 12")
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
         print("Your order is for Delivery a $9.00 delivery charge applies if order has 5 or more items")
         print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Your Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {}   Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    if len(order_list) >= 5:
        print("Your order will be delivered to you for free")
    elif len(order_list) < 5:
        print("Due to the fact that you have ordered less than 5 items, there is a $9.00 delivey charge")
        total_cost = total_cost + 9
    print("Order Cost Details")
    print(f"${total_cost:.2f}")




# Ability to cancel or proceed with order





# Option for new order or to exit







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

main()