import pyodbc

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = sqlalchemy.create_engine("mssql+pyodbc://SERVERNAME/DBNAME?driver=SQL+Server+Native+Client+11.0")
df.to_sql('TABLENAME',engine,if_exists = 'replace',index = False,schema='dbo')
