"""
3 5 4 2
"""
n = int(input())

nums = input().split()

if n != len(nums):
  print('error')
else:
  print('it is ok you can continue')

# print(input().split())

# s = 0
# for i in input().split():
#   s += int(i)

# print(sum([1, 2.4, 3]))

# print([int(i) for i in input().split()])

print(sum([int(i) for i in input().split()]))
