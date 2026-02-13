class Student:
    def __init__(self, usn, name, subject_ids=None):
        self.usn = usn
        self.name = name
        self.subjects = subject_ids if subject_ids else []


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

    # ------------------------
    # Helper Methods
    # ------------------------

    def get_subjectId(self, name):
        for subject in self.subjects.values():
            if subject.name.lower() == name.lower():
                return subject
        return None

    def create_or_get_subject_ids(self, subject_names):
        subject_ids = []

        for sub_name in subject_names:
            subject = self.get_subjectId(sub_name)

            if subject:
                subject_ids.append(subject.id)
            else:
                new_subject = Subject(sub_name)
                self.subjects[new_subject.id] = new_subject
                subject_ids.append(new_subject.id)

        return subject_ids

    # ------------------------
    # Student Methods
    # ------------------------

    def insert_student(self, usn, name):
        if usn in self.students:
            print("Student already exists!")
            return

        self.students[usn] = Student(usn, name)
        print("Student added successfully.")

        choice = input("Do you want to assign subjects now? (y/n): ").lower()

        if choice == 'y':
            self.assign_subjects(usn)


    def assign_subjects(self, usn):
        if usn not in self.students:
            print("Student not found!")
            return

        if not self.subjects:
            print("No subjects available.")
            return

        self.display_subjects()

        ids_input = input("Enter subject IDs (comma separated): ")
        try:
            ids = [int(i.strip()) for i in ids_input.split(",")]
        except ValueError:
            print("Invalid input!")
            return

        student = self.students[usn]

        for sub_id in ids:
            if sub_id in self.subjects:
                if sub_id not in student.subjects:
                    student.subjects.append(sub_id)

        print("Subjects assigned successfully.")

    def search_student(self, usn):
        if usn not in self.students:
            print("Student not found!")
            return

        student = self.students[usn]

        print("\nStudent Details")
        print("----------------")
        print(f"USN: {student.usn}")
        print(f"Name: {student.name}")
        print("Subjects:")

        if not student.subjects:
            print("No subjects assigned.")
            return

        for sub_id in student.subjects:
            subject = self.subjects.get(sub_id)
            if subject:
                print(f"- {subject.name}")

    def display_students(self):
        if not self.students:
            print("No students available.")
            return

        for usn in self.students:
            self.search_student(usn)

    def update_student(self, usn):
        if usn not in self.students:
            print("Student not found!")
            return

        student = self.students[usn]

        print("\nUpdate Menu")
        print("1. Update Name")
        print("2. Update Subjects")
        print("3. Update Both")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input!")
            return

        if choice == 1:
            new_name = input("Enter new name: ")
            student.name = new_name
            print("Name updated successfully.")

        elif choice == 2:
            subjects_input = input("Enter new Subjects (comma-separated): ")
            subject_names = [s.strip() for s in subjects_input.split(",")]
            student.subjects = self.create_or_get_subject_ids(subject_names)
            print("Subjects updated successfully.")

        elif choice == 3:
            new_name = input("Enter new name: ")
            student.name = new_name

            subjects_input = input("Enter new Subjects (comma-separated): ")
            subject_names = [s.strip() for s in subjects_input.split(",")]
            student.subjects = self.create_or_get_subject_ids(subject_names)

            print("Student updated successfully.")

        else:
            print("Invalid choice!")

    def delete_student(self, usn):
        if usn not in self.students:
            print("Student not found!")
            return

        del self.students[usn]
        print("Student deleted successfully.")

    # ------------------------
    # Subject Methods
    # ------------------------

    def delete_subject(self, subject_name):
        subject = self.get_subjectId(subject_name)

        if not subject:
            print("Subject not found!")
            return

        del self.subjects[subject.id]

        for student in self.students.values():
            if subject.id in student.subjects:
                student.subjects.remove(subject.id)

        print("Subject deleted successfully.")

    def add_subject(self, name):
        if self.get_subjectId(name):
            print("Subject already exists!")
            return

        new_subject = Subject(name)
        self.subjects[new_subject.id] = new_subject
        print("Subject added successfully.")

    def display_subjects(self):
        if not self.subjects:
            print("No subjects available.")
            return

        print("\nAll Subjects")
        print("-------------")
        for subject in self.subjects.values():
            print(f"ID: {subject.id} | Name: {subject.name}")


# ------------------------
# MAIN PROGRAM
# ------------------------

m = Manipulator()

while True:
    print("\nMENU")
    print("1. Manage Students")
    print("2. Manage Subjects")
    print("3. Exit")

    try:
        n = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input!")
        continue

    match n:
        case 1:
            print("\n1. Insert Student")
            print("2. Assign Subjects")
            print("3. Display Student")
            print("4. Display All Students")
            print("5. Update Student")
            print("6. Delete Student")

            x = int(input("Enter your choice: "))

            match x:
                case 1:
                    usn = input("Enter USN: ")
                    name = input("Enter Name: ")
                    m.insert_student(usn, name)

                case 2:
                    usn = input("Enter USN: ")
                    m.assign_subjects(usn)

                case 3:
                    usn = input("Enter USN: ")
                    m.search_student(usn)

                case 4:
                    m.display_students()

                case 5:
                    usn = input("Enter USN: ")
                    m.update_student(usn)

                case 6:
                    usn = input("Enter USN: ")
                    m.delete_student(usn)

        case 2:
            print("\n1. Add Subject")
            print("2. Delete Subject")
            print("3. Display Subjects")

            y = int(input("Enter your choice: "))

            match y:
                case 1:
                    name = input("Enter subject name: ")
                    m.add_subject(name)

                case 2:
                    name = input("Enter subject name: ")
                    m.delete_subject(name)

                case 3:
                    m.display_subjects()

        case 3:
            print("Exiting program...")
            break

        case _:
            print("Invalid choice!")
