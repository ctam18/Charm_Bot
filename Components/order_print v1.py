# List to store ordered Charms
order_list =['Ariel Charm', 'Dancing Groot Charm', 'Broken Heart Charm', 'Circle of Pave Charm' ]
# List to store Charm prices
order_cost = [129, 89, 59, 79]


count = 0
for item in order_list:
    print("Ordered: {}   Cost: ${:.2f}".format(item, order_cost[count]))
    count = count+1
