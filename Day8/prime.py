def is_prime(num):
  for i in range(2,num):
    if num%i==0:
      return "It's not a Prime Number"
  return "It's a Prime Number"

print(is_prime(9))