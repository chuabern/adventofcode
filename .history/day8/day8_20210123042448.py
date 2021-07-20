with open('day8_input.txt', 'r') as text:
    lines = text.read().split("\n")

accumulator = 0 # initialize accumulator value at 0
index = -1 # initialize index at -1
for line in lines:
  index += 1
  action = line.split()[0]
  value = line.split()[1]

  if action == 'nop':
    continue
  elif action == 'acc':
    accumulator += value
