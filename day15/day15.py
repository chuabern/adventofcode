puzzle = [16,11,15,0,1,7]
# puzzle = [0,3,6]

all_numbers_spoken = {}


# Part one
for i in range(1, 2021):
  # print(f'i = {i}')
  # print('record so far:' ,all_numbers_spoken)
  if i < len(puzzle) + 1: # initialize starting numbers
    all_numbers_spoken[i] = puzzle[i - 1] #number of turn = number spoken
  else:
    # print(f'last number spoken: {all_numbers_spoken[i-1]}')
    placeholder_dict = all_numbers_spoken.copy()
    del placeholder_dict[i-1]
    if all_numbers_spoken[i-1] not in list(placeholder_dict.values()):
      all_numbers_spoken[i] = 0
      # print(f"Number to be saved = 0 as {all_numbers_spoken[i-1]} has never appeared before")
    else:
      # figure out most recent appeared
      # placeholder_dict = all_numbers_spoken.copy()
      # del placeholder_dict[i-1]
      flipped_dict = dict(sorted(placeholder_dict.items(), reverse = True))
      for j, k in flipped_dict.items():
        if k == all_numbers_spoken[i-1]:
          all_numbers_spoken[i] = (i-1) - j
          # print(f"Number to be saved = Turn # {i-1} - earlier turn # {j}")
          break
  # print(f'saved record: {all_numbers_spoken}')
  # print('\n')


print(all_numbers_spoken[2020])

for i in range(1, 30000001):
  # print(f'i = {i}')
  # print('record so far:' ,all_numbers_spoken)
  if i < len(puzzle) + 1: # initialize starting numbers
    all_numbers_spoken[i] = puzzle[i - 1] #number of turn = number spoken
  else:
    # print(f'last number spoken: {all_numbers_spoken[i-1]}')
    placeholder_dict = all_numbers_spoken.copy()
    del placeholder_dict[i-1]
    if all_numbers_spoken[i-1] not in list(placeholder_dict.values()):
      all_numbers_spoken[i] = 0
      # print(f"Number to be saved = 0 as {all_numbers_spoken[i-1]} has never appeared before")
    else:
      # figure out most recent appeared
      # placeholder_dict = all_numbers_spoken.copy()
      # del placeholder_dict[i-1]
      flipped_dict = dict(sorted(placeholder_dict.items(), reverse = True))
      for j, k in flipped_dict.items():
        if k == all_numbers_spoken[i-1]:
          all_numbers_spoken[i] = (i-1) - j
          # print(f"Number to be saved = Turn # {i-1} - earlier turn # {j}")
          break
  # print(f'saved record: {all_numbers_spoken}')
  # print('\n')

print(all_numbers_spoken[30000000])
