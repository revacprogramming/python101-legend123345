w=int(input("Enter 1 for Gross Pay\nEnter 2 for Grade \n"))
if(w==1):
  
  hrs = input("Enter Hours:")
  hrs=float(hrs)
  rate=input("Enter Rate:")
  rate=float(rate)
  if hrs<=40 and hrs>=0:
      gpay=hrs*rate
  if hrs>40:
      hrs1=hrs-40
      rate1=1.5*rate
      gpay1=hrs1*rate1
      gpay=40*rate+gpay1
  else:
    print("Enter Valid Hours.")
  print(gpay)
#3.3
elif(w==2):
  score = float(input("Enter Score: "))
  if score>=0.9 and score<=1:
    grade="A"
  if score>=0.8 and score<0.9:
    grade="B"
  if score>=0.7 and score<0.8:
    grade="C"
  if score>=0.6 and score<0.7:
    grade="D"
  if score<0.6 and score>=0:
    grade="F"
  elif score<0 or score>1:
    print("Enter Valid Score.")
  print(grade)
else:
  print("Enter Valid Choice.")