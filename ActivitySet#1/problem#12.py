filename = "dataset/mbox-short.txt"
fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
senders1 = list()
senders = dict()
for line in fh:
    line = line.split()
    if len(line) < 3 or line[0] != 'From':
        continue
    senders1.append(line[1])

for sender in senders1:
    senders[sender] = senders.get(sender, 0) + 1

maximum = None
theone = None
for sender, count in senders.items():
    if maximum is None or count > maximum:
        maximum = count
        theone = sender

print(theone, maximum)