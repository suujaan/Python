weight = int(input("Enter Your weight: "))
unit = input("Enter (L)bs or (k)g: ")
converted = weight * 0.45
if  unit.upper() == "L":
    print(f"You are {int(converted) * float(0.45)} kilos")
else:
    print( f"You are {int(converted) / float(0.45)} pounds")
