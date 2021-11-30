from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Porter', 'J.K. Rowling', '9.3')")
# db.commit()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book> {self.title}'


db.create_all()

new_book = Book(id=1, title='Harry Porter', author='J.K. Rowling', rating=9.3)

db.session.add(new_book)
db.session.commit()

all_books = session.query(Book).all()


@app.route('/')
def home():
    return render_template('index.html', all_books=all_books)


@app.route("/add")
def add():
    pass


if __name__ == "__main__":
    app.run(debug=True)
