import re

# ff = open('in.txt', 'r')
# t = ff.read()
# ff.close()

with open('in.txt', 'r') as f:
  text = f.read()

'''
# Examples from text:
  - \w+stan ----> Kazakhstan   ---  Kyrgyzstan  ---- Uzbekistan
  - \d{2}\.\d{2}\.\d{2,4} ----> Selecting Date with format:  20.02.2021 
  - \d{2}:\d{2}:\d{2} ----->  Selecting time with format: 14:56:10
  - (\+7|8)\(?\d{3}\)?-?\d{3}-\d{2}-\d{2} ---> +7707-123-11-22  ----- +7(707)123-11-22 ---- 8(707)123-11-22
  - [a-z]+@[a-z]+\.[a-z]{2,5}   --->   asd@gmail.com
  - [a-z0-9_]+@[a-z]+\.[a-z]{2,5} --->  asd3_asd@gmail.com
  - [A-Za-z0-9_]+\.?[A-Za-z0-9_]+@[a-z]+\.[a-z]{2,4}  --->  bobur.mukhsimbaev@kbtu.kz
  - [\w]+\.?[\w]+@[\w]+\.[\w]{2,4}  ---> bobur.mukhsimbaev@kbtu.kz
  - \[\w+\] ---> [apple],[four],[4],[13123]
  - \d+(,\d{3})+ --->  22,724,900     ----     110,052,100
  - \d+\.\d{1,}  ---> 18.81131
'''

# [A-Za-z0-9_]  <==> \w
# \d{1,}   <==> \d+
# \d{0,}   <==> \d*
# \d{0,1}   <==> \d?


email_pattern = re.compile(r'[\w]+\.?[\w]+@[\w]+\.[\w]{2,4}')



res = email_pattern.findall(text)
# print(res[1][0])

with open('out.txt', 'w') as file:
  for r in res:
    file.write(f'{str(r)}\n')



