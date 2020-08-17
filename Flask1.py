from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def first():
    name = "Tk"
    return render_template('index.html', name=name)


@app.route("/about")
def second():
    return render_template('about.html')


app.run(debug=True)
