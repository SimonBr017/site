from flask import Blueprint, render_template
from .utils import versioned_file

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html', versioned_file=versioned_file)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')