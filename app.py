from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def redir():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/information.html')
def information():
    return render_template('information.html')

@app.route('/contact.html')
def submit():
    return render_template('contact.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    # Extract form data
    name = request.form['name']
    student_number = request.form['studentNumber']
    email = request.form['email']
    grades = request.form['grades']
    satisfaction = request.form['satisfaction']
    improvements = request.form.get('improvements', '')  # Optional field

    # Write form data to "document.txt"
    with open("feedback.txt", "a") as file:
        file.write(f"Name: {name}\nStudent Number: {student_number}\nEmail: {email}\nGrades: {grades}\nSatisfaction: {satisfaction}\nImprovements: {improvements}\n------------------------------------------\n")

    # Redirect or respond to indicate successful submission
    return redirect(url_for('feedback_submitted'))

@app.route('/feedback_submitted')
def feedback_submitted():
    # Render a template or return a response indicating success
    return render_template('feedback_submitted.html')

if __name__ == '__main__':
    app.run(debug=True, port=2132)