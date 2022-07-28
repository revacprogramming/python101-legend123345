filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = list()
counts = dict()
for line in handle:
    line = line.split()
    if len(line) < 3 or line[0] != 'From':
        continue
    time= line[5].split(':')
    hours.append(time[0])

for hour in hours:
    counts[hour] = counts.get(hour, 0) + 1

lst = sorted([(k,v) for k,v in counts.items()])

for k,v in lst:
    print(k,v)