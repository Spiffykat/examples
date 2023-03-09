#Measure-Command {start-process python -ArgumentList (".\findv1.py", "file.txt", 100) -Wait}
#10.177.227.68


import os
import re

def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in dirs:
            result.append(os.path.join(root,name))
    return result
    
default_path = "C:\\"

i = find_all("crd", default_path)
print (index)
v = "9834"
r = re.compile(r".*"v)
focus = list(filter(r.match, i))
 
#focus = re.findall(r'*9834*', index)

print(focus)


'''
test 1. Find the STR
>>> r = re.compile("b")
>>> b = list(filter(r.match, stuff))
>>> print(b)

test2 Find mutable STR
>>> v = "9834"
>>> r1 = ".*" + re.escape(v)
>>> r = re.compile(r1)
>>> focus = list(filter(r.match, i))
>>> print(focus)
['C:\\Users\\v-mbranche\\Documents\\skuqual\\983439BE_1057101FE\\crd']


test3 Change Directory based off focus
os.chdir(focus[0])
os.getcwd()
os.listdir()


'''