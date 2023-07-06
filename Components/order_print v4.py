# List to store ordered Charms
order_list =['Ariel Charm', 'Dancing Groot Charm', 'Broken Heart Charm', 'Circle of Pave Charm' ]
# List to store Charm prices
order_cost = [129, 89, 59, 79]

cust_details = {'name': 'Carleen', 'phone': '1234456', 'house': '65', 'street': 'Golden', 'suburb': 'Howick'}

def print_order():
    total_cost = sum(order_cost)
    print ("Customer Details")
    print(f"Customer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {}   Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Order Cost Details")
    print(f"${total_cost:.2f}")

print_order()