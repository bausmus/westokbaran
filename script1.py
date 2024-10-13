from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('AusmusBaranHomePage.html')

@app.route('/SoftwareInterests/')
def interests():
    return render_template('SoftwareInterests.html')

@app.route('/SoftwareSummary/')
def summary():
    return render_template('SoftwareSummary.html')

if __name__ == "__main__":
    app.run(debug=True)