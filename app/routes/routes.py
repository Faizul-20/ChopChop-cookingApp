from flask import Blueprint

## "main" adlah blueprint yang di cari __init__ yang ada 
# di application factory di root klo ini di ganti maka di __init__
# harus di ganti juga
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello, Flask is running!"
