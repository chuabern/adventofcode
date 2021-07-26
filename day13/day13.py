with open('day13_input.txt', 'r') as text:
    lines = text.read().split("\n")

earliest_timestamp = int(lines[0])

bus_list = lines[1]
bus_list = bus_list.split(",")
all_buses = []

for buses in bus_list:
  if buses != 'x':
    all_buses.append(int(buses))


# create the bus schedule
buses_running = {}
for buses in bus_list:
  if buses != 'x':
    buses_running[buses] = []
    count = 1
    while int(buses)*count < earliest_timestamp + max(all_buses): # the loop will stop at the longest running bus
      buses_running[buses].append(int(buses) * count)
      count += 1

# print(buses_running)
# print(bus_list)

# find out the earliest bus
earliest_bus = 0

earliest_timing_for_each_bus = {}

for buses, timings in buses_running.items():
  for individual_timing in timings:
    if earliest_timestamp - individual_timing < 0:
      # print(individual_timing)
      # print(buses)
      earliest_timing_for_each_bus[buses] = individual_timing
      break

# print(min(earliest_timing_for_each_bus.items(), key = lambda x: x[1])[1])

# answer = (min(earliest_timing_for_each_bus.items(), key = lambda x: x[1])[1] - earliest_timestamp) * int(min(earliest_timing_for_each_bus.items(), key = lambda x: x[1])[0])
# print(answer)



## Part Two
# print(bus_list)
indexed_bus_list = []
for i in enumerate(bus_list):
  if i[1] != 'x':
    indexed_bus_list.append(i)

# print(indexed_bus_list)

did_the_bus_match = {}
for bus in indexed_bus_list:
  did_the_bus_match[bus[1]] = 0
counter = round(783685719679632/23)
# print(counter)
while counter > 0:
  did_the_bus_match2 = did_the_bus_match.copy()
  first_bus_timestamp = int(indexed_bus_list[0][1]) * counter
  did_the_bus_match2[indexed_bus_list[0][1]] = 1
  # print(f'first bus timetamp is {first_bus_timestamp}')
  for next_bus in indexed_bus_list[1:]:
    next_bus_timestamp = int(first_bus_timestamp + int(next_bus[0])) # find the timestamp of the next bus
    # print(f'next bus timestamp is {next_bus_timestamp}')
    if next_bus_timestamp % int(next_bus[1]) == 0:
      did_the_bus_match2[next_bus[1]] = 1
      # print(first_bus_timestamp)
  # print(did_the_bus_match2)
  # print(sum(did_the_bus_match2.values()))
  if sum(did_the_bus_match2.values()) == len(indexed_bus_list):
    print(f'Found a match for earliest timestamp {first_bus_timestamp}')
    break
  counter += 1

# print(did_the_bus_match)
# print(did_the_bus_match2)
# print(sum(did_the_bus_match2.values()))
# print(indexed_bus_list)

