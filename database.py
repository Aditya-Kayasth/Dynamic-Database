
#---------------------------------------------------------------------------------------------
# Host: sql12.freesqldatabase.com
# Database name: sql12757501
# Database user: sql12757501
# Database password: eUhn2s2xJf
# Port number: 3306
# LINK: mysql+pymysql://<user>:<password>@<host>:<port>/<databasename>?<options>
#---------------------------------------------------------------------------------------------

from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# Database connection details

load_dotenv()

engine = create_engine(os.getenv("DB_CONNECTION"))

# Using the engine to connect and execute a query

def jobs_dict():

    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        
        # Convert rows to a list of dictionaries


        result_dicts = [dict(row) for row in result.mappings()] # We could have used the .all()
        
    return result_dicts

def load_job_from_db(id):

    with engine.connect() as conn:


        result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))

        row = result.mappings().first()
          # Get the first matching row as a mapping

        return dict(row) if row else None
