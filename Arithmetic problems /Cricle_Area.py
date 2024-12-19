r = int(input("Enter the radius of the circle \n"))


def area():
    return 3.1415 * pow(r,2)

print(f"The area of the circle with radius {r} is {area():.3f}")