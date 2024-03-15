from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def rere():
    return render_template('submit.html')

@app.route('/submit.html')
def information_html():
    return render_template('submit.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    # Capture the form data
    name = request.form['name']
    course = request.form['course']
    short_answer = request.form['short-answer']
    long_answer = request.form['long-answer']
    satisfaction = request.form['satisfaction']
    recommend = request.form['recommend']
    improvements = request.form.get('improvements', 'No suggestions')  # Optional field

    # Save the data to a .txt file
    with open('feedback_results.txt', 'a', encoding='utf-8') as file:
        file.write(f"Name: {name}\nCourse: {course}\nShort Answer: {short_answer}\n")
        file.write(f"Long Answer: {long_answer}\nSatisfaction: {satisfaction}\n")
        file.write(f"Recommend: {recommend}\nImprovements: {improvements}\n")
        file.write("----------\n\n")

    # Redirect to a new page or back to the form
    return redirect(url_for('feedback_submitted'))

@app.route('/feedback_submitted')
def feedback_submitted():
    # Render a template or return a response indicating success
    return "Feedback submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True, port=2132)