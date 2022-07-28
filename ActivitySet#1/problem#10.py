filename = "dataset/mbox-short.txt"
# Use the file name mbox-short.txt as the file name
fname = input("Enter File Name: ")
fh = open(fname)
count=0
ext1=0
ext2=0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        text = line
        c=text.find(":")
        ext=text[c+1:]
        ext1=ext.strip()
        ext3=float(ext1)
        ext2+=ext3
        count+=1
print("Average spam confidence:",ext2/count)