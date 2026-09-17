# Name: Lucas Escobar   
# Period: PM
# Student Performance Analyzer

# Program introduction
print(f"========================================")
print(f"       STUDENT PERFORMANCE CHECK        ")
print(f"========================================")
print(f"Enter the student information to start.\n")

# get all the student info
student_name = input(f"Student name: ")
grade_level = int(input(f"Grade level (9-12): "))
assignment_average = float(input(f"Assignment average: "))
quiz_average = float(input(f"Quiz average: "))
test_average = float(input(f"Test average: "))
attendance = float(input(f"Attendance percentage: "))
missing_assignments = int(input(f"Number of missing assignments: "))


# calculate the weighted grade
def calculate_grade(assignment_average, quiz_average, test_average):
    overall_grade = (assignment_average * 0.30) + (quiz_average * 0.30) + (test_average * 0.40)
    print(f"\nWeighted Overall Grade: {overall_grade:.1f}%")
    return overall_grade


# figure out the letter grade
def letter_grade(overall_grade):
    if overall_grade >= 90:
        grade = "A"
    elif overall_grade >= 80:
        grade = "B"
    elif overall_grade >= 70:
        grade = "C"
    elif overall_grade >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Letter Grade Earned: {grade}")


# check the attendance range
def attendance_status(attendance):
    if attendance >= 95:
        status = "Excellent Attendance"
    elif attendance >= 90:
        status = "Good Attendance"
    elif attendance >= 80:
        status = "Attendance Warning"
    else:
        status = "Poor Attendance"

    print(f"Attendance Check: {status}")


# check how many assignments are missing
def assignment_status(missing_assignments):
    if missing_assignments == 0:
        status = "Excellent"
    elif missing_assignments <= 2:
        status = "Good"
    elif missing_assignments <= 4:
        status = "Warning"
    else:
        status = "Critical"

    print(f"Missing Work Status: {status}")


# check eligibility without and/or
def check_eligibility(overall_grade, attendance, missing_assignments):
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                print(f"Academic Eligibility: ELIGIBLE")
                print(f"Result: all three requirements were met.")
            else:
                print(f"Academic Eligibility: NOT ELIGIBLE")
                print(f"Reason: there are too many missing assignments.")
        else:
            print(f"Academic Eligibility: NOT ELIGIBLE")
            print(f"Reason: attendance is below the requirement.")
    else:
        print(f"Academic Eligibility: NOT ELIGIBLE")
        print(f"Reason: the overall grade is below the requirement.")


# three level check for high honors
def check_high_honors(overall_grade, attendance, missing_assignments):
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                print(f"High Honors: YES")
            else:
                print(f"High Honors: NO")
                print(f"Reason: the student still has missing assignments.")
        else:
            print(f"High Honors: NO")
            print(f"Reason: attendance does not meet the honors requirement.")
    else:
        print(f"High Honors: NO")
        print(f"Reason: the grade does not meet the honors requirement.")


# good standing has to use and
def check_good_standing(overall_grade, attendance):
    if overall_grade >= 70 and attendance >= 90:
        print(f"Good Standing: YES")
    else:
        print(f"Good Standing: NO")


# support check has to use or
def check_support(overall_grade, attendance):
    if overall_grade < 70 or attendance < 80:
        print(f"Academic Support: RECOMMENDED")
    else:
        print(f"Academic Support: NOT NEEDED")


# message based on grade level
def grade_level_message(grade_level):
    if grade_level == 9:
        print(f"Grade Message: Freshman year - welcome to high school!")
    elif grade_level == 10:
        print(f"Grade Message: Sophomore year - keep building your skills!")
    elif grade_level == 11:
        print(f"Grade Message: Junior year - keep pushing forward!")
    elif grade_level == 12:
        print(f"Grade Message: Senior year - finish strong!")
    else:
        print(f"Grade Message: Invalid grade level entered.")


# find the strongest score without using max
def strongest_category(assignment_average, quiz_average, test_average):
    if assignment_average >= quiz_average:
        if assignment_average >= test_average:
            category = "Assignments"
        else:
            category = "Tests"
    else:
        if quiz_average >= test_average:
            category = "Quizzes"
        else:
            category = "Tests"

    print(f"Strongest Academic Category: {category}")


# extra credit status check
def check_advanced_status(overall_grade, attendance, missing_assignments):
    if (overall_grade >= 90 and attendance >= 95) or (overall_grade >= 85 and missing_assignments == 0):
        print(f"Advanced Status: OUTSTANDING STUDENT")
    else:
        print(f"Advanced Status: STANDARD STUDENT STATUS")


# calculate once and use the same grade for every check
overall_grade = calculate_grade(assignment_average, quiz_average, test_average)

print(f"\n--------------- RESULTS ----------------")
letter_grade(overall_grade)
attendance_status(attendance)
assignment_status(missing_assignments)
check_eligibility(overall_grade, attendance, missing_assignments)
check_high_honors(overall_grade, attendance, missing_assignments)
check_good_standing(overall_grade, attendance)
check_support(overall_grade, attendance)
grade_level_message(grade_level)
strongest_category(assignment_average, quiz_average, test_average)
check_advanced_status(overall_grade, attendance, missing_assignments)


# simple nested login check
print(f"\n--------------- LOGIN ------------------")
username = input(f"Enter username: ")
pin = input(f"Enter PIN: ")

if username == "student":
    if pin == "1234":
        print(f"Login Successful! Welcome back.")
    else:
        print(f"Login Failed: the PIN was incorrect.")
else:
    print(f"Login Failed: the username was incorrect.")


# final student summary
print(f"\n========================================")
print(f"            STUDENT SUMMARY")
print(f"========================================")
print(f"Student Name: {student_name}")
print(f"Grade Level: {grade_level}")
print(f"Assignment Average: {assignment_average:.1f}%")
print(f"Quiz Average: {quiz_average:.1f}%")
print(f"Test Average: {test_average:.1f}%")
print(f"Overall Grade: {overall_grade:.1f}%")
print(f"Attendance: {attendance:.1f}%")
print(f"Missing Assignments: {missing_assignments}")
print(f"========================================")
