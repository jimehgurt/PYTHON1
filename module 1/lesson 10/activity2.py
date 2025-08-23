print ("select your ride")
print ("2 : car")
print (" 1 : bike")
choice = int(input("choose what ride u want 1 or 2 : "))
if choice == 1:
    print ("what type of bike")
    print ("1 : scooter")
    print ("2 : scooty")
    choice2 = int(input("choose your bike"))
    if choice2 == 1 :
        print("you chose a scooter")
    else :
        print ("you chose a scooty")
elif choice==2 :
    print ("what type of car")
    print ("1 : sedan")
    print ("2 : xuv")
    choice3 = int(input("choose your car"))
    if choice3 == 1 :
        print("you chose a sedan")
    else :
        print ("you chose a xuv")
else :
    print ("wrong chocie")
