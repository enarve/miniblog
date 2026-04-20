from flask import Flask, render_template, url_for

app = Flask(__name__)

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
    
if __name__ == '__main__':
    app.run(debug=True)