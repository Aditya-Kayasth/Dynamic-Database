from sqlalchemy import create_engine, text
# from sqlalchemy.exc import SQLAlchemyError  # Uncomment if you want to handle specific SQLAlchemy errors
import os
from dotenv import load_dotenv  # Used to load environment variables from a .env file
# import logging  # Uncomment if you want to add logging for debugging purposes
# logging.basicConfig(level=logging.DEBUG)  # Example logging configuration

# Load environment variables from a .env file
load_dotenv()

# Create a database engine using the connection string from environment variables
engine = create_engine(os.getenv("DB_CONNECTION"))  # Ensure the .env file contains DB_CONNECTION=<your_connection_string>

# Test the database connection by executing a simple query
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))  # Executes a simple query to check the connection
    print(result.scalar())  # Outputs the result (should print '1' if successful)

# Function to fetch all jobs from the database
def jobs_dict():
    """
    Fetches all job listings from the 'jobs' table.
    Returns:
        A list of dictionaries, where each dictionary represents a job record.
    """
    with engine.connect() as conn:  # Establish a connection to the database
        result = conn.execute(text("SELECT * FROM jobs"))  # Execute the query to fetch all jobs
        # Convert rows to a list of dictionaries using result.mappings()
        return [dict(row) for row in result.mappings()]  # Return the list of job records

# Function to fetch details of a specific job based on its ID
def load_job_from_db(id):
    """
    Fetches details of a specific job from the 'jobs' table based on the given ID.
    Parameters:
        id (int): The ID of the job to fetch.
    Returns:
        A dictionary representing the job details, or None if the job does not exist.
    """
    with engine.connect() as conn:  # Establish a connection to the database
        query = text("SELECT * FROM jobs WHERE id = :id")  # SQL query to fetch the job by ID
        result = conn.execute(query, {"id": id})  # Execute the query with the provided job ID
        row = result.mappings().first()  # Get the first result (if any)
        return dict(row) if row else None  # Return the job details as a dictionary, or None if not found

# Function to add a job application to the database
def add_application_to_db(data, form_data):
    """
    Inserts a new job application into the 'applications' table.
    Parameters:
        data (dict): The job data (containing job ID and other details).
        form_data (dict): The form data submitted by the user (name, email, LinkedIn, etc.).
    """
    with engine.connect() as conn:  # Establish a connection to the database
        query = text("""
            INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
            VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
        """)  # SQL query to insert application data into the 'applications' table
        # Execute the query with the provided job and form data
        conn.execute(query, {
            "job_id": data['id'],  # ID of the job being applied to
            "full_name": form_data['name'],  # Applicant's full name
            "email": form_data["email"],  # Applicant's email address
            "linkedin_url": form_data["linkedin"],  # Applicant's LinkedIn profile URL
            "education": form_data["education"],  # Applicant's educational background
            "work_experience": form_data["work_experience"],  # Applicant's work experience
            "resume_url": form_data["resume"]  # URL of the applicant's resume
        })
        conn.commit()  # Commit the transaction to save the changes to the database
