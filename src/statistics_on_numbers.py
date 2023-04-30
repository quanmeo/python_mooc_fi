class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.records = []

    def add_number(self, number: int):
        self.records.append(number)
        self.numbers += 1

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return sum(self.records) if self.count_numbers() != 0 else 0

    def average(self):
        return (sum(self.records) / self.count_numbers()) if self.count_numbers() != 0 else 0

number_stat = NumberStats()
even_stat = NumberStats()
odd_stat = NumberStats()

print('Please type in integer numbers: ')
while True:
    number = int(input())
    if number == -1:
        break

    number_stat.add_number(number)
    if number % 2 == 0:
        even_stat.add_number(number)
    else:
        odd_stat.add_number(number)

print(f"Sum of numbers: {number_stat.get_sum()}")
print(f"Mean of numbers: {number_stat.average()}")
print(f"Sum of even numbers: {even_stat.get_sum()}")
print(f"Sum of the odd numbers: {odd_stat.get_sum()}")
