# weight convertor

weight = float(input("Enter the weight: "))
unit = input("Kilograms or Pounds(K or L): ").lower()


if  unit == "k":
    weight = weight * 2.205
    unit ="Lbs"

elif unit == "l":
    weight = weight / 2.205
    unit = "Kgs"

else:
    print(f"The {unit} isnt valid!")
print(f"Your weight is {round(weight, 3)} {unit}")