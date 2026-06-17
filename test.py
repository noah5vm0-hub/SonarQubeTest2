def calculate_student_grade(score):
    if score >= 90:
        result = "A"
    elif score >= 80:
        result = "B"
    elif score >= 70:
        result = "C"
    elif score >= 60:
        result = "D"
    else:
        result = "F"

    print(f"Student grade: {result}")
    return result


def calculate_employee_level(score):
    if score >= 90:
        result = "Senior"
    elif score >= 80:
        result = "Intermediate"
    elif score >= 70:
        result = "Junior"
    elif score >= 60:
        result = "Trainee"
    else:
        result = "Probation"

    print(f"Employee level: {result}")
    return result
