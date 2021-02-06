a = ['1', 'Hello', {}, [True, False]]
# for i in a:
#   print(i)

# for i, v in enumerate(a):
#   if i % 2 != 0:
#     print(f"{i} -- {v}")


# for i in range(len(a)): # (start, end, step)
#   print(a[i])

# i = 0
# while i < len(a):
#   print(a[i])
#   i += 1

# [print(i) for i in a] # ["expression" for "iterator" in "some iterable object"]

# [print(i) for i in range(0, 20) if i % 2 == 0]
[print(i) if i % 2 == 0 else print('*') for i in range(20)]
