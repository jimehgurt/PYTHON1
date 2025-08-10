a = float(input("whats your weight in kg?"))
b = float(input("whats your height in meters?"))
bmi = a/b*b
if bmi <= 18.5 :
    print ("your under weight")
elif bmi <= 24.9 :
    print ("your normal weight")
elif bmi <= 29.9 :
    print ("your over weight")
elif bmi <= 34.9 :
    print ("your obese")
else :
    print ("your extremly obese")