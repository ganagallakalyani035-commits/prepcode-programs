def area (r,h):
    return 2*3.14*r*(r+h)
def volume (r,h):
    return 3.14*r*r*h
r=int(input("Enter radius:"))
h=int(input("Enter height:"))
print("Area =", area (r,h))
print("Volume=",volume(r,h))