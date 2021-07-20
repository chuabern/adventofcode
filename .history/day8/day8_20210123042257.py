with open('day8_input.txt', 'r') as text:
    lines = text.read().split("\n")

accumulator = 0 # initialize accumulator value at 0

for line in lines:
  action = line.split()[0]
  value = line.split()[1]
