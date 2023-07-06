# List to store ordered Charms
order_list =['Ariel Charm', 'Dancing Groot Charm', 'Broken Heart Charm', 'Circle of Pave Charm' ]
# List to store Charm prices
order_cost = [129, 89, 59, 79]

cust_details = {'name': 'Carleen', 'phone': '1234456', 'house': '65', 'street': 'Golden', 'suburb': 'Howick'}

#print("Customer Name: {} \nCustomer Phone: {} \nCustomer Address: {} {} {}".format(cust_details['name'],cust_details['phone'],cust_details['house'],cust_details['street'],cust_details['suburb']))

print(f"Customer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")





count = 0
for item in order_list:
    print("Ordered: {}   Cost: ${:.2f}".format(item, order_cost[count]))
    count = count+1
