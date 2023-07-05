# List of charm names
charm_names = ['Ariel Charm', 'Mickey & Minnie Padlock Charm', 'Dancing Groot Charm', 'Spider-Man Charm', 'Star Wars 3D Charm', 'BB-8 Charm', 'Compass Medallion Charm', 
               'Broken Heart Charm', 'Glass Sea Turtle Charm', 'Kiwi and Fern Charm', 'Pave Heart Charm', 'Circle of Pave Charm' ]
# List of charm prices
charm_prices = [129, 129, 89, 119, 30, 40, 59, 45, 89, 59, 59, 79]

# List to store ordered Charms
order_list =[]
# List to store Charm prices
order_cost = []

# List to store order cost

def list():
    number_charms = 12

    for count in range (number_charms):
        print("{} {} ${:.2f}" .format(count+1, charm_names[count],charm_prices[count]))

list()

# Ask for total number of charms for order
num_charms = 0


while True:
    try:
        num_charms = int(input("How many Charms do you want to order? "))
        if num_charms >= 1 and num_charms <= 5:
            break
        else:
            print("Your order must be between 1 and 5")
    except ValueError:
        print("That is not a valid number")
        print("Please enter a number between 1 and 5")



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


