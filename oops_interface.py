class Student:
    def __init__(self, usn, name):
        self.id = usn
        self.name = name
        self.subjects = []


class Subject:
    init_id = 1

    def __init__(self, name):
        self.id = Subject.init_id
        self.name = name
        Subject.init_id += 1

class CRUDManager:
    def __init__(self):
        self.data = {}

    def create(self, obj):
        if obj.id in self.data:
            print("Already exists!")
            return
        self.data[obj.id] = obj
        print("Created successfully.")

    def read(self, obj_id):
        obj = self.data.get(obj_id)
        if not obj:
            print("Not found!")
            return
        return obj

    def update(self, obj_id, **kwargs):
        obj = self.data.get(obj_id)
        if not obj:
            print("Not found!")
            return

        for key, value in kwargs.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        print("Updated successfully.")

    def delete(self, obj_id):
        if obj_id not in self.data:
            print("Not found!")
            return
        del self.data[obj_id]
        print("Deleted successfully.")

    def display_all(self):
        if not self.data:
            print("No records found.")
            return

        for obj in self.data.values():
            print(vars(obj))

student_manager = CRUDManager()
subject_manager = CRUDManager()

s = Student("101", "Pragna")
student_manager.create(s)

sub = Subject("Math")
subject_manager.create(sub)

student_manager.update("101", name="New Name")

student_manager.display_all()
subject_manager.display_all()