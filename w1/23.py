nums = [int(i) for i in input().split()]

i, s = 0, 0

while i < len(nums):
  if nums[i] % 2 != 0:
    s += nums[i]

  i += 1

print(s)

