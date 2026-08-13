class Student:
    
    def __init__(self, name, dept, roll_no):
        self.name = name
        self.dept = dept
        self.roll_no = roll_no

    
    def show(self):
        print("Name:", self.name)
        print("Department:", self.dept)
        print("Roll No:", self.roll_no)
        print("----------------------")



s1 = Student("Avik", "CSE", 101)
s2 = Student("Rahul", "CSE", 102)
s3 = Student("Sourav", "IT", 103)
s4 = Student("Ankit", "ECE", 104)
s5 = Student("Rohan", "CSE", 105)


s1.show()
s2.show()
s3.show()
s4.show()
s5.show()
