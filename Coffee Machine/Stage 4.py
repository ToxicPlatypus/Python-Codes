print('The coffee machine has:')
print('400 of water')
print('540 of milk')
print('120 of coffee beans')
print('9 of disposable cups')
print('550 of money')

x = input('Write action (buy, fill, take): ')
if x == 'buy':
    y = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:'))
    
    if y == 1:
        print('The coffee machine has:')
        print('150 of water')
        print('540 of milk')
        print('104 of coffee beans')
        print('8 of disposable cups')
        print('554 of money')
    if y == 2:
        print('The coffee machine has:')
        print('50 of water')
        print('465 of milk')
        print('100 of coffee beans')
        print('8 of disposable cups')
        print('557 of money')
    if y == 3:
        print('The coffee machine has:')
        print('200 of water')
        print('440 of milk')
        print('108 of coffee beans')
        print('8 of disposable cups')
        print('556 of money')

if x == 'fill':
    water = int(input('Write how many ml of water do you want to add: '))
    milk = int(input('Write how many ml of milk do you want to add: '))
    bean = int(input('Write how many grams of coffee beans do you want to add: '))
    cup = int(input('Write how many disposable cups of coffee do you want to add: '))

    print('The coffee machine has:')
    print(400 + water,' of water')
    print(540 + milk, ' of milk')
    print(120 + bean, ' of coffee beans')
    print(9 + cup, ' of disposable cups')
    print('550 of money')

if x == 'take':
    print('I gave you $550\n')
    print('The coffee machine has:')
    print('400 of water')
    print('540 of milk')
    print('120 of coffee beans')
    print('9 of disposable cups')
    print('0 of money')
    








