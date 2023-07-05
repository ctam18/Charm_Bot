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
    print ("Is your order for click and collect or delivery?")
    print ("For click and collect pleaser enter 1")
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Click and collect")
                    collect_info()
                    break
                elif delivery == 2:
                    print ("Delivery")
                    delivery_info()
                    break
            else: 
                print("Number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")


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





# Print order out - including if order is del or click and collect and names and prices of each charm - total cost including any delivery charge




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
    order_type()
    list()

main()