# anagram?
# hello loehl - YES
# hello lohll - NO

# Python collections: List, Tuple, Set, Dictionary
line1, line2 = input().split()

# Part solution (duplicated chars not true)
# if set(line1) == set(line2):
#   print('yes')
# else:
#   print('no')

# a = [5, 3, 7]
# a.sort()
# print(a)

print('YES') if sorted(line1) == sorted(line2) else print('NO')
