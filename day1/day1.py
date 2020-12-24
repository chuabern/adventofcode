
with open("day1_input.txt") as f:
    numbers = list(f.read().split('\n'))

def find_two_numbers(numbers):
    for i in numbers:
        number_1 = int(i)
        for n in range(1,len(numbers)):
            number_2 = int(numbers[n])
            sum = number_1 + number_2
            if sum == 2020:
                return (number_1 * number_2)

print(find_two_numbers(numbers))

def find_three_numbers(numbers):
    for i in numbers:
        number_1 = int(i)
        for j in range(1,len(numbers)):
            number_2 = int(numbers[j])
            for k in range(2, len(numbers)):
                number_3 = int(numbers[k])
                sum = number_1 + number_2 + number_3
                if sum == 2020:
                    return (number_1 * number_2 * number_3)

print(find_three_numbers(numbers))