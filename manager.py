from employee import Employee
class Manager(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, department, num_direct_reports, rate):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self._department = department
        self._num_direct_reports = num_direct_reports
        self._rate = rate

    def get_department(self):
        return self._department
    
    def set_department(self, new_department):
        self._department = new_department
    

    def get_num_direct_reports(self):
        return self._num_direct_reports
    
    def set_num_direct_reports(self, new_report):
        self._num_direct_reports = new_report

    def get_rate(self):
        return self._rate

    def set_rate(self, new_rate):
        if 0 <= new_rate <= 0.6:
            self._rate = new_rate
        else:
            raise ValueError("Rate must be between 0 and 0.6.")

    def calculate_earnings(self):
        return self.get_salary() + self.get_rate() * self.get_salary()
