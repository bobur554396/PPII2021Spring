# JSON -> JavaScript Object Notation
import json

a = {
  'id': '20BD1212',
  'name': 'Student 1',
  'age': 20
}
b = json.dumps(a) # serializing dict to str

print(type(b))
print(b)

c = json.loads(b)  # deserializing str back to dicts
print(a == c)
print(type(c))
print(c['age'])
print(c['name'])
