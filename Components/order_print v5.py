# List to store ordered Charms
order_list =['Ariel Charm', 'Dancing Groot Charm', 'Broken Heart Charm', 'Pave Heart Charm', 'Circle of Pave Charm' ]
# List to store Charm prices
order_cost = [129, 89, 59, 79, 59]

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
    if len(order_list) >= 5:
        print("Your order will be delivered to you for free")
    elif len(order_list) < 5:
        print("Due to the fact that you have ordered less than 5 items, there is a $9.00 surcharge for delivery")
        total_cost = total_cost + 9
    print("Order Cost Details")
    print(f"${total_cost:.2f}")

print_order()