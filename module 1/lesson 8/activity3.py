print ("enter your grades for all subjects")
math = int(input("whats your grade for maths"))
eng = int(input("whats your grade for eng"))
sci = int(input("whats your grade for sci"))
his = int(input("whats your grade for his"))
geo = int(input("whats your grade for geo"))
total = math + eng + sci + his + geo
avg = total/5 
print ("the average is", avg)
if avg >= 90 :
    print ("you got an A+")
elif avg >= 80 and avg < 90 :
    print ("you got an A")
elif avg >= 70 and avg< 80 :
    print ("you got a B")
elif avg >= 50 and avg< 70 :
    print ("you got a C")
else :
    print ("you got an F")