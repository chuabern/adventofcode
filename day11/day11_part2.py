import copy
with open('day11_input.txt', 'r') as text:
    lines = text.read().split("\n")
# part 1

def split(word):
    return [char for char in word]

for line in range(0,len(lines)):
  lines[line] = split(lines[line])

total_no_of_seats=0
seat_locations = []

# for row in range(0,len(lines)):
#   for seat in range(0,len(lines[row])):
#     if lines[row][seat] == '#':
#       seat_locations.append([row, seat])
#       total_no_of_occupied_seats += 1

for row in range(0,len(lines)):
  for seat in range(0,len(lines[row])):
    if lines[row][seat] == 'L':
      seat_locations.append([row, seat])
      total_no_of_seats += 1

#Get the number of rows and columns
number_of_rows = len(lines)
number_of_columns = len(lines[0])

##### PART TWO
total_no_of_seats
# print(seat_locations)

directions = {
  "North": [-1,0],
  "Northwest": [-1,-1],
  "Northeast": [-1,1],
  "East": [0,1],
  "Southeast": [1,1],
  "South": [1,0],
  "Southwest": [1,-1],
  "West": [0,-1]
}

def seat_lookup(row, seat, directions):
  continue_flag = True
  match = 0
  seats_within_line_of_vision = []

  for direction, movement in directions.items():
    row2 = copy.copy(row)
    seat2 = copy.copy(seat)
    continue_flag = True
    # print('hereeeee1')
    while row2 >= 0 and row2 <= number_of_rows and seat2 >= 0 and seat2 <= number_of_columns and continue_flag == True:
      # print(row2)
      # print(seat2)
      # print('New location:', [row2 + movement[0], seat2 + movement[1]])
      if [row2 + movement[0], seat2 + movement[1]] in seat_locations:
        # print(f"Match for {[row2 + movement[0], seat2 + movement[1]]}")
        
        seats_within_line_of_vision.append(lines[row2 + movement[0]][seat2 + movement[1]])
        # print(f"This corresponds to a {lines[row2 + movement[0]][seat2 + movement[1]]}")
        continue_flag = False
        break
      row2 += movement[0]
      seat2 += movement[1]
  # print(seats_within_line_of_vision)
  return seats_within_line_of_vision


def first_visible_seats(lines, row, seat):
  seats_within_line_of_vision = seat_lookup(row, seat, directions)
  new_lines = copy.deepcopy(lines)
  no_change_count = 0
  # for seats in range(0,len(seats_within_line_of_vision)):
  #   seats_within_line_of_vision[seats] = lines[seats][seats_within_line_of_vision[seats][1]]

  return seats_within_line_of_vision

# print(first_visible_seats(lines, 0, 0))

def occupy_seat_two(lines):
  no_change_count = 0
  new_lines2 = copy.deepcopy(lines)
  # print('hereeeeeeeee')
  for individual_seat in seat_locations:
    # print(individual_seat)
    row = individual_seat[0]
    seat = individual_seat[1]

    seats_within_line_of_vision = first_visible_seats(lines, row, seat)

    if lines[row][seat] == 'L' and '#' not in seats_within_line_of_vision:
      # print('2222here')
      # print("There are no occupied seats visible")
      become_occupied = True # becomes occupied
      # print(new_lines2[row][seat])
      new_lines2[row][seat] = '#'
    elif lines[row][seat] == '#' and seats_within_line_of_vision.count('#') >= 5:
      # print("There are four or more seats adjacent that are occupied")
      new_lines2[row][seat] = 'L'
      become_empty = True
    else:
      no_change_count += 1
  return new_lines2, no_change_count

for individual_seat in seat_locations:
  row = individual_seat[0]
  seat = individual_seat[1]
# occupy_seat_two(lines)

no_change_count = 0
# new_lines2, no_change_count = occupy_seat_two(lines)
while no_change_count != total_no_of_seats:
  print(no_change_count)
  print('here1111')
  lines, no_change_count = occupy_seat_two(lines)

total_no_of_occupied_seats = 0
for row in range(0,len(lines)):
  for seat in range(0,len(lines[row])):
    if lines[row][seat] == '#':
      seat_locations.append([row, seat])
      total_no_of_occupied_seats += 1

# print(lines)
print(total_no_of_occupied_seats)

### RUN TIME IS TOO LONG