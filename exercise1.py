# leap_years=[]
# start_year=int(input("Enter start year:"))
# end_year=int(input("Enter end year:"))
# for year in range(start_year ,end_year+1):
#     if(year %400==0) or (year%4==0 and year %100!=0):
#         leap_years.append(year)
# print(leap_years)

# # def add(x):
# #     return x+10
# add=lambda x:x+10
# print(add(2))

# # def expo(x):
# #     return x**x
# expo=lambda x:x**x
# print(expo(2))

# # def is_event(a):
# #     return a%2==0
# is_event=lambda a:a%2==0
# print(is_event(10))
# # def area(b,h):
# #     return b*h/2
# area=lambda b,h:b*h/2
# print(area(2,2))


# my_list=[]
# my_list=['Veasna','Dalin','Hong','Nika','Ena','Lisa','Nuna','Mina', 'Eva','Pina']
# a=input("Enter name:")
# for name in my_list:
#    if a in name:
#       print(f"This is you charactor:{name}")
      

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print( )

n=5
for i in range(1,n+1):
    print(''*(n-i),end=" ")
    for j in range (1,i+1):
        print(j,end=" ")
    print( )
    
n=5
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=" ")
    print()

n=5
for i in range(1,n+1):
    print(''*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()

    