class Student:
    def __init__(self, usn, name, subjects=None):
        self.usn = usn
        self.name = name
        self.subjects = subjects or []


class Subject:
    init_id = 1
    def __init__(self, name):
        self.id = Subject.init_id
        self.name = name
        Subject.init_id += 1


class Manipulator:
    def __init__(self):
        self.students = {}
        self.subjects = {}

    # ---------- Utility ----------
    def get_or_create_subject(self, name):
        for sub in self.subjects.values():
            if sub.name.lower() == name.lower():
                return sub.id
        new_sub = Subject(name)
        self.subjects[new_sub.id] = new_sub
        return new_sub.id

    def get_subject_obj(self, name):
        for sub in self.subjects.values():
            if sub.name.lower() == name.lower():
                return sub
        return None

    # ---------- Student ----------
    def insert_student(self, usn, name, subject_names):
        if usn in self.students:
            print("Student already exists!")
            return

        subject_ids = [self.get_or_create_subject(s.strip())
                       for s in subject_names]

        self.students[usn] = Student(usn, name, subject_ids)
        print("Student added successfully.")

    def search_student(self, usn):
        student = self.students.get(usn)
        if not student:
            print("Student not found!")
            return

        print(f"\nUSN: {student.usn}")
        print(f"Name: {student.name}")
        print("Subjects:")
        for sid in student.subjects:
            print("-", self.subjects[sid].name)

    def display_students(self):
        if not self.students:
            print("No students available.")
            return
        for usn in self.students:
            self.search_student(usn)

    def update_student(self, usn):
        student = self.students.get(usn)
        if not student:
            print("Student not found!")
            return

        print("1.Name  2.Subjects  3.Both")
        ch = int(input("Choice: "))

        if ch in (1, 3):
            student.name = input("New name: ")

        if ch in (2, 3):
            names = input("New subjects (comma): ").split(",")
            student.subjects = [self.get_or_create_subject(s.strip())
                                for s in names]

        print("Updated successfully.")

    def delete_student(self, usn):
        if self.students.pop(usn, None):
            print("Student deleted.")
        else:
            print("Student not found!")

    # ---------- Subject ----------
    def add_subject(self, name):
        if self.get_subject_obj(name):
            print("Subject already exists!")
            return
        sid = self.get_or_create_subject(name)
        print(f"Subject added (ID {sid})")

    def delete_subject(self, name):
        subject = self.get_subject_obj(name)
        if not subject:
            print("Subject not found!")
            return

        del self.subjects[subject.id]
        for s in self.students.values():
            if subject.id in s.subjects:
                s.subjects.remove(subject.id)

        print("Subject deleted.")

    def display_subjects(self):
        if not self.subjects:
            print("No subjects available.")
            return
        for s in self.subjects.values():
            print(f"{s.id} - {s.name}")


# ------------------ MENU ------------------

m = Manipulator()

while True:
    print("\n1.Insert 2.Search 3.All Students 4.Update")
    print("5.Del Student 6.Del Subject 7.Add Subject")
    print("8.Show Subjects 9.Exit")

    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            usn = input("USN: ")
            name = input("Name: ")
            subs = input("Subjects (comma): ").split(",")
            m.insert_student(usn, name, subs)
        case 2:
            m.search_student(input("USN: "))
        case 3:
            m.display_students()
        case 4:
            m.update_student(input("USN: "))
        case 5:
            m.delete_student(input("USN: "))
        case 6:
            m.delete_subject(input("Subject name: "))
        case 7:
            m.add_subject(input("Subject name: "))
        case 8:
            m.display_subjects()
        case 9:
            break
        case _:
            print("Invalid choice!")
