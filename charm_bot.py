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


main()