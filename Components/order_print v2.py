# List to store ordered Charms
order_list =['Ariel Charm', 'Dancing Groot Charm', 'Broken Heart Charm', 'Circle of Pave Charm' ]
# List to store Charm prices
order_cost = [129, 89, 59, 79]

cust_details = {'name': 'Carleen', 'phone': '1234456', 'house': '65', 'street': 'Golden', 'suburb': 'Howick'}



#print("\n",cust_details['name'],"\n",cust_details['phone'], "\n",cust_details['house'], "\n",cust_details['street'], "\n",cust_details['suburb'])

print("\n Customer Name: {} Customer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Suburb\n{}".format(cust_details['name'],cust_details['phone'],cust_details['house'],cust_details['street'],cust_details['suburb']))



count = 0
for item in order_list:
    print("Ordered: {}   Cost: ${:.2f}".format(item, order_cost[count]))
    count = count+1
