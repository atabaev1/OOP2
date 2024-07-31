class Person:
    def __init__(self, name, age, address, username, password):
        self.name = name
        self.age = age
        self.address = address
        self.username = username
        self.password = password

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


class Employee(Person):
    def __init__(self, name, age, address, username, password, employee_id, position):
        super().__init__(name, age, address, username, password)
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}, Position: {self.position}")

    def notify(self, message):
        print(f"Notification for {self.name}: {message}")


class HRManager(Employee):
    def __init__(self, name, age, address, username, password, employee_id, position):
        super().__init__(name, age, address, username, password, employee_id, position)

    def conduct_interview(self, candidate):
        print(f"Conducting interview with {candidate.name}")


class Recruiter(Employee):
    def __init__(self, name, age, address, username, password, employee_id, position):
        super().__init__(name, age, address, username, password, employee_id, position)

    def search_candidate(self):
        print(f"Searching for candidates")


class Trainer(Employee):
    def __init__(self, name, age, address, username, password, employee_id, position):
        super().__init__(name, age, address, username, password, employee_id, position)

    def conduct_training(self):
        print(f"Conducting training program")


class Director(Employee):
    def __init__(self, name, age, address, username, password, employee_id, position):
        super().__init__(name, age, address, username, password, employee_id, position)

    def assign_task(self, recruiter, task):
        print(f"Assigning task to recruiter: {task}")
        recruiter.notify(task)


class HRSystem:
    def __init__(self):
        self.employees = []
        self.logged_in_employee = None

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

    def login(self, username, password):
        for emp in self.employees:
            if emp.username == username and emp.password == password:
                self.logged_in_employee = emp
                print(f"{emp.name} has logged in successfully.")
                return True
        print("Login failed. Invalid username or password.")
        return False

    def logout(self):
        if self.logged_in_employee:
            print(f"{self.logged_in_employee.name} has logged out.")
            self.logged_in_employee = None

    def register_candidate(self, candidate):
        print(f"Registering candidate {candidate.name}")
        # You can add code here to save candidate details to a list or database

    def evaluate_employee(self, employee_id, performance):
        employee = self.find_employee(employee_id)
        if employee:
            print(f"Evaluating employee {employee.name} with performance: {performance}")
        else:
            print(f"Employee with ID {employee_id} not found")

    def manage_training(self):
        print("Managing training programs for employees")


if __name__ == "__main__":
    hr_system = HRSystem()

    emp1 = HRManager("Alice", 30, "123 Main St", "alice", "password123", 1, "HR Manager")
    emp2 = Recruiter("Bob", 40, "456 Elm St", "bob", "password456", 2, "Recruiter")
    emp3 = Trainer("Charlie", 35, "789 Oak St", "charlie", "password789", 3, "Trainer")
    emp4 = Director("Dave", 50, "321 Pine St", "dave", "password321", 4, "Director")

    hr_system.add_employee(emp1)
    hr_system.add_employee(emp2)
    hr_system.add_employee(emp3)
    hr_system.add_employee(emp4)

    hr_system.display_all_employees()

    if hr_system.login("alice", "password123"):
        emp1.conduct_interview(emp2)
        hr_system.logout()

    if hr_system.login("bob", "password456"):
        emp2.search_candidate()
        hr_system.logout()

    if hr_system.login("dave", "password321"):
        emp4.assign_task(emp2, "Find 5 new candidates for the IT department")
        hr_system.logout()

    hr_system.remove_employee(1)

    hr_system.display_all_employees()
