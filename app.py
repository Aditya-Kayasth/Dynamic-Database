from flask import Flask, render_template, jsonify, request
from database import jobs_dict, load_job_from_db, add_application_to_db

# Initialize the Flask application
app = Flask(__name__)

# Route to fetch all available jobs in JSON format
@app.route('/jobs')
def list_jobs():
    """
    Fetches the list of all jobs as a JSON response.
    This route can be useful for API usage or integrating with other systems.
    """
    result_dicts = jobs_dict()  # Fetch job data from the database
    return jsonify(result_dicts)  # Return the job data as a JSON response

# Home route to display the homepage
@app.route('/')
def hello_world():  # The main entry point of the application
    """
    Displays the homepage with a list of available jobs.
    Fetches job data from the database and passes it to the 'home.html' template.
    """
    result_dicts = jobs_dict()  # Fetch job data from the database
    return render_template('home.html', jobs=result_dicts)  # Render the homepage with job listings

# Route to display details of a specific job
@app.route('/job/<id>')
def show_job(id):
    """
    Displays detailed information about a specific job.
    Parameters:
    - id (str): The ID of the job to fetch details for.
    
    Fetches job data based on the given ID and passes it to the 'job.html' template.
    """
    loaded_job = load_job_from_db(int(id))  # Fetch job details using the job ID
    return render_template("job.html", job=loaded_job)  # Render the job detail page

# Route to handle job application form submissions
@app.route('/job/<id>/apply', methods=['POST'])
def apply_to_job(id):
    """
    Handles the job application form submission.
    Parameters:
    - id (str): The ID of the job being applied to.
    
    Fetches job details and processes the user's form data by saving it to the database.
    Displays an acknowledgment page to the user after successful submission.
    """
    data = load_job_from_db(int(id))  # Fetch job details for the specified job ID
    form_data = request.form  # Retrieve the form data submitted by the user

    add_application_to_db(data, form_data)  # Save the application details to the database

    return render_template("acknowledgement.html", user_form=form_data, data=data)  # Render acknowledgment page

# Route for "About Us" page
@app.route('/about')
def about_us():
    """
    Displays the 'About Us' page.
    This page can include details about the website, its purpose, and its development process.
    """
    return render_template("about-us.html")  # Render the 'about.html' template

# Route for "Contact" page
@app.route('/contact')
def contact_us():
    """
    Displays the 'Contact' page.
    This page can include contact information or a form to reach out to the website admins.
    """
    return render_template("contact-us.html")  # Render the 'contact.html' template

# Entry point for the application
if __name__ == "__main__":
    """
    Starts the Flask application.
    - The host '0.0.0.0' allows access from any network (useful for testing or production on a server).
    - The debug=True enables automatic reloading and error reporting during development.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
