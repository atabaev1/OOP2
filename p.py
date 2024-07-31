class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")
        
class Employee(Person):
    def __init__(self, name, age, address, employee_id, position):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}, Position: {self.position}")

    def notify(self, message):
        print(f"Notification for {self.name}: {message}")
class Manager(Employee):
    def __init__(self, name, age, address, employee_id, position, department):
        super().__init__(name, age, address, employee_id, position)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
        
class HRSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        employee_to_remove = None
        for emp in self.employees:
            if emp.employee_id == employee_id:
                employee_to_remove = emp
                break
        
        if employee_to_remove:
            self.employees.remove(employee_to_remove)
            employee_to_remove.notify("You have been removed from the company.")

    def find_employee(self, employee_id):
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def display_all_employees(self):
        for emp in self.employees:
            emp.display_info()
            print("-" * 30)
            
if __name__ == "__main__":
    hr_system = HRSystem()

    emp1 = Employee("Alice", 30, "123 Main St", 1, "Developer")
    emp2 = Manager("Bob", 40, "456 Elm St", 2, "Project Manager", "IT")

    hr_system.add_employee(emp1)
    hr_system.add_employee(emp2)

    hr_system.display_all_employees()

    hr_system.remove_employee(1)  

    hr_system.display_all_employees()
