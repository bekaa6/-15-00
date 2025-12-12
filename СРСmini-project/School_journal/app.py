from flask import Flask, render_template, request, redirect, url_for, flash
from models.student import Student
from models.grade import Grade
from models.journal import SchoolJournal
from models.parent_report import ParentReport

app = Flask(__name__)
app.secret_key = "change-me-to-a-secure-random-key"
journal = SchoolJournal.get_instance()

@app.route("/")
def index():
    return render_template("index.html", students=journal.students)

@app.route("/add_student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        try:
            sid = int(request.form["id"])
            name = request.form["name"].strip()
            age = int(request.form["age"])
            class_num = request.form["class"].strip()
        except Exception as e:
            flash("Invalid input: please check the fields.", "danger")
            return redirect(url_for("add_student"))

        student = Student(sid, name, age, class_num)
        journal.add_student(student)
        flash(f"Student {name} (id={sid}) added.", "success")
        return redirect(url_for("index"))
    return render_template("add_student.html")

@app.route("/add_grade", methods=["GET", "POST"])
def add_grade():
    if request.method == "POST":
        try:
            gid = int(request.form["id"])
            sid = int(request.form["student_id"])
            subject = int(request.form["subject"])
            value = int(request.form["value"])
        except Exception as e:
            flash("Invalid input: please check the fields.", "danger")
            return redirect(url_for("add_grade"))

        # Optional: check student exists
        if sid not in journal.students:
            flash(f"Student with id={sid} not found.", "warning")
            return redirect(url_for("add_grade"))

        grade = Grade(gid, sid, subject, value)
        journal.add_grade(grade)
        flash(f"Grade {value} for student {sid} added.", "success")
        return redirect(url_for("index"))
    return render_template("add_grade.html", subjects=journal.subjects)

@app.route("/report/<int:id>")
def report(id):
    student = journal.students.get(id)

    if not student:
        return "Student not found!", 404

    grades = journal.get_grades_for_student(id)
    report = ParentReport()
    text = report.generate(student, grades, journal.subjects)

    return render_template("report.html", text=text)

if __name__ == "__main__":
    app.run(debug=True)