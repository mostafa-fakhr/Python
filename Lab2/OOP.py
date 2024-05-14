
class Employee:
    EmployeeList = []

    def __init__(self,First_name,Last_name,Age,Department,Salary):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Age = Age
        self.Department = Department
        self.Salary = Salary


        Employee.EmployeeList.append(self)

    def insert_record_in_database(self):
        print(f"Inserting new employee {self.First_name} {self.Last_name} into database.")
        

    def transfer(self, newdepartment):
        self.Department = newdepartment
    

    def update_database(self):
        print(f"Updating database employee {self.first_name} {self.last_name}.")


    def remove_from_database(self):
        Employee.EmployeeList.remove(self)

        
    def show(self):
        # Print all employee data
        print(f"Employee Details:")
        print(f"First Name: {self.First_name}")
        print(f"Last Name: {self.Last_name}")
        print(f"Age: {self.Age}")
        print(f"Department: {self.Department}")
        print(f"Salary: {self.Salary}")


    def AllEmployees():
        print("List of Employees:")
        for employee in Employee.EmployeeList:
            employee.show()
            print()
        








class Manager(Employee):
    def __init__(self,Managed_Department,First_name,Last_name,Age,Department,Salary) :
        super().__init__(First_name,Last_name,Age,Department,Salary)
        self.Managed_Department = Managed_Department

    

    def show(self):
        # Print all data except the salary (print 'Confidential' instead)
        print("Employee Details:")
        print(f"First Name: {self.First_name}")
        print(f"Last Name: {self.Last_name}")
        print(f"Age: {self.Age}")
        print(f"Department: {self.Department}")
        print("Salary: Confidential")
        print(f"Managed Department: {self.Managed_department}")



emp1 = Employee("John", "Doe", 30, "HR", 50000)
emp2 = Employee("Jane", "Smith", 35, "IT", 60000)




while True:
    print("\nMenu:")
    print("add new employee (type add)")
    print("show specific data of employee (type show)")
    print("quit the program (type quit)")

    choice = input("Enter your choice: ")

    if choice == 'add':
        first_name = input("Enter employee's first name: ")
        last_name = input("Enter employee's last name: ")
        age = input("Enter employee's age: ")
        department = input("Enter employee's department: ")
        salary = input("Enter employee's salary: ")
        managed_department = input("Enter managed department: ")
        employee_type = input("Enter employee type (manager for Manager, employee for Employee): ")


        if employee_type=="manager":
            Manager(first_name,last_name,age,department,salary,managed_department)
        elif employee_type=="employee":
            Employee(first_name,last_name,age,department,salary)

        print("Employee added successfully!")

    elif choice == 'show':
        if not Employee.AllEmployees:
            print("No employees to show.")
        else:
            Employee.AllEmployees()


    elif choice == 'quit':
        print("Exiting the program. Goodbye!")
        break

    
    else:
        print("Invalid choice. Please enter a valid option.")