largest = None
smallest = None
l1=list()
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num1=int(num)
    except:
        print("Invalid input")
    l1.append(num1)
largest=max(l1)
smallest=min(l1)
print("Maximum is",largest)
print("Minimum is",smallest)