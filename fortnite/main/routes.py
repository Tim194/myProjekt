from flask import render_template, url_for, flash, redirect
from main import app, db, bcrypt
from main.models import User, Post
from main.forms import RegistrationForm, LoginForm
from flask_login import login_user
import random


posts = [
    {
        "author": "Tim Homlqvist",
        "title": "First blog post",
        "content": "Hello. this is the first post on the blog. I relly hope that this site is gong to be the site to go to if you play fortnite. If you want to contact me do it at Timkon@hotmail.se",
        "date_posted": "sep 4, 2018",
    },
    {
        "author": "Tim Homlqvast",
        "title": "andra blog",
        "content": "Hello world this is from the content dir from the secund blog post",
        "date_posted": "sep 4, 2018"
    }
]

game = [
    {
        "title": "Gray",
        "content": "Only play whit gray wepends and if you want to go hard mode don't yuse meds",
        "vidoe": "https://www.youtube.com/embed/MHNXJEA0u_I",
    },
    {
        "title": "Green",
        "content": "Only play whit green wepends and if you want to go hard mode don't yuse meds",
        "vidoe": "https://www.youtube.com/embed/ptFfMwcfRRk",
    },
    {
        "title": "blue",
        "content": "Only play whit blue wepends and if you want to go hard mode don't yuse meds",
        "vidoe": "https://www.youtube.com/embed/PcDphtl2SDo",
    },
    
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/blog")
def blog():
    return render_template("blog.html", posts=posts, title="Blog")

@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/games")
def games():
    ran = random.randint(0, 2)
    print(ran)
    return render_template("game.html", title="Game", game=game[ran])


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        print("'" + form.username.data + "' has created a accont")
        
        return redirect(url_for("login"))
    
    return render_template("register.html", title="Register", form=form)

@app.route("/login" , methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            
            login_user(user, remember=form.remember)
            
            print("'" + user.username + "' Has loggd in")
            flash('You are now loggd in!', 'success')
            return redirect(url_for("home"))
        else:
            if user:
                print("'" + user.username + "' Has tride loggd in but the passowrd was wrong")
            else:
                print("'" + form.email.data + "' We don't have the email in the databse")
            flash("Login Unsuccessful. Please check username and password", "danger")
        
    return render_template("login.html", title="Login", form=form)
