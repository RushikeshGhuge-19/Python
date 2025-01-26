# compound interest program

principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter the principle amount: "))
    if  principle <=0:
        print("Principle cant be less or equal to 0!")

while rate <=0:
    rate = float(input("Enter the Interest Rate: "))
    if  rate <=0:
        print("Interest Rate cant be 0 or less then 0")

while time <=0:
    time = int(input("Enter the number of years: "))
    if  time <=0:
        print("Time cant be 0 or less then 0")

total = principle * pow((1+ rate / 100), time)
print(f"Balance after {time} is {total}")