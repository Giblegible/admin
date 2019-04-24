from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Andreas Tjendra',
        'title': 'Book 1',
        'content': 'Study content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Harry Potter',
        'content': 'Test content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 80)