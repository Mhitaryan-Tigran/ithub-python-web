from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from . import db
from .models import STATUSES, Book, User

bp = Blueprint("books", __name__)


def form_data():
    f = request.form
    rating = f.get("rating", "")
    data = {
        "title": f.get("title", "").strip(),
        "author": f.get("author", "").strip(),
        "status": f.get("status") if f.get("status") in STATUSES else "want",
        "rating": int(rating) if rating in {"1", "2", "3", "4", "5"} else None,
        "review": f.get("review", "").strip(),
    }
    return data, (None if data["title"] and data["author"] else "Укажите название и автора.")


def own(book_id):
    book = db.get_or_404(Book, book_id)
    if book.owner_id != current_user.id:
        abort(403)
    return book


@bp.route("/")
def index():
    latest = Book.query.filter(Book.status == "done", Book.review != "").order_by(Book.updated.desc()).limit(6).all()
    stats = {"users": User.query.count(), "books": Book.query.count(), "done": Book.query.filter_by(status="done").count()}
    return render_template("index.html", latest=latest, stats=stats)


@bp.route("/profile")
@login_required
def profile():
    status = request.args.get("status")
    books = [b for b in current_user.books if not status or b.status == status]
    counts = {key: sum(1 for b in current_user.books if b.status == key) for key in STATUSES}
    return render_template("profile.html", books=books, counts=counts, status=status, statuses=STATUSES)


@bp.route("/readers/<int:user_id>")
def reader(user_id):
    user = db.get_or_404(User, user_id)
    return render_template("reader.html", user=user, statuses=STATUSES)


@bp.route("/books/new", methods=["GET", "POST"])
@login_required
def new():
    if request.method == "POST":
        data, error = form_data()
        if error:
            flash(error, "error")
        else:
            db.session.add(Book(owner=current_user, **data))
            db.session.commit()
            flash(f"«{data['title']}» на полке.")
            return redirect(url_for("books.profile"))
    return render_template("book_form.html", book=None, statuses=STATUSES)


@bp.route("/books/<int:book_id>/edit", methods=["GET", "POST"])
@login_required
def edit(book_id):
    book = own(book_id)
    if request.method == "POST":
        data, error = form_data()
        if error:
            flash(error, "error")
        else:
            for key, value in data.items():
                setattr(book, key, value)
            db.session.commit()
            flash("Изменения сохранены.")
            return redirect(url_for("books.profile"))
    return render_template("book_form.html", book=book, statuses=STATUSES)


@bp.post("/books/<int:book_id>/delete")
@login_required
def delete(book_id):
    book = own(book_id)
    db.session.delete(book)
    db.session.commit()
    flash(f"«{book.title}» убрана с полки.")
    return redirect(url_for("books.profile"))
