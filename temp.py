unit = input("Enter the Temp in Celsius or Fahrenheit( C or F): ").lower()
temp = float(input("Enter the Temperature: "))

if  unit == "c":
    temp = ((9 * temp)/ 5 + 32)
    print(f"The Temp in Fahrenheit is: {temp}°F ")
elif unit == "f":
    temp = (( temp- 32)* 5/9 )
    print(f"The Temp in Celsius is: {round(temp,2)}°C ")
else:
    print(f"{unit} is not available: ")