# report_generator.py
from abc import ABC, abstractmethod
from student import Student


# Abstraction: Interface for reporting
class ReportGenerator(ABC):
    """Defines the contract for all report types."""

    @abstractmethod
    def generate(self, student: Student):
        pass


# Polymorphism: A concrete implementation of the report
class ParentReport(ReportGenerator):
    """Generates a nicely formatted report for parents."""

    # Polymorphism: Implements the abstract generate method
    def generate(self, student: Student):
        print("\n" + "=" * 40)
        print(f"*** Official Parent Report: {student.get_name()} ***")
        print("=" * 40)

        subject_grades = {}
        # Student-тің инкапсуляцияланған мәліметтерін қолданады
        for grade in student.generate_report():
            code = grade.get_subject_code()
            if code not in subject_grades:
                subject_grades[code] = []
            subject_grades[code].append(grade)

        print("\nIndividual Subject Scores:")
        for code, grades in subject_grades.items():
            print(f"- Subject {code}:")
            for grade in grades:
                print(f"    -> Score: {grade.get_score():.1f}")

        print("\n" + "-" * 40)
        print(f"FINAL SEMESTER AVERAGE (GPA): {student.calculate_gpa():.2f}")
        print("-" * 40)