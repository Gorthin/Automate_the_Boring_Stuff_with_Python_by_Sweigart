#! python3

import os, re, shutil

dir = 'D:/1_PYTHON_PROJEKTY/Sweigart_tasks'

seq = re.compile(r'^(spam)(\d+)(.txt)')

lst = []
for file in os.listdir(dir):
    num = seq.search(file).group(2)
    lst.append( (int(num.lstrip('0')), file, len(num)) )

lst = sorted(lst)
for index in range(len(lst)):
    padding = lst[index][2]
    num = str(int(index) + 1)
    padded_num = num.rjust(padding, '0')
    src = os.path.join(dir, lst[index][1])
    dst = os.path.join(dir, seq.sub(r'\g<1>%s\g<3>' % padded_num, lst[index][1]))
    shutil.move(src, dst)