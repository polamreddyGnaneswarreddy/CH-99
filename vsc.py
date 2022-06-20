import os

os.mkdir("Har")

os.getcwd()

path='\VNANESWAR\Python H\99\Har'

isExist=os.path.exists(path)
print(isExist)


import os
path='/usr/loacl/bin/file.txt'

isExist=os.path.exists(path)
print(isExist)
root_ext=os.path.splitext(path)


print("root part: ",root_ext[0])
print("extension part: ",root_ext[1])


os.listdir()