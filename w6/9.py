l = [20, 18, 14, 25, 10]
# for i in l:
#   if i >= 18:
#     print(i)

def take_adult(age):
  return age >= 18

print(list(filter(take_adult, l)))


def my_filter(func, iterable):
  for item in iterable:
    if func(item):
      yield item

print(list(my_filter(take_adult, l)))
