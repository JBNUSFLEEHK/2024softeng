from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog_list.html')

@app.route('/about_me')
def aboutme():
    return render_template('about_me.html')

@app.route('/army_life')
def armylife():
    return render_template('armylife.html')


app.run(debug=True)