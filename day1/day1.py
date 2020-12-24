
with open("day1_input.txt") as f:
    numbers = list(f.read().split('\n'))

def find_numbers(numbers):
    for i in numbers:
        number_1 = int(i)
        for n in range(1,len(numbers)):
            number_2 = int(numbers[n])
            sum = number_1 + number_2
            if sum == 2020:
                return (number_1 * number_2)
        if sum == 2020:
            break

find_numbers(numbers)