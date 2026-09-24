class AssignmentSubmission:
    def__init__(self, student_name, student_id, assignment_title, due_date):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = None
        self.__submitted_files = []

    def add_file(self, filename):
        if self.__is_duplicate(filename):
            print(f"[Error] File '{filename}' already exists.")
        else:
            self.__submitted_file.append(filename)
            self.__check_submission_status()
            print(f"[Success] Added file: {filename}")

    def remove_file(self, filename):
        if filename in self.__submitted_file:
            self.__submitted_file.remove(filename)
            self.__check_submission_status()
            print(f"[Success] Removed file: {filename}")
        else:
            print(f"[Error] File '{filename}' not found.")

    def assign_grades(self, grade):
        if not self.__is_submitted:
            print("[Error] Cannot grade an unsubmitted assignment.")
        elif self.__validate_grade(score):
            self.__score = score
            print(f"[Success] Grade of {score} assigned to {self.student_name}.")
        else:
            print("[Error] Invalid score. Must be between 0.0 and 100.0.")

    def get_grade(self) -> str:
        if self.__score == -1.0:
            return "Ungraded"
            return f"{self.__score}/100"

    

print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grades(95)
print(f"Alex's Files: {student1.view()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grades(88)
print(f"Adelle's Files: {student2.view()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Juan's Files: {student3.view()}\n")

print("--- TEST SCENARIO 4: Removing Files after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grades(75)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grades(100)
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
