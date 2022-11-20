a=[9,8,7,6,44,4,399,2,1]

def highestVal(arr):
  highest = 0
  for i in arr:
    if highest<i:
      highest = i
  return highest

print(highestVal(a))

print(max(a))