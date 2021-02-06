student = {
    'ID': '20BD123123',
    'name': 'Student name',
    'gpa': 4.0,
    'year_of_sudy': 2
}


print(student['ID'])

student['gpa'] = 3.9

student['faculty'] = 'FIT'

print(student)
print(len(student))
print('-'*100)

# for i in student:
#   print(i)

# for i in student.keys():
#   print(i)

# for i in student.values():
#   print(i)

# for key, val in student.items():
#   print(f'{key} => {val}')

print('ID' in student)

student.pop('ID')
del student['gpa']
print(student)

