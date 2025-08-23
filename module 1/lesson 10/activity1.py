medical_cause = input("do you have a medical cause answer Y/N")
attendence = int(input("what is your attendence?"))
if medical_cause == "Y" :
    print ("allowed")
else :
    if attendence >= 75 :
        print ("allowed")
    else : 
        print ("not allowed")
