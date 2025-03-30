class employee():
    companyname= "Jetlearn"
    def __init__(self, name, age, idnumber, department):
        self.name = name
        self.age = age
        self.idnumber = idnumber
        self.department = department
    def Showdetails(self):
        print(f"name: {self.name}\n age: {self.age} \n idnumber: {self.idnumber} \n department: {self.department} \n companyname: {self.companyname}")

    def changeage(self):
        newage= input("To what age would you like to change it? ")
        self.age=newage
employee= employee("Anjali", 18, 27, "Teacher")
employee.Showdetails()
employee.changeage()
employee.Showdetails()