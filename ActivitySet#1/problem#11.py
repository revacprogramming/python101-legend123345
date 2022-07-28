filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lst1=list()
a=""
for line in fh:
    a=line.split()
    lst+=a
    for i in lst:
        if i not in lst1:
            lst1.append(i)
        else:
            continue
lst1.sort()
print(lst1)
#8.5
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if line.startswith("From") and "From:" not in line:
        text = line
        c=text.split()
        ext=c[1]
        ext1=ext.strip()
        print(ext1)
        count+=1

print("There were", count, "lines in the file with From as the first word"