from employee import Employee
class Intern(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, university, program, duration_months):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self._university = university
        self._program = program
        self._duration_months = duration_months

    def get_university(self):
        return self._university
    
    def set_university(self, new_univerity):
        self._university = new_univerity

    def get_program(self):
        return self._program
    
    def set_program(self, new_program):
        self._program = new_program

    def get_duration_months(self):
        return self._duration_months

    def set_duration_months(self, new_duration):
        if 3 <= new_duration <= 6:
            self._duration_months = new_duration
        else:
            raise ValueError("Duration must be between 3 and 6 months.")

    def calculate_earnings(self):
        return self.get_salary() * (self.get_duration_months() / 12)

