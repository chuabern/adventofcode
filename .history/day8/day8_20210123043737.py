with open('day8_input.txt', 'r') as text:
    lines = text.read().split("\n")

accumulator = 0 # initialize accumulator value at 0
index = 0 # initialize index at 0
# for line in lines:
#   index += 1
#   action = line.split()[0]
#   value = line.split()[1]

#   if action == 'nop':
#     continue
#   elif action == 'acc':
#     accumulator += value
#   elif action == 'jmp':

total_length = len(lines)

tracking = []
for line in lines:
  tracking.append(
    {
      'id':line,
      'times_appeared':0
    }
  )

print(tracking)

# while index < total_length-1:
#   line = lines[index]
#   action = line.split()[0]
#   value = line.split()[1]

#   if action == 'nop':
#     continue
#   elif action == 'acc':
#     accumulator += value
#   elif action == 'jmp':


