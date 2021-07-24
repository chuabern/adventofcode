import copy
with open('day11_input.txt', 'r') as text:
    lines = text.read().split("\n")
# part 1

def split(word):
    return [char for char in word]

for line in range(0,len(lines)):
  lines[line] = split(lines[line])


### Initial logistics
#Counting the number of seats

total_no_of_seats=0
seat_locations = []

for row in range(0,len(lines)):
  for seat in range(0,len(lines[row])):
    if lines[row][seat] == 'L':
      seat_locations.append([row, seat])
      total_no_of_seats += 1

#Get the number of rows and columns
number_of_rows = len(lines)
number_of_columns = len(lines[0])


def find_beside_seats(lines, row, seat):
  adjacent_seats = []
  for i in [-1,0,1]:
    for j in [-1,0,1]:
      if i == 0 and j == 0:
        continue
      elif row+i >= 0 and seat+j >= 0:
        try:
          adjacent_seats.append(lines[row+i][seat+j])
        except:
          "no adjacent seat found for this placement"
  return adjacent_seats

def occupy_seat(lines):
  no_change_count = 0
  new_lines = copy.deepcopy(lines)
  for individual_seat in seat_locations:
    # print(individual_seat)
    row = individual_seat[0]
    seat = individual_seat[1]
    # print(individual_seat)
    adjacent_seats = find_beside_seats(lines, row, seat)

    if lines[row][seat] == 'L' and '#' not in adjacent_seats:
      # print("There are no occupied seats adjacent")
      become_occupied = True # becomes occupied
      # print(new_lines[row][seat])
      new_lines[row][seat] = '#'
    elif lines[row][seat] == '#' and adjacent_seats.count('#') >= 4:
      # print("There are four or more seats adjacent that are occupied")
      new_lines[row][seat] = 'L'
      become_empty = True
    else:
      no_change_count += 1
  return new_lines, no_change_count

no_change_count = 0

while no_change_count != total_no_of_seats:
  lines, no_change_count = occupy_seat(lines)

total_no_of_occupied_seats = 0
for row in range(0,len(lines)):
  for seat in range(0,len(lines[row])):
    if lines[row][seat] == '#':
      seat_locations.append([row, seat])
      total_no_of_occupied_seats += 1

# print(lines)
print(total_no_of_occupied_seats)

# This was so tough I died at part 1

# #diagonal seats are counted
# def corner_seat(row, seat):
#   if row in [0, number_of_rows-1] and seat in [0, number_of_rows-1]:
#     return True
#   else:
#     return False 

# def occupy_corner_seat(row, seat):
#   if row == 0:
#     if seat == 0: #Top left
#       adjacent_seats = [
#         [0,1],
#         [1,0],
#         [1,1]
#       ]
#     elif seat == number_of_columns - 1: #Top right
#       adjacent_seats = [
#         [0, number_of_columns - 2],
#         [1, number_of_columns - 2],
#         [1, number_of_columns - 1]
#       ]
#   else:
#     if seat == 0: #Bottom left
#       adjacent_seats = [
#         [number_of_rows - 2, 0],
#         [number_of_rows - 2, 1],
#         [number_of_rows - 1, 1]
#       ]
#     elif seat == number_of_columns - 1: #Bottom right
#       adjacent_seats = [
#         [number_of_rows - 1, number_of_columns - 2],
#         [number_of_rows - 2, number_of_columns - 2],
#         [number_of_rows - 2, number_of_columns - 1]
#       ]
#   return adjacent_seats



# adjacent_seats = []
# row = 1
# seat = 0
# adjacent_seats = (find_beside_seats(lines, row, seat))

# print(adjacent_seats)

# def side_seat(row, seat):
#   if row in [0, number_of_rows-1] or seat in [0, number_of_columns-1]:
#     return True
#   else:
#     return False

# def check_adjacent_seats(adjacent_seats):
#   beside_seats = []
#   for each_seat in adjacent_seats:
#     each_seat = lines[each_seat[0]][each_seat[1]]
#     beside_seats.append(each_seat)

#   become_occupied = False
#   become_empty = False
#   no_change = False

#   if '#' not in beside_seats:
#     # print("There are no occupied seats adjacent")
#     become_occupied = True # becomes occupied
#   elif beside_seats.count('#') >= 4:
#     # print("There are four or more seats adjacent that are occupied")
#     become_empty = True
#   else:
#     no_change = True

#   return become_occupied, become_empty, no_change

# def change_seats(lines, row, seat, become_occupied, become_empty):
#   if become_occupied:
#     lines[row][seat] = '#'
#   if become_empty:
#     lines[row][seat] = 'L'

# def occupy_seat(total_checker):
#   for row in range(0, len(lines)):
#     for seat in range(0, len(lines[row])):
#       if corner_seat(row, seat) is True:
#         print("This is a corner seat")
#         adjacent_seats = occupy_corner_seat(row, seat)
#         become_occupied, become_empty, no_change = check_adjacent_seats(adjacent_seats)
#         change_seats(lines, row, seat, become_occupied, become_empty)
#         # Check the number of changes left
#         # if 0, thats the end
#         if no_change is True:
#           total_checker += 1
#       elif side_seat(row, seat) is True:
#         print("This is a side seat")
#   return total_checker

# total_checker = 0
# # total_checker = occupy_seat(total_checker)
# # print(lines)
# # print(total_checker)

