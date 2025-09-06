low = int(input("enter the lowr number"))
upper = int(input("enter the upper number"))
for num in range (low, upper+1) :
         if num > 1:
                 for i in range (2, num) :
                         if num% i == 0 :
                                 break
                 else :
                         print (num)