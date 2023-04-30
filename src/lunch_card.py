class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def is_enough_money(self, subtract: float):
        return self.balance >= subtract

    def eat_lunch(self):
        if self.is_enough_money(2.6):
            self.balance -= 2.6

    def eat_special(self):
        if self.is_enough_money(4.6):
            self.balance -= 4.6

    def deposit_money(self, addition: float):
        if addition < 0:
            raise ValueError('You cannot deposit an amount of money less than zero')
        self.balance += addition

if __name__ == '__main__':
    peter_lunch = LunchCard(20)
    grace_lunch = LunchCard(30)

    peter_lunch.eat_special()
    grace_lunch.eat_lunch()

    print(f"Peter: {peter_lunch}")
    print(f"Grace: {grace_lunch}")

    peter_lunch.deposit_money(20)
    grace_lunch.eat_special()

    print(f"Peter: {peter_lunch}")
    print(f"Grace: {grace_lunch}")

    peter_lunch.eat_lunch()
    peter_lunch.eat_lunch()
    grace_lunch.deposit_money(50)

    print(f"Peter: {peter_lunch}")
    print(f"Grace: {grace_lunch}")
