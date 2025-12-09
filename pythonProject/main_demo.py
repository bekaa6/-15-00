# main_demo.py
# Барлық қажетті кластарды импорттау
from student import Student
from teacher import Teacher
from subject import Subject
from report_generator import ParentReport


def run_demo():
    print("--- 📝 School Journal System Demo ---")

    # 1. Initialization
    s1 = Student(1001, "Alice Smith")
    t1 = Teacher(501, "Mr. Harrison")

    math = Subject("MATH101", "Algebra I")
    eng = Subject("ENG101", "English Literature")

    print("\n## Initial Setup")
    print(s1.get_details())

    # 2. Enrollment
    s1.enroll_subject(math.get_code())
    s1.enroll_subject(eng.get_code())
    print(f"\n{s1.get_name()} enrolled in {math.get_code()} and {eng.get_code()}.")

    # 3. Grade Entry (Teacher Action)
    print("\n## Grade Entry (Teacher Action)")

    # Mr. Harrison enters grades for Alice
    t1.enter_grade(s1, math.get_code(), 85.5)
    t1.enter_grade(s1, eng.get_code(), 92.0)
    t1.enter_grade(s1, math.get_code(), 78.0)

    # Try an invalid score (Demonstrating Encapsulation/Validation)
    t1.enter_grade(s1, eng.get_code(), 105.0)

    # 4. Report Generation (Abstraction & Polymorphism)
    print("\n## Report Generation")

    # Generate the official parent report (Using the ParentReport concrete class)
    parent_report = ParentReport()
    parent_report.generate(s1)

    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    run_demo()