weight = int(input())
grow = float(input())
c =weight/pow(grow,2)
if c<18.5:
    print("Underweight")
elif 25>c>=18.5:
    print("Normal") 
elif 30>c>=25:
    print("Overweight")
elif c>=30:
    print("Obesity")





