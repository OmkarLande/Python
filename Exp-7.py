#CLASS
class Student:
    def __init__(self):   #CONSTRUCTOR
        self.name = "Indira"
        self.course = "physics"

    def info(self):
        print(f"{self.name} loves {self.course}")
    
    @staticmethod
    def add(a,b):
        print("addition is",(a+b))
    
    #inner class
    class Marks:
        def __init__(self):
            self.num=99

        def display(self):
            print("My marks in this subject is: ",self.num)
a = Student()  # OBJECT
a.info()
a.add(2,3)     #Static Method
b=a.Marks()   #inner class object
b.display()
