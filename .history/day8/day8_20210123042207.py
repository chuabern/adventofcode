with open('day8_input.txt', 'r') as text:
    lines = text.read().split("\n")

accumulator = 0 # initialize accumulator value at 0

for line in lines:
  print(line[0-2:])
