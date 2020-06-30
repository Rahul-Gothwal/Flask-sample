from flask import Flask, render_template, url_for

app = Flask(__name__)

posts= [
    {'author':'Rahul',
    'title':'Man must explore, and this is exploration at its greatest',
    'subtitle':'Problems look mighty small from 150 miles up',
    'date_posted':'September 24, 2018'},
    {'author':'Rahul',
    'title':'I believe every human has a finite number of heartbeats. I dont intend to waste any of mine.',
    'subtitle':'',
    'date_posted':'September 24, 2018'},
    {'author':'Rahul',
    'title':'Science has not yet mastered prophecy',
    'subtitle':'We predict too much for the next year and yet far too little for the next ten.',
    'date_posted':'September 24, 2018'},
    {'author':'Rahul',
    'title':'Failure is not an option',
    'subtitle':'Many say exploration is part of our destiny, but it’s actually our duty to future generations.',
    'date_posted':'September 24, 2018'}
    ]



@app.route("/")
def home():
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)