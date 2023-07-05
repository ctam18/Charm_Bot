charm_names = ['Ariel Charm', 'Mickey & Minnie Padlock Charm', 'Dancing Groot Charm', 'Spider-Man Charm', 'Star Wars 3D Charm', 'BB-8 Charm', 'Compass Medallion Charm', 
               'Broken Heart Charm', 'Glass Sea Turtle Charm', 'Kiwi and Fern Charm', 'Pave Heart Charm', 'Circle of Pave Charm' ]

charm_prices = [129, 129, 89, 119, 30, 40, 59, 45, 89, 59, 59, 79]


def list():
    number_charms = 12

    for count in range (number_charms):
        print("{} {} ${:.2f}" .format(count+1, charm_names[count],charm_prices[count]))

list()