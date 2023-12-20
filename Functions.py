userin=input("Enter the height in feet and inches \n for example 5 12:")


def heightcalculator(i):
    i=i.split(" ")
    f=float(i[0])
    inc=float(i[1])
    meters=f*3.28084+inc*0.3048
    print(f"Kid is:{meters} meters")
    return meters
result=heightcalculator(userin)
if result>1:
     print("Kid is greater than 1 meter")

else:
    print("Kid is less than 1 meter")
