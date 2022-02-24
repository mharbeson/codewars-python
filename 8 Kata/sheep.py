def count_sheeps(sheep):
  count = 0
  for item in range(len(sheep)):
    if sheep[item] == True:
      count += 1
    else:
      pass
  return count



array1 = [True,  True,  True,  False, True,  True,  True,  True , True,  False, True,  False, True,  False, False, True , True,  True,  True,  True , False, False, True, True ];

print(count_sheeps(array1))


