def final_deposit_amount(*interest, amount):
    for n in interest:
        amount = amount * (1 + n / 100)
    return round(amount, 2)
