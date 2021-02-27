import os

BASE_ULR = os.getcwd()

for root, dirs, files in os.walk(BASE_ULR):
  # os.path.join
  print(root, dirs, files)


# os.makedirs('dir4/f1/f2/f3')

def create_dir(path):
  if not os.path.exists(path):
    os.mkdir(path)

def safe_rename(src: str, dst: str):
  if os.path.exists(src):
    os.rename(src, dst)
  
def safe_rmdir(path: str):
  if os.path.exists(path):
    os.rmdir(path)


# os.rename('file1.txt', 'file1_changed.txt')
# os.rename('dir4', 'dir4_changed')

safe_rename('file1.txt', 'file1_changed.txt')
safe_rename('dir4', 'dir4_changed')


# create_dir('dir5')
safe_rmdir('dir5')
