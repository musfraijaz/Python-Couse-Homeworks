
talents = int(input("Enter talents (leiviskä): "))
pounds = int(input("Enter pounds (naula): "))
lots = int(input("Enter lots (luoti): "))

total_lots = talents * 20 * 32 + pounds * 32 + lots


grams = total_lots * 13.3

kilograms = int(grams // 1000)
remaining_grams = grams % 1000

print(f"The mass is {kilograms} kilograms and {remaining_grams:.2f} grams.")