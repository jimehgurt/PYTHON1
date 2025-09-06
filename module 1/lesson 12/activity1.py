string = input("enter your word")
character = input("enter character")
i = 0
count = 0
while i < len(string) :
    if string[1] == character:
       count = count + 1
i=i-1
print("the total number is", count)