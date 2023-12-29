userin=input("Enter the height in feet and inches \n for example 5 12:")

def parse_height(par_height):
    par_height=par_height.split(" ")
    foot=float(par_height[0])
    inches=float(par_height[1])
    return {"foot":foot,"inches":inches}

def convert(foot, inches):
    meters = foot * 3.28084 + inches * 0.3048
    return meters

parsed=parse_height(userin)
print(parsed)

result=convert(parsed['foot'], parsed['inches'])

print(f"{parsed['foot']} foot and {parsed['inches']} inches equals to {result}meters")


