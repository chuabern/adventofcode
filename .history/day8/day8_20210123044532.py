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

print(tracking[0])


while index < total_length-1:
  line = lines[index]
  action = line.split()[0]
  print(action)
  value = int(line.split()[1])
  print(value)
  tracking[index]['times_appeared'] += 1

  if tracking[index]['times_appeared'] == 2:
    print("BREAK LOOP!")
    break

  if action == 'nop':
    continue
  elif action == 'acc':
    accumulator += value
  elif action == 'jmp':
    index += value
    continue

  index += 1

print(accumulator)



