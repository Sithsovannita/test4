"""
        Employee class
"""
class Employee :
    def __init__(self,_id="None",name="None",gender="None",position="None",salary="None")->None:
        self.id=_id
        self.name=name
        self.gender=gender
        self.position=position
        self.salary=salary
    def show_emp(self):
        return f"{self._id} {self.name} {self.gender} {self.position} {self.salary}"
    def input(self):
        try:
            self._id=int(input("Enter emp id:"))
            self.name=input("Enter emp name:")
            self.gender=input("Enter emp gender")
            self.position=input("Enter emp position:")
            self.salary=input("Enter emp salary:")
        except Exception as e:
            print(e)
        else:
            print("Employee data enterd successfully.")
emp1=Employee(1234,"Coca","Female","IT",500)
emp1.show_emp()
    