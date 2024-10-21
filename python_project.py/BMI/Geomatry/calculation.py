# # while True:
# #     try:
# #         x,y=int(input("Enter x:")), int(input("Enter y:"))
# #         print(x,y)
# #         break
# #     except ValueError as error:
# #         print(f"An error occured:{error}")
# def get_x_y()->tuple:
#     while True:
#         try:
#             x=int(input("Enter x:"))
#             break
#         except ValueError as va:
#             print(f"An error occurred:{va}")
#     while True:
#         try:
#             y=int(input("Enter y:"))
#             break
#         except ValueError as va:
#             print(f"An error occurred:{va}")
#     return x,y
# x,y=get_x_y()
# print(x)
# try:
#     x=int(input("Enter x:"))
# except ValueError as va:
#     print("Invalid input...!")
# print("Your code...!")

from os import system
while True:
    try:
        choice=input("Select one choice:")
        if choice!='+' or choice != '-' or  choice !='*' or choice!='/':
            raise Exception("Invalid choice...!")
        break
    except Exception as error:
        system("cls")
        print(error)
print(f"Your choice is :{choice}")


