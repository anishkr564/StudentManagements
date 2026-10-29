students = []

def add_student(name, roll_no):
    students.append({"name": name, "roll_no": roll_no})

def display_students():
    for s in students:
        print(f"{s['roll_no']} - {s['name']}")

add_student("Anish", 1)
add_student("Rahul", 2)
display_students()