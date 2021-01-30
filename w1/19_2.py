# palindrome?
# aba abba - YES
# abb aabc - NO
line = input()

# if line == line[::-1]:
#   print('YES')
# else:
#   print('NO')

print('YES') if line == line[::-1] else print('NO')
# cout << 2 == 2 ? YES : NO