from models.report import Report

class ParentReport(Report):
    def generate(self, student, grades, subjects):
        text = f"Report for {student.get_info()}:\n\n"
        if not grades:
            text += "No grades available.\n"
            return text

        for g in grades:
            subj_obj = subjects.get(g.get_subject_id())
            subject = subj_obj.get_title() if subj_obj else f"Subject {g.get_subject_id()}"
            text += f"{subject}: {g.get_value()}\n"
        return text