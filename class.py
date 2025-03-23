class student():
    schoolname= "Stanislascollege Westplantsoen"
    def __init__(self, name, age, rollno, classname):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.classname = classname
    def Showdetails(self):
        print(f"name: {self.name}\n age: {self.age} \n rollno: {self.rollno} \n classname: {self.classname} \n schoolname: {self.schoolname}")
    def change_age(self):
        age=input("To what age do you want to change it? ")
        self.age=age
student1= student("Aryan Madan", 14, 14, "A3a")
student1.Showdetails()
student1.change_age()
student1.Showdetails()