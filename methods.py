class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        return self.marks > 40
s1 = Student("Naga Sri", 55)
s2 = Student("Asha", 72)
print(f"{s1.name}: {'Passed' if s1.is_passed() else 'Failed'}")
print(f"{s2.name}: {'Passed' if s2.is_passed() else 'Failed'}")


class Employee:
    company_name = "TechCorp"
    def __init__(self, name):
        self.name = name
    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name
    def display(self):
        print(f"{self.name} works at {Employee.company_name}")
e1 = Employee("Rahul")
e2 = Employee("Priya")
e1.display()
e2.display()
Employee.change_company("InnovateX")
print("\nAfter company name change:")
e1.display()
e2.display()


class MathOps:
    @staticmethod
    def is_even(num):
        return num % 2 == 0
print(MathOps.is_even(10))
m = MathOps()
print(m.is_even(7))



class Car:
    wheels = 4
    def __init__(self, mileage):
        self.mileage = mileage
    def display_specs(self):
        print(f"Mileage: {self.mileage} kmpl, Wheels: {Car.wheels}")
    @classmethod
    def change_wheels(cls, new_wheels):
        cls.wheels = new_wheels
car1 = Car(18)
car1.display_specs()
Car.change_wheels(6)
print("After modification:")
car1.display_specs()


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32
    def show_conversion(self):
        f = Temperature.to_fahrenheit(self.celsius)
        print(f"{self.celsius}°C = {f}°F")
t = Temperature(25)
t.show_conversion()

class Book:
    total_books = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1
    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)
    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3
if Book.is_valid_title("Python"):
    b1 = Book("Python", "Guido")
if Book.is_valid_title("AI"):
    b2 = Book.from_string("AI-Andrew")
else:
    print("Invalid title: AI")
b3 = Book.from_string("ML-Tom")
print(f"Total books created: {Book.total_books}")


class Employee:
    bonus_rate = 0.1
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def final_salary(self):
        return self.base_salary + (self.base_salary * Employee.bonus_rate)
    @classmethod
    def update_bonus(cls, new_rate):
        cls.bonus_rate = new_rate
    @staticmethod
    def is_valid_salary(sal):
        return sal > 0
e1 = Employee("Sneha", 50000)
e2 = Employee("Aman", 60000)
print(f"{e1.name} final salary: {e1.final_salary()}")
print(f"{e2.name} final salary: {e2.final_salary()}")
Employee.update_bonus(0.15)
print("\nAfter bonus update:")
print(f"{e1.name} final salary: {e1.final_salary()}")
print(f"{e2.name} final salary: {e2.final_salary()}")


class Course:
    total_students = 0
    def __init__(self, student_name):
        self.student_name = student_name
    def enroll(self):
        Course.total_students += 1
        print(f"{self.student_name} enrolled")
    @classmethod
    def show_total(cls):
        print(f"Total students: {cls.total_students}")
    @staticmethod
    def is_eligible(age):
        return age >= 18
s1 = Course("Riya")
s2 = Course("Kabir")
if Course.is_eligible(20):
    s1.enroll()
if Course.is_eligible(17):
    s2.enroll()  # won't enroll
else:
    print("Kabir not eligible")
Course.show_total()


class BankAccount:
    bank_name = "SBI"
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance
    def deposit(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid amount")
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
    @staticmethod
    def validate_amount(amount):
        return amount > 0
acc = BankAccount("Vikram", 1000)
acc.deposit(500)
acc.deposit(-100)
BankAccount.change_bank_name("HDFC")
print(f"Bank name now: {BankAccount.bank_name}")


class Student:
    passing_marks = 40
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def result(self):
        if self.marks >= Student.passing_marks:
            print(f"{self.name}: Passed")
        else:
            print(f"{self.name}: Failed")
    @classmethod
    def update_passing_marks(cls, new_marks):
        cls.passing_marks = new_marks
    @staticmethod
    def grade_category(marks):
        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"
s1 = Student("Anita", 75)
s2 = Student("Rohit", 38)
print(f"{s1.name} Grade: {Student.grade_category(s1.marks)}")
s1.result()
print(f"{s2.name} Grade: {Student.grade_category(s2.marks)}")
s2.result()
Student.update_passing_marks(35)
print("\nAfter updating passing marks to 35:")
s2.result()