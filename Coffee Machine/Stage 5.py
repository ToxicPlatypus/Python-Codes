water = 400
milk = 540
bean = 120
cup = 9
taka = 550

while True:
    choice = input('Write action (buy, fill, take, remaining, exit): ')
    if choice == 'remaining':
        print('The coffee machine has:')
        print(water,'of water')
        print(milk,'of milk')
        print(bean,'of coffee beans')
        print(cup,'of disposable cups')
        print('$',taka,' of money',sep='')

    if choice == 'exit':
        break

    if choice == 'take':
        print('I gave you $',taka,sep='')
        taka -= taka

    if choice == 'fill':
        x = int(input('Write how many ml of water do you want to add: '))
        water += x
        x = int(input('Write how many ml of milk do you want to add: '))
        milk += x
        x = int(input('Write how many grams of coffee beans do you want to add: '))
        bean += x
        x = int(input('Write how many disposable cups of coffee do you want to add: '))
        cup += x

    if choice == 'buy':
        x = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        if x == 'break':
            break;
        if x == '1':
            if water >= 250 and bean >= 16 and cup >= 1:
                print('I have enough resources, making you a coffee!')
                water -= 250
                bean -= 16
                cup -= 1
                taka += 4
            elif water < 250:
                print('Sorry, not enough water!')
            elif bean < 16:
                print('Sorry, not enough beans!')
            elif cup < 1:
                print('Sorry, not enough cups!')
        
        if x == '2':
            if water >= 350 and milk >= 75 and bean >= 20 and cup >= 1:
                print('I have enough resources, making you a coffee!')
                water -= 350
                milk -= 75
                bean -= 20
                cup -= 1
                taka += 7
            elif water < 350:
                print('Sorry, not enough water!')
            elif bean < 20:
                print('Sorry, not enough beans!')
            elif milk < 75:
                print('Sorry, not enough beans!')
            elif cup < 1:
                print('Sorry, not enough cups!')
        
        if x == '3':
            if water >= 200 and milk >= 100 and bean >= 12 and cup >= 1:
                print('I have enough resources, making you a coffee!')
                water -= 200
                milk -= 100
                bean -= 12
                cup -= 1
                taka += 6
            elif water < 200:
                print('Sorry, not enough water!')
            elif bean < 12:
                print('Sorry, not enough beans!')
            elif milk < 100:
                print('Sorry, not enough beans!')
            elif cup < 1:
                print('Sorry, not enough cups!')