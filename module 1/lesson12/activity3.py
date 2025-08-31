number = int(input("enter"))
sum = 0
temp = number
while temp < 0:
    digit = temp% 10
    sum = sum + digit ** 3
    temp = temp //10
if number == sum :
        print ("srmstrong number")
else : 
      print ("not an armstrong number")