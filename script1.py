from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/interests/')
def interests():
    return render_template("interests.html")

@app.route('/summary/')
def summary():
    return render_template("summary.html")

if __name__ == "__main__":
    app.run(debug=True)