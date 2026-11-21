
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print(f"Employee Details:")
        super().show_details()
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)
        self.department = department

    def show_details(self):
        print(f"Manager Details:")
        super().show_details()
        print(f"Department: {self.department}")


people = []

while True:

    print("\n Python OOP Project: Employee Management System ")

    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)
        people.append(person)

        print(f"\nPerson created with name: {name} and age: {age}.")

    elif choice == "2":

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, emp_id, salary)
        people.append(employee)

        print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}.")

    elif choice == "3":

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age, emp_id, salary, department)
        people.append(manager)

        print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {department}.")

    elif choice == "4":

        if len(people) == 0:
            print("\nNo Details Found!")

        else:
            print("(\n All Details)")

            for person in people:
                print("\n")
                person.show_details()

    elif choice == "5":

        print("\nThank you for using Employee Management System!")
        break

    else:
        print("\nInvalid Choice! Please try again.")

    print("\nChoose another operation ")