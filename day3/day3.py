with open("day3_input.txt", "r") as f:
    map = list(f.read().split('\n'))


def find_position_a(map):
    previous_position = 0
    trees = 0 
    for row in range(1,len(map)):
        length = len(map[row])
        previous_position += 3
        next_position = previous_position

        if next_position > length-1:
            next_position = next_position - length

        thing = map[row][next_position]

        previous_position = next_position
        
        if thing == '#':
            trees += 1
    print(trees)

# find_position_a(map)

def find_position_a(map):
    previous_position = 0
    trees = 0 
    for row in range(1,len(map)):
        length = len(map[row])
        previous_position += 3
        next_position = previous_position

        if next_position > length-1:
            next_position = next_position - length

        thing = map[row][next_position]

        previous_position = next_position
        
        if thing == '#':
            trees += 1
    print(trees)

def multiple_slopes(map, right, down):
    horizontal_position = 0 # initial position
    vertical_position = 0 # initial position
    trees = 0 # initial position
    length = len(map[vertical_position])
    for row in range(1,len(map)):
        vertical_position += down
        horizontal_position += right
        if horizontal_position > length-1: #Check if the horizontal position is greater than the # of objects in the row, if yes start over 
            horizontal_position -= length
        if vertical_position > len(map): #Check if the vertical position exceeds number of rows
            break
        thing = map[vertical_position][horizontal_position]
        if thing == '#':
            trees += 1
    print("The number of trees encountered when going right {}, down {} is {}".format(right,down,trees))   
    return trees

print(multiple_slopes(map,1,1) * multiple_slopes(map,3,1) * multiple_slopes(map,5,1)  *multiple_slopes(map,7,1) * multiple_slopes(map,1,2))