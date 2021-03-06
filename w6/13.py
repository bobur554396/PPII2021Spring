# l = [2, 40, 5, 10]
# print(sorted(l, reverse=True))

a = [
  {'id': 1, 'name': 'Stundet 1', 'age': 20},
  {'id': 3, 'name': 'Stundet 3', 'age': 18},
  {'id': 5, 'name': 'Stundet 5', 'age': 22},
  {'id': 4, 'name': 'Stundet 4', 'age': 21},
]

def kk(obj):
  return obj['age']

# sorted_a = sorted(a, key=kk, reverse=True)

sorted_a = sorted(a, key=lambda x: x['age'], reverse=True)
for i in sorted_a:
  print(i)
