print ("Please Confirm Your Order?")
print ("To confirm pleaser enter 1")
print ("To cancel please enter 2")
while True:
    try:
        confirm = int(input("Please enter a number "))
        if confirm >= 1 and confirm <= 2:
            if confirm == 1:
                print ("Order Confirmed")
                print ("Your Order has been sent to our shop")
                print ("Your Jewelry Charms will be with you shortly")
                break

            elif confirm == 2:
                print ("Your Order as been Cancelled")
                print ("You can restart your order or exit the BOT")
                break
        else: 
            print("Number must be 1 or 2")
    except ValueError:
        print("That is not a valid number")
        print("Please enter 1 or 2")