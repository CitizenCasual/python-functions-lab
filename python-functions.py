# Challenge 1
def sum_to(n):
  sum = 0
  for num in range(1, n + 1):
    sum += num
  return sum
print(sum_to(10))

# Challenge 2
def largest(lis):
  lis.sort()
  print(lis[-1])
print(largest([100, 4, 2, 23, 91,  54]))

# Challenge 3
def occurances(str1, str2):
  count = str1.count(str2)
  print(count)
print(occurances('fleep floop', 'ee'))

# Challenge 4
def product(*args):
  product = 1
  for arg in args:
    product = product * arg
  return product
print(product(4, 0.5, 5))