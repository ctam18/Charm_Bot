import random 
from random import randint

# List of random names
names = ["Mark", "Pheobe", "Sally", "Michael", "Niall", "Rocky", "Abby", "Ross", "Ian", "Aroha"]

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


def main():
     '''
    Purpose: To generate random name from the list and print out
    a welcome message 
    Parameters: None
    Returns: None 
    '''
     welcome()


main()