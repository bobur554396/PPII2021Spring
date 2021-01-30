# palindrome?
# aba abba - YES
# abb aabc - NO
line = input()

new_line = ''.join(reversed(line)) # split(',')

if line == new_line:
  print('YES')
else:
  print('NO')

