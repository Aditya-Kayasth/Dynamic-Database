
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

engine = create_engine(os.getenv("DB_CONNECTION"),echo=True)

# Using the engine to connect and execute a query
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    
    # Convert rows to a list of dictionaries


    result_dicts = [dict(row) for row in result.mappings()] # We could used a 
    

