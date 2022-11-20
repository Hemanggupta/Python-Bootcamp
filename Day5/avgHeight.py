
a= [175, 124,156,154,134,122,132,133]
def avg_height(arr):
  num = 0
  count = 0
  for height in arr:
    num += height
    count+=1
  averageHeight= num/count
  return averageHeight

avg=avg_height(a)
print(round(avg,2)) #Math module not needed

def smart_python(arr):
  total = sum(arr)
  length = len(arr)
  return total/length

print(round(smart_python(a)))