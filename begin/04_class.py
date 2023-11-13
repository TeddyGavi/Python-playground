class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def print_name(self):
        print(self.fname, self.lname)


person1 = Person("Bob", "villa", 45)


class Student(Person):
    pass


student1 = Student("Bob", "Ross", 45)
student1.print_name()
person1.print_name()
