# Charm bot program 
import random 
from random import randint

# List of random names
names = ["Mark", "Pheobe", "Sally", "Michael", "Niall", "Rocky", "Abby", "Ross", "Ian", "Aroha"]

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

def collect():
    print ("Is your order for click and collect or delivery?")
    print ("For click and collect pleaser enter 1")
    print ("For delivery please enter 2")
    while True:
        try:
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Click and collect")
                    break

                elif delivery == 2:
                    print ("Delivery")
                    break
            else: 
                print("Number must be 1 or 2")
        except ValueError:
            print("That is not a valid number")
            print("Please enter 1 or 2")





# CLick and collect information - name and phone number






# Delivery information - name address and phone





# Choose total number of Charms - max 5






# Charm List 






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
    collect()

main()