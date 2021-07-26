
from operator import add, mul
with open('day12_input.txt', 'r') as text:
    lines = text.read().split("\n")

# Part 1 


current_position = [0,0] # [North/South , East/West]
# initial_direction = {
#   'N': 0,
#   'S': 0,
#   'E': 0,
#   'W': 0
# }

direction_movements = {
  'N': [1,0],
  'S': [-1,0],
  'E': [0,1],
  'W': [0,-1]
}

direction_bearings = {
  'N': 0,
  'S': 180,
  'E': 90,
  'W': 270
}

# Set initial direction to be East
# initial_direction['E'] = 1

def determine_current_direction(current_direction):
  for direction, value in current_direction.items():
    if value == 1:
      return direction # NSEW

def determine_direction_from_degrees(direction_bearings, old_direction, degree_change):
  # print(degree_change)
  # print(old_direction)
  for direction, degree in direction_bearings.items():
    if direction == old_direction:
      new_degree = direction_bearings[direction] + degree_change
      # print(f"New degree: {new_degree}")
      if new_degree == 360: #This part should be done less manually
        new_degree = 0
      elif new_degree == 450 or new_degree == - 270:
        new_degree = 90
      elif new_degree == 540 or new_degree == - 180:
        new_degree = 180
      elif new_degree == 630 or new_degree == -90:
        new_degree = 270
      for direction, degree in direction_bearings.items():
        if new_degree == degree:
          # print(f"New direction: {direction}")
          return direction

def move_values(current_position, direction_movements, direction):
  current_position = list(
      map(
        add,
        current_position,
        [i * int(action[1:]) for i in direction_movements[direction]]
      )
    )
  return current_position

# direction = determine_current_direction(initial_direction)
direction = 'E'

for action in lines:
  # print(direction)
  if action[0] == 'F':
    current_position = move_values(current_position, direction_movements, direction)
  elif action[0] in direction_movements:
    current_position = move_values(current_position, direction_movements, action[0])
  elif action[0] in ['R', 'L']:
    degree_change = int(action[1:])
    # print(f"Original Direction: {direction}")
    # print(action[0])
    # print(f"Degree Change: {-degree_change}")
    if action[0] == 'R':      
      direction = determine_direction_from_degrees(direction_bearings, direction, degree_change)
      # print(direction)
    elif action[0] == 'L':
      direction = determine_direction_from_degrees(direction_bearings, direction, -degree_change)
    # print(direction)
    # print('\n')
  # print(current_position)

# print(current_position)
# print(abs(current_position[0]) + abs(current_position[1]))

# Part 2
ship_position = [0,0]
waypoint_position = [1,10]

print(f"Initial ship position:" , ship_position)
def rotate_waypoint(waypoint_position, degree, direction):
  how_to_flip = {
    'L': {
      90: [waypoint_position[1], -waypoint_position[0]],
      180: [-waypoint_position[0], -waypoint_position[1]],
      270: [-waypoint_position[1], waypoint_position[0]],
    },
    'R': {
      90: [-waypoint_position[1], waypoint_position[0]],
      180: [-waypoint_position[0], -waypoint_position[1]],
      270: [waypoint_position[1], -waypoint_position[0]]
    }
  }
  waypoint_position = how_to_flip[direction][degree]
  return waypoint_position

for action in lines:
  if action[0] == 'F': # Move the ship
    ship_position = list(map(add, ship_position, list(map(mul, waypoint_position, [int(action[1:]), int(action[1:])]))))
    # print('\n')
  elif action[0] in direction_movements: # Move the waypoint only
    # print(action[0])
    # print(direction_movements)
    waypoint_position = move_values(waypoint_position, direction_movements, action[0])
  elif action[0] in ['R', 'L']:
    degree_change = int(action[1:])
    waypoint_position = rotate_waypoint(waypoint_position, degree_change, action[0])
  # print('ship_position', ship_position)
  # print('waypoint_position', waypoint_position)
  # print('\n')

print(ship_position)
print(abs(ship_position[0]) + abs(ship_position[1]))