
import pandas as pd
import datetime
import pyodbc

conn = pyodbc.connect('DSN=DSNNAME;Trusted_Connection=yes;')
strQuery='select * from DBNAME.dbo.TABLENAME'

df = pd.read_sql(sql=strQuery, con=conn)
