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



num_charms = int(input("How many Charms do you want to order? "))



print(num_charms)

# Choose charm from menu
print("Please choose your Charms by entering the number from the list")
for item in range(num_charms):
    while num_charms > 0:
        charm_ordered = int(input()) 
        charm_ordered = charm_ordered -1
        order_list.append(charm_names[charm_ordered]) 
        order_cost.append(charm_prices[charm_ordered])
        print("{} ${:.2f}" .format(charm_names[charm_ordered],charm_prices[charm_ordered]))
        num_charms = num_charms-1

print(order_list)
print(order_cost)





# Countdown until all charms are ordered



# Print order