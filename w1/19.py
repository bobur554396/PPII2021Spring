# palindrome?
# aba abba - YES
# abb aabc - NO
line = input()

ok = True
for i in range(int(len(line) / 2)):
  if line[i] != line[len(line) - i - 1]:
    ok = False

if ok:
  print('YES')
else:
  print('NO')
