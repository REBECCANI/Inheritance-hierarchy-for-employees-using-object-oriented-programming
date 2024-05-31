from employee import Employee
from manager import Manager
from director import Director
from intern import Intern

# Creating a Manager instance
manager1 = Manager(1, "KIRABO", "Esther", "esther.ki@gmail.com", 60000, "Sales", 10, 0.4)

# Using setter methods to update private attributes
manager1.set_department("Marketing")
manager1.set_num_direct_reports(15)
manager1.set_rate(0.5)

# Accessing private attributes using getter methods
print("Manager Information:")
print(f"First name: {manager1.get_first_name()}")
print(f"Last name: {manager1.get_last_name()}")
print(f"Email: {manager1.get_email()}")
print(f"Salary: {manager1.get_salary()}")
print(f"Department: {manager1.get_department()}")
print(f"Number of Direct Reports: {manager1.get_num_direct_reports()}")
print(f"Allowance Rate: {manager1.get_rate()}")
print(f"Earnings: ${manager1.calculate_earnings():.2f}\n")

# Creating a Director instance
director1 = Director(2, "INGABIRE", "Sylvie", "sylvie.ng@gmail.com", 80000, "Law", 10000)

# Using setter methods to update private attributes
director1.set_department("Legal Affairs")
director1.set_annual_bonus(12000)

# Accessing private attributes using getter methods
print("Director Information:")
print(f"First name: {director1.get_first_name()}")
print(f"Last name: {director1.get_last_name()}")
print(f"Email: {director1.get_email()}")
print(f"Salary: {director1.get_salary()}")
print(f"Department: {director1.get_department()}")
print(f"Annual Bonus: ${director1.get_annual_bonus()}")
print(f"Earnings: ${director1.calculate_earnings():.2f}\n")

# Creating an Intern instance
intern1 = Intern(3, "GIRAMATA", "Divine", "divine.gi@gmail.com", 20000, "XYZ University", "Software Engineering", 4)

# Using setter methods to update private attributes
intern1.set_university("ABC University")
intern1.set_program("Computer Science")
intern1.set_duration_months(5)

# Accessing private attributes using getter methods
print("Intern Information:")
print(f"First name: {intern1.get_first_name()}")
print(f"Last name: {intern1.get_last_name()}")
print(f"Email: {intern1.get_email()}")
print(f"Salary: {intern1.get_salary()}")
print(f"University: {intern1.get_university()}")
print(f"Program Name: {intern1.get_program()}")
print(f"Duration (months): {intern1.get_duration_months()}")
print(f"Earnings: ${intern1.calculate_earnings():.2f}\n")