
length = float(input("Enter the length of the zander in cm: "))


limit = 42


if length < limit:
    difference = limit - length
    print("Release the fish back into the lake.")
    print(f"The fish is {difference:.1f} cm below the legal size.")
else:
    print("You can keep the fish.")