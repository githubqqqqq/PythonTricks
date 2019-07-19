
import snowflake.connector 
from snowflake.connector import DictCursor
import pandas as pd
import datetime
import pyodbc



ACCOUNT = 'act'
USER = 'username'
PASSWORD = 'pswd'

con = snowflake.connector.connect(
  user=USER,
  password=PASSWORD,
  account=ACCOUNT
)
cur=con.cursor(DictCursor)
results = cur.execute("select * from database.schema.table  ").fetchall()
df=pd.DataFrame(results)