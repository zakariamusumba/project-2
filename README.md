# Student Registration and Fee Management System

## 1. Project Description

The Student Registration and Fee Management System is a Python-based project designed to manage student registration details and fee records. The system stores student names, registration numbers, courses, and fee amounts. It also includes functions for recording student payments, calculating total fee balances, and generating student and institutional fee summaries.

The project aims to simplify student record management and make it easier to track fees payable by students.

## 2. Project Objectives

The main objectives of this project are:

- To register and store student information.
- To maintain student registration numbers and course details.
- To record student fee payments.
- To calculate total fee amounts and outstanding balances.
- To search for student records.
- To generate individual student fee statements.
- To provide an institutional summary of student fee records.

## 3. Technologies Used

- **Programming Language:** Python
- **Data Structures:** Lists, dictionaries, and sets
- **Functions:** Used to organize registration and fee management operations.
- **Input and Output:** Used to collect user input and display results in the terminal.

## 4. Student Records

The project contains sample records for the following students:

| Registration No. | Student Name | Course | Fee Amount |
|---|---|---|---:|
| 1 | Jerry | Mechanics | KSh 60,000 |
| 2 | Tom | Hospitality | KSh 120,000 |
| 3 | Mercy | Biomedical Science (Biomed) | KSh 130,000 |
| 4 | Michael | Business and Finance | KSh 200,000 |
| 5 | Mary | Nursing | KSh 345,000 |
| 6 | Harry | Computer Science | KSh 66,000 |
| 7 | Austin | Business and Architecture | KSh 26,000 |
| 8 | Benard | Agriculture and Natural Resources | KSh 16,000 |
| 9 | Paul | Business and Finance | Not specified |

*Note: The fee amounts above are reproduced from the sample data. They may represent recorded amounts rather than the official fees payable.*

## 5. Main Features

### Student Registration
Stores student names, registration numbers, courses, and fee information.

### Fee Recording
The `record_sh_number()` function records an amount against a student's registration number and adds it to any previously recorded amount.

### Total Fee Calculation
The `calculate_total_sh_numbers()` function calculates the total of all amounts recorded for students in a dictionary.

### Fee Balance Calculation
The project includes functions intended to calculate fee balances and determine the amount payable by students.

### Student Search
The project includes a `student_search()` function intended to check whether a student is registered.

### Payment Records and Reports
The project includes functions intended to manage payment records, individual student statements, and institutional fee summaries.

## 6. Project Functions

| Function | Purpose |
|---|---|
| `record_sh_number()` | Records and accumulates a student's fee amount. |
| `calculate_total_sh_numbers()` | Calculates the total recorded amounts for all students. |
| `calculated_balance()` | Multiplies the supplied value by the amount of KSh 134,000. |
| `calculate_institution_fees()` | Subtracts KSh 134,000 from the supplied value. |
| `student_registration()` | Intended to handle student registration. |
| `student_search()` | Intended to search student records. |
| `payment_record()` | Intended to manage payment records. |
| `calculate_balace()` | Intended to calculate fee balances. |
| `individual_statements()` | Intended to generate individual fee statements. |
| `institution_summary()` | Intended to generate an institutional fee summary. |

Some functions are still under development and require corrections before all features can work correctly.

## 7. How to Run the Project

### Requirements
- Python 3 installed on your computer.
- A code editor such as Visual Studio Code, PyCharm, or IDLE.

### Instructions

1. Save the Python code in a file named `main.py`.
2. Open a terminal or command prompt.
3. Navigate to the folder containing the project.
4. Run the program using:

   ```bash
   python main.py
   ```

5. Follow any prompts displayed in the terminal.

## 8. Example Usage

The `record_sh_number()` function can be used to record a student's fee amount:

```python
students_dictionary = {}

record_sh_number(students_dictionary, 9, 50000)
record_sh_number(students_dictionary, 9, 20000)

print(students_dictionary)
print(calculate_total_sh_numbers(students_dictionary))
```

Expected output:

```text
{9: {'sh_number': 70000}}
70000
```

This example demonstrates how two amounts recorded for registration number 9 are combined into one total.

## 9. Current Limitations

- Student records are stored in memory and are not permanently saved to a database or file.
- The student data uses a list of strings rather than a consistent dictionary-based registry.
- Some functions contain errors that prevent them from working as intended.
- The payment input is collected but is not used to update the student's fee balance.
- The fee payment status logic needs improvement.
- Student search and report-generation functions are incomplete.
- The program does not yet provide a complete menu-driven interface.

## 10. Future Improvements

The project can be improved by:

- Using dictionaries or a database to store student records consistently.
- Implementing a working student registration and search system.
- Adding payment processing and accurate outstanding balance calculations.
- Saving records permanently using files or an SQLite database.
- Generating individual fee statements and institutional reports.
- Adding a menu-driven interface for easier use.
- Validating registration numbers, payment amounts, and course information.
- Protecting student financial records against unauthorized access.

## 11. Conclusion

The Student Registration and Fee Management System is a starting point for developing a student administration application using Python. It demonstrates basic programming concepts such as lists, dictionaries, functions, loops, conditional statements, and arithmetic operations.

With further development and testing, the project can become a more reliable system for managing student registration, fee payments, outstanding balances, and institutional financial reports.