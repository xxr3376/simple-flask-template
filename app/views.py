#!encoding=utf-8
from app import app_
from app.models import Test
from flask import render_template

@app_.route('/')
def hello():
  return render_template('index.html')
