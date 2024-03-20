from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, Optional

# Initialize Flask application
app = Flask(__name__)
# Configure secret key for form security
app.config['SECRET_KEY'] = 'a_very_secret_hash'

# Define a form class using Flask-WTF for feedback submission
class FeedbackForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(message="Your name is required.")])
    studentNumber = StringField('Student Number', validators=[DataRequired(message="Student number is required."), Length(min=4, max=10, message="Student number must be between 4 to 10 characters.")])
    email = StringField('Email Address', validators=[DataRequired(message="Email address is required."), Email(message="Invalid email address.")])
    grades = TextAreaField('Grades Obtained in Your Courses', validators=[DataRequired(message="Grades are required.")])
    satisfaction = SelectField('Overall Satisfaction with Academic Experience', choices=[('', 'Select satisfaction level'), ('excellent', 'Excellent'), ('good', 'Good'), ('average', 'Average'), ('poor', 'Poor')], validators=[DataRequired(message="Please select your satisfaction level.")])
    improvements = TextAreaField('Suggestions for Improvement (Optional)', validators=[Optional()])
    submit = SubmitField('Submit Feedback')

# Route for the homepage, redirects to index.html
@app.route('/')
def redir():
    return render_template('index.html')

# Route for the index page
@app.route('/index.html')
def index():
    return render_template('index.html')

# Route for the information page
@app.route('/information.html')
def information():
    return render_template('information.html')

# Route for the contact page with form for feedback submission
@app.route('/contact.html', methods=['GET', 'POST'])
def submitfeedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        # Save form data to a file upon successful submission
        with open("feedback.txt", "a") as file:
            file.write(f"Name: {form.name.data}\n")
            file.write(f"Student Number: {form.studentNumber.data}\n")
            file.write(f"Email: {form.email.data}\n")
            file.write(f"Grades: {form.grades.data}\n")
            file.write(f"Satisfaction: {form.satisfaction.data}\n")
            file.write(f"Improvements: {form.improvements.data}\n")
            file.write("------------------------------------------\n")

        return redirect(url_for('feedback_submitted'))
    return render_template('contact.html', form=form)

# Route indicating successful feedback submission
@app.route('/feedback_submitted')
def feedback_submitted():
    return render_template('feedback_submitted.html')

if __name__ == '__main__':
    app.run(debug=True, port=2132)