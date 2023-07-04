# Bugs 
# will only work for valid input "d" and "c"
# invalid input triggers else statement but program does not as for input again

# list so that user can choose either click and collect or delivery

print ("Do you want your ordered delivery or to click and collect it?")

print (" For delivery enter d")
print (" For click and collect enter c")

delivery = input ()

if delivery == "d":
    print ("Delivery")

elif delivery == "c":
    print ("Click and Collect")

else:
    print("That was not a valid input")