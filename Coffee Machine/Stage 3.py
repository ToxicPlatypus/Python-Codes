water = int(input('Write how many ml of water the coffee machine has: '))
coffee = int(input('Write how many ml of milk the coffee machine has: '))
beans = int(input('Write how many grams of coffee beans the coffee machine has: '))
need = int(input('Write how many cups of coffee you will need: '))

water = water / 200
coffee = coffee / 50
beans = beans / 15

ans = int(min(water, coffee, beans))

if ans == need:
    print("Yes, I can make that amount of coffee")
elif ans > need:
    print("Yes, I can make that amount of coffee (and even ",ans-1," more than that)")
else:
    print("No, I can make only ",ans," cups of coffee")