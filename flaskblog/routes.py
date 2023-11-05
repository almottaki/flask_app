from datetime import datetime
from flaskblog import app
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

data = [
    {
        'title': 'Looking for a Web-Developer?',
        'doc_title': 'This Web Developer job description sample template is optimized for advertising for a website developer on online job boards or careers pages. It is easy to customize with key duties and responsibilities. Feel free to modify this posting to a web designer job description, or for your specific needs.',
        'title2': 'What is Web-Development?',
        'doc_title2': 'A web developer’s job is to create websites. While their primary role is to ensure the website is visually appealing and easy to navigate, many web developers are also responsible for the website’s performance and capacity.'
    }
]

data2 = [
    {
        'id': 'Blog ID 1',
        'name': 'Mamun',
        'age': '23 year',
        'date_of_birth': 'Date of Birth:- 31-08-2000',
        'gender': 'Gender:- Male',
        'skill': 'Skill:- I am a Full-Stack Developer.'
    },
    {
        'id': 'Blog ID 2',
        'name': 'Mottaki',
        'age': '21 year',
        'date_of_birth': 'Date of Birth:- 16-09-2002',
        'gender': 'Gender:- Male',
        'skill': 'Skill:- I am still studying at Web developer.'
    }
]

data3 = [
    {
        'title': 'What is Web-Development?',
        'doc_title': 'A web developer’s job is to create websites. While their primary role is to ensure the website is visually appealing and easy to navigate, many web developers are also responsible for the website’s performance and capacity.',
        'title2': 'Types of web developers',
        'doc_title2': 'Web developers usually fall under one of three categories: back-end developers, front-end developers, and full-stack developers. Some web developers also work as webmasters. Let’s take a closer look at each of these roles.',
        'doc_title2_1': 'BACK-END WEB DEVELOPERS: Back-end web developers create the website’s structure, write code, and verify the code works. Their responsibilities also may include managing access points for others who need to manage a website’s content.',
        'doc_title2_2': 'FRONT-END WEB DEVELOPERS: Front-end web developers work on the visual part of the website—the pages visitors see and interact with (also known as the user interface). They design the physical layout of each page, integrate graphics, and use HTML and JavaScript to enhance the site. You can gain essential front-end web development skills with Metas Front-End Developer Professional Certificate.',
        'doc_title2_3': 'FULL-STACK DEVELOPERS: Full-stack developers do the work of both a back-end and front-end developer. These developers have the knowledge to build a complete website and may work for organizations that don’t have the budget for a large website team. If youre interested in full-stack web development, consider earning IBMs Full-Stack Developer Professional Certificate.',
        'doc_title2_4': 'WEBMASTERS: Webmasters are essentially website managers. Their primary responsibility is to keep the website updated, ensuring that the links and applications on each page work properly.',
        'title3': 'Web developer career path',
        'doc_title3': 'Many web developers start their careers with a single focus, usually front-end or back-end development. They may move on to be full-stack developers or explore careers in related fields, including project management, computer programming, or graphic design.',
        'title4': 'Web developer tasks and responsibilities',
        'doc_title4': 'As a web developer, you could work for a company or agency, or as a freelancer taking on projects for individual clients. Your tasks will vary depending on your work situation, but day-to-day responsibilities might generally include:',
        'doc_title4_1': [
            '1. Designing user interfaces and navigation menus',
            '2. Writing and reviewing code for sites, typically HTML, XML, or JavaScript',
            '3. Integrating multimedia content onto a site',
            '4. Testing web applications',
            '5. Troubleshooting problems with performance or user experience',
            '6. Collaborating with designers, developers, and stakeholders'
        ]
    }
]


@app.route("/")
@app.route("/web_developer")
def web_developer():
    return render_template('web_developer.html', posts=data)


@app.route("/user")
def user():
    return render_template('user.html', posts=data2)


@app.route("/about")
def about():
    return render_template('about.html', posts=data3)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'Success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'al.mottaki000@gmail.com' and form.password.data == 'pass':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password!', 'danger')
    return render_template('login.html', title='Login', form=form)
