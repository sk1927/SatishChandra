try:
    a=float(input("enter a lengenth:"))
    b=float(input("enter a breadth:"))
    if a==b:
        exit("Looks like a square! Please try again")
    area=a*b
    print(area)
except ValueError:
    print("Please enter a number please!")