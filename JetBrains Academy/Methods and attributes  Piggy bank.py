class PiggyBank:
    def __init__(self, dollars, cents):
        self.cents = cents % 100
        self.dollars = dollars + cents // 100

    def add_money(self, deposit_dollars, deposit_cents):
        total_cents = self.cents + deposit_cents
        self.dollars += deposit_dollars + total_cents // 100
        self.cents = total_cents % 100