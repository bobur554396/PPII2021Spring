"""
4
3 5 4 2
"""
n = int(input())
# print(type(n))
nums = input().split()
# print(type(nums[0]))
s = 0
for i in nums:
  s += int(i)

print(s)
