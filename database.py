from sqlalchemy import create_engine, text
# from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv
# import logging
# logging.basicConfig(level=logging.DEBUG)


# Load environment variables
load_dotenv()

# Create database engine
engine = create_engine(os.getenv("DB_CONNECTION"))

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.scalar()) 

def jobs_dict():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        # Convert rows to a list of dictionaries
        return [dict(row) for row in result.mappings()]

def load_job_from_db(id):
    with engine.connect() as conn:
        query = text("SELECT * FROM jobs WHERE id = :id")
        result = conn.execute(query, {"id": id})
        row = result.mappings().first()
        return dict(row) if row else None


def add_application_to_db(data,form_data):

    with engine.connect() as conn:
        query = text("""
            INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
            VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
        """)
        conn.execute(query, {
            "job_id": data['id'],
            "full_name": form_data['name'],
            "email": form_data["email"],
            "linkedin_url": form_data["linkedin"],
            "education": form_data["education"],
            "work_experience": form_data["work_experience"],
            "resume_url": form_data["resume"]
        })
        conn.commit()



