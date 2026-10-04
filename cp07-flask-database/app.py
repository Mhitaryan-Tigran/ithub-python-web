from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///favourites.db"
app.config["SECRET_KEY"] = "cp07-dev-key"
db = SQLAlchemy(app)

CATEGORIES = {"music": "Музыка", "films": "Фильмы", "books": "Книги"}


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer)
    note = db.Column(db.String(300), default="")


SEED = [
    ("music", "Random Access Memories", "Daft Punk", 2013, "Альбом, под который хорошо пишется код"),
    ("music", "Discovery", "Daft Punk", 2001, ""),
    ("music", "Currents", "Tame Impala", 2015, ""),
    ("films", "Социальная сеть", "Дэвид Финчер", 2010, "История создания Facebook"),
    ("films", "Интерстеллар", "Кристофер Нолан", 2014, ""),
    ("films", "Двухсотлетний человек", "Крис Коламбус", 1999, ""),
    ("books", "Чистый код", "Роберт Мартин", 2008, ""),
    ("books", "Стив Джобс", "Уолтер Айзексон", 2011, "Биография"),
    ("books", "Мастер и Маргарита", "Михаил Булгаков", 1967, ""),
]


@app.cli.command("seed")
def seed():
    db.drop_all()
    db.create_all()
    db.session.add_all(Item(category=c, title=t, author=a, year=y, note=n) for c, t, a, y, n in SEED)
    db.session.commit()
    print(f"Добавлено {len(SEED)} записей")


@app.route("/")
def index():
    counts = {key: Item.query.filter_by(category=key).count() for key in CATEGORIES}
    return render_template("index.html", counts=counts, categories=CATEGORIES)


@app.route("/<category>")
def category(category):
    if category not in CATEGORIES:
        return redirect(url_for("index"))
    items = Item.query.filter_by(category=category).order_by(Item.year.desc()).all()
    return render_template("category.html", items=items, key=category, categories=CATEGORIES)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        form = request.form
        if form.get("category") in CATEGORIES and form.get("title", "").strip() and form.get("author", "").strip():
            year = form.get("year", "").strip()
            db.session.add(Item(category=form["category"], title=form["title"].strip(), author=form["author"].strip(), year=int(year) if year.isdigit() else None, note=form.get("note", "").strip()))
            db.session.commit()
            flash("Запись добавлена")
            return redirect(url_for("category", category=form["category"]))
        flash("Заполните категорию, название и автора", "error")
    return render_template("add.html", categories=CATEGORIES)


@app.post("/delete/<int:item_id>")
def delete(item_id):
    item = db.get_or_404(Item, item_id)
    key = item.category
    db.session.delete(item)
    db.session.commit()
    flash("Запись удалена")
    return redirect(url_for("category", category=key))


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
