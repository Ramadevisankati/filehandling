f=open("file_list.txt")
l=[]
for line in f:
    f_l=line.strip()
    li=f_l.split()
    l.append(li)
print(l)