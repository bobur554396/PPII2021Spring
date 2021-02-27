import os


def create_dir(path):
  if not os.path.exists(path):
    os.mkdir(path)

create_dir('dir3')

BASE_ULR = os.getcwd()
# print(type(BASE_ULR))

# os.chdir('dir1')
# create_dir('dir1_1')

# print(os.listdir('.'))
for target in os.listdir('.'):
  # target_path = BASE_ULR + '/' + target -- not recommended
  target_path = os.path.join(BASE_ULR, target)
  if os.path.isfile(target_path):
    print(f'FILE: {target_path}')
  if os.path.isdir(target_path):
    print(f'DIR: {target_path}')
    for t in os.listdir(target_path):
      t_path = os.path.join(BASE_ULR, target, t)
      if os.path.isfile(t_path):
        print(f"{' '*5}FILE: {t_path}")
      if os.path.isdir(t_path):
        print(f"{' '*5}DIR: {t_path}")
