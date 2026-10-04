from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///group.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), unique=True, nullable=False)
    speciality = db.Column(db.String(120), nullable=False)
    students = db.relationship("Student", back_populates="group", order_by="Student.last_name")


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    hair = db.Column(db.String(30))
    eyes = db.Column(db.String(30))
    hobby = db.Column(db.String(80))
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable=False)
    group = db.relationship("Group", back_populates="students")


STUDENTS = [
    ("Мхитарян", "Тигран", "мужской", 18, "чёрные", "карие", "macOS-приложения"),
    ("Алексеева", "Мария", "женский", 18, "русые", "серые", "рисование"),
    ("Борисов", "Даниил", "мужской", 19, "каштановые", "зелёные", "футбол"),
    ("Волкова", "Анна", "женский", 18, "светлые", "голубые", "фотография"),
    ("Григорьев", "Илья", "мужской", 18, "тёмные", "карие", "киберспорт"),
    ("Дмитриева", "София", "женский", 19, "рыжие", "зелёные", "музыка"),
    ("Егоров", "Артём", "мужской", 18, "русые", "серые", "3D-моделирование"),
    ("Захарова", "Полина", "женский", 18, "чёрные", "карие", "танцы"),
]


@app.cli.command("seed")
def seed():
    Student.query.delete()
    Group.query.delete()
    group = Group(code="ИСП9-Kh36", speciality="09.02.07 Информационные системы и программирование")
    db.session.add(group)
    for last, first, gender, age, hair, eyes, hobby in STUDENTS:
        db.session.add(Student(last_name=last, first_name=first, gender=gender, age=age, hair=hair, eyes=eyes, hobby=hobby, group=group))
    db.session.commit()
    print(f"Группа {group.code}: {len(STUDENTS)} студентов")


@app.route("/")
def index():
    group = Group.query.first()
    gender = request.args.get("gender")
    students = [s for s in (group.students if group else []) if not gender or s.gender == gender]
    ages = [s.age for s in students]
    return render_template("index.html", group=group, students=students, gender=gender, avg_age=sum(ages) / len(ages) if ages else 0)


@app.route("/student/<int:student_id>")
def student(student_id):
    return render_template("student.html", s=db.get_or_404(Student, student_id))


if __name__ == "__main__":
    app.run(debug=True)
