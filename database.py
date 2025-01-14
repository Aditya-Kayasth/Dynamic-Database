
#---------------------------------------------------------------------------------------------
# Host: sql12.freesqldatabase.com
# Database name: sql12757501
# Database user: sql12757501
# Database password: eUhn2s2xJf
# Port number: 3306
# LINK: mysql+pymysql://<user>:<password>@<host>:<port>/<databasename>?<options>
#---------------------------------------------------------------------------------------------

from sqlalchemy import create_engine, text

# Database connection details

engine = create_engine("mysql+pymysql://sql12757501:eUhn2s2xJf@sql12.freesqldatabase.com:3306/sql12757501?charset=utf8mb4",echo=True)

# Using the engine to connect and execute a query
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    
    # Convert rows to a list of dictionaries


    result_dicts = [dict(row) for row in result.mappings()] # We could used a 
    

