def computepay(h, r):
  if h<=40 and h>=0:
    p=h*r
  if h>40:
    h1=h-40
    r1=1.5*r
    p1=h1*r1
    p=40*r+p1
  return p
hrs = float(input("Enter hours: "))
rte = float(input("Enter rate per hour: "))
pay = computepay(hrs, rte)
print("Pay", pay)