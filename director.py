from employee import Employee
class Director(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, department, annual_bonus):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self._department = department
        self._annual_bonus = annual_bonus

    def get_department(self):
        return self._department
    
    def set_department(self, new_department):
        self._department = new_department

    def get_annual_bonus(self):
        return self._annual_bonus

    def set_annual_bonus(self, new_bonus):
        if new_bonus >= 0:
            self._annual_bonus = new_bonus
        else:
            raise ValueError("Bonus cannot be negative.")

    def calculate_earnings(self):
        return self.get_salary() + self.get_annual_bonus()
