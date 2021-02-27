import os
import shutil

# shutil.rmtree('dir2')

shutil.copy('dir3/2.txt', 'dir1/dir1_1/2.txt')
# shutil.copytree('dir3', 'dir33')


# shutil.move('dir33/2.txt', 'dir1/2.txt')
shutil.move('dir1/dir1_1', 'dir33/')
