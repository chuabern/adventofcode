with open('day9_input.txt', 'r') as text:
    lines = text.read().split("\n")

lines = list(map(int, lines)) # Convert all to int
all_numbers = lines
# Goal: check which number is not the sum of two of the 25 numbers before


# with open('all_numbers.txt', 'r') as text:
#     lines = text.read().split("\n")

# lines = list(map(int, lines)) # Convert all to int
# all_numbers = lines

starting_index = 25

# Part 1

def check_sum(all_numbers, starting_index):
  initial_number = all_numbers[starting_index]
  for number in all_numbers[starting_index:]:
    numbers_to_look_at = all_numbers[all_numbers.index(number)-starting_index:all_numbers.index(number)]

    for preceding_number in numbers_to_look_at:
      # print('preceeding_number', preceding_number)
      complementary_number = number - preceding_number
      # print('complementary_number', complementary_number)
      number_of_matches = 0

      if complementary_number not in numbers_to_look_at or complementary_number == preceding_number:
        # print(f"There was no match for {number}")
        continue

      elif complementary_number in numbers_to_look_at and complementary_number != preceding_number:
        # print(f"Preceding number is {preceding_number} and complementary number is {complementary_number}")
        number_of_matches += 1
        break

    # print(f'number_of_matches {number_of_matches}')

    if number_of_matches == 0:
      print("Found! This number couldn't be matched")
      return number

desired_number = check_sum(all_numbers, starting_index)
print(desired_number)

print('\n\n\n\n\n')


### Part 2

def find_list_of_numbers(all_numbers):
  for number in all_numbers:
    # print('number', number)
    total_count = number

    index = all_numbers.index(number)
    list_of_numbers = [number]

    for subsequent_numbers in all_numbers[index+1:]:
      # print('subsequent_number', subsequent_numbers)
      # print('total_count', total_count)

      if desired_number - total_count > 0:
        list_of_numbers.append(subsequent_numbers)
        # print("Adding the next number...")
        total_count += subsequent_numbers
      elif desired_number - total_count < 0:
        # print("Too much! Exiting loop")
        break
      # elif desired_number == total_count:
      #   continue
      elif desired_number - total_count == 0:
        # print("FOUND IT!!!!")
        # print(list_of_numbers)
        return(list_of_numbers)
        break

list_of_numbers = find_list_of_numbers(all_numbers)
print(list_of_numbers)

print(min(list_of_numbers) + max(list_of_numbers))