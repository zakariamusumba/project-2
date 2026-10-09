#Each student must have a unique registration number, name, course and total course
students = ["Jerry reg.no 1 : mechanics , sh60000\n"
            "Tom reg.no 2 : hospitality , sh120000\n"
            "Mercy reg.no 3 : biomed , sh130000\n"
            "Michael reg.no 4 : business and finance , sh200000\n"
            "Mary reg.no 5 : nursing , sh345000\n"
            "Harry reg.no 6 : computer science , sh66000\n"
            "Austin reg.no 7 : business and architecture , sh26000\n"
            "Benard reg.no 8 : agriculture and natural resourses , sh16000\n"
            ]


def record_sh_number(students_dictionary, registration_number, sh_number):
    """Add an SH amount to a student's record and return their new total."""
    if not isinstance(sh_number, (int, float)):
        raise ValueError("The SH amount must be a number.")

    if registration_number not in students_dictionary:
        students_dictionary[registration_number] = {}

    previous_amount = students_dictionary[registration_number].get("sh_number", 0)
    students_dictionary[registration_number]["sh_number"] = previous_amount + sh_number
    return students_dictionary[registration_number]["sh_number"]


def calculate_total_sh_numbers(students_dictionary):
    """Calculate the total of all SH amounts recorded for every student."""
    return sum(student.get("sh_number", 0) for student in students_dictionary.values())


print(students[4])
students.append("paul reg.no 9\n")
print(students)
print("== YOUR TOTAL FEE BALANCE ==")
reg1 = {
    "student name : Paul\n",
    "student reg no. : 9\n",
    "student course : business and finance\n",
}

for i in range (1,12):
    fee_balance = 134000 * i
    print(f"Total: sh{fee_balance} to be paid for {reg1}")

fees = input("Enter you amount: ")
total_balance = 134000
if total_balance == 134000:
    print("you have paid")
elif total_balance <= 134000:
    print("you have almost paid")
else:
    print("you have not paid")

def calculated_balance(x):
    amount = 134000
    print(amount)
    return  amount * x

def calculate_institution_fees(x):
    amount = 134000
    print (amount)
    return x - amount

def student_registration(registry):
    registry = students
    students = ["Jerry reg.no 1 : mechanics , sh60000\n"
            "Tom reg.no 2 : hospitality , sh120000\n"
            "Mercy reg.no 3 : biomed , sh130000\n"
            "Michael reg.no 4 : business and finance , sh200000\n"
            "Mary reg.no 5 : nursing , sh345000\n"
            "Harry reg.no 6 : computer science , sh66000\n"
            "Austin reg.no 7 : business and architecture , sh26000\n"
            "Benard reg.no 8 : agriculture and natural resourses , sh16000\n"
            ]
    
    print(students)
    return registry(students)

def student_search (registry):
     registry = students
     if students not in registry:
            print ("student did not register")

def payment_record():
    for i in range (1,12):
        total = i + students.strip().split()
        return (total)

def calculate_balace():
    for i in range (1,12):
            total = i + students.strip().split()
            return (total)

def individual_statements():
    for i in range (1,12):
            total = i + students.strip().split()
            return (total)

def institution_summary():
     for i in range (1,12):
             total = i + students.strip().split()
             return (total)