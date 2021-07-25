from datetime import datetime
from app import db

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), index=True, unique=True)
   author_name = db.Column(db.Integer, db.ForeignKey('author.name'))
   description = db.Column(db.Text)
   authors = db.relationship("Author", backref="book", lazy="dynamic")
   users = db.relationship("User", backref="user", lazy="dynamic")

   def __str__(self):
       return f"<User {self.title}>"


class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(200), index=True, unique=True)
   book_title = db.Column(db.Integer, db.ForeignKey('book.title'))
   books = db.relationship("Book", backref="author", lazy="dynamic")

   def __str__(self):
       return f"<Post {self.name}>"


class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(200), index=True, unique=True)
   borrowed = db.Column(db.DateTime, index=True, default=datetime.utcnow)
   returned = db.Column(db.DateTime, index=True, default=datetime.utcnow)
   book_title = db.Column(db.Integer, db.ForeignKey('book_title'))

   def __str__(self):
       return f"<Post {self.name}>"