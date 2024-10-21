# number=int(input("Input number:"))
# rev=0
# while(number>0):
#     rev=(rev*10)+number%10
#     number=number//10
# print("Output number:",rev)


number=int(input("Enter number:"))
rev=0
remain=0
while number>0:
    remain=number%10
    rev=rev*10+remain
    number//=10
print(rev)
# eval use for calculate in consol
print(eval(input("Input:")))








