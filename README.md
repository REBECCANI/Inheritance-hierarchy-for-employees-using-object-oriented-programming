                             EMPLOYMENT MANAGEMENT SYSTEM

This Python-based Employee Management System is designed using object-oriented programming principles. It allows you to create and manage different types of employees, including regular employees, managers, directors, and interns. Below are the key components and instructions for using the system effectively.

# Components
1. Employee Class:

Represents basic employee information such as ID, name, email, and salary.
Provides methods to access and modify this information.
2. Manager Class:

Inherits from the Employee class and extends it to include manager-specific attributes.
Allows management of department, number of direct reports, and a rate for additional earnings.
Calculates earnings based on salary and the additional rate.
3. Director Class:

Inherits from the Employee class and includes director-specific attributes like department and an annual bonus.
Provides methods to manage department and annual bonus.
Calculates total earnings considering the salary and annual bonus.
4. Intern Class:

Inherits from the Employee class and is tailored for intern-specific information.
Manages university details, program, and internship duration in months.
Calculates earnings based on the internship duration.

# How to Use

1. Creating Employees:

Create instances of employees using their respective classes (Employee, Manager, Director, Intern).
Provide necessary information such as ID, name, email, salary, and specific attributes like department, bonus, or internship duration.

2. Updating Employee Information:

Use setter methods to update private attributes of employees.
For example, set_department(new_department) updates the department for managers and directors.
Accessing Employee Information:

3. Utilize getter methods to retrieve employee details.
For instance, get_salary() returns the salary of the employee.
Calculating Earnings:

4. Call the calculate_earnings() method on employees to determine their total earnings based on their specific logic.
Managers earn a percentage of their salary as an additional rate, directors have an annual bonus, and interns earn based on their internship duration.

# Running the Code
1. Ensure that each class (Employee, Manager, Director, Intern) is in a separate Python file.
2. Import these classes into your main script.
3. Create instances of employees and utilize setter and getter methods to manage and access their information.
4. Calculate earnings using the calculate_earnings() method specific to each employee type.

# AUTHOR
Nishimwe rebecca
nrebecca@andrew.cmu.edu
MSECE

[1] ‘Python Crash Course by ehmatthes’. Accessed: Oct. 11, 2023. [Online]. Available: https://ehmatthes.github.io/pcc/
[2] ‘PEP 8 – Style Guide for Python Code | peps.python.org’. Accessed: Oct. 11, 2023. [Online]. Available: https://peps.python.org/pep-0008/
