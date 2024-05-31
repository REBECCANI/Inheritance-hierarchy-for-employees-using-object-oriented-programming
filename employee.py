class Employee:
    def __init__(self, employee_id, first_name, last_name, email, salary):
        self._employee_id = employee_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._salary = salary

    def get_employee_id(self):
        return self._employee_id

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
        else:
            raise ValueError("Salary cannot be negative.")

    def display_info(self):
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Name: {self.get_first_name()} {self.get_last_name()}")
        print(f"Email: {self.get_email()}")
        print(f"Salary: ${self.get_salary()}")

