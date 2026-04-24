from flask import render_template, url_for, flash, redirect

from miniblog import app
from miniblog.forms import RegistrationForm, LoginForm
from miniblog.models import User, Post

# sample data
posts = [
    {
        'author': 'enarve',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '20 april 2026'
    },
    {
        'author': 'fjarne',
        'title': 'Good weather',
        'content': 'Finally it is raining outside.',
        'date_posted': '20 april 2026'
    }
]

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', posts=posts)
    
@app.route("/about")
def about():
    return render_template('about.html', title='About')
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == '123':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
           flash('Login unsuccessful! Please check username and password.', 'danger') 
    return render_template('login.html', title='Login', form=form)