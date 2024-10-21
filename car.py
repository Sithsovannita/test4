"""
        ------------------------------------------------------
        This file use for defind a blue print for `car` object
"""


class car:
    # constuctor
    def __init__(self,model,year,color):
        self.model=model
        self.year=year
        self.color=color
    def drive(self):
        print(f"This {self.model} is driving...")
        
if __name__=='__main__':
    car1=car("GTR R35",2019,"Black")
    car2=car("Raptor",2024,"Black")
    car1.drive()
    car2.drive()

