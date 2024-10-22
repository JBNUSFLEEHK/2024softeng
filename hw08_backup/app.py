from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/about_me')
def aboutme():
    return render_template('about_me.html', title="About me")

@app.route('/blog')
def blog_list():

    df = pd.read_csv("data.csv")
    post_list = []
    for i, row in df.iterrows():
        post_list.append({
            "title": row["title"],
            "content": row["content"],
            
        })

    print(post_list)
    return render_template('blog.html', title="blog post",posts=post_list)

@app.route('/naver_blog')
def naverblog():
    return render_template('naver_blog.html', title="naver blog")

@app.route('/army_life')
def armylife():
    return render_template('armylife.html', title="armylife")

app.run(debug=True)
