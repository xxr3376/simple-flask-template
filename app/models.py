#!encoding=utf-8
from app.foundation import db

class Test(db.Model):
  id = db.Column(db.Integer, primary_key = True)

  def __repr__(self):
    return '<test>'
