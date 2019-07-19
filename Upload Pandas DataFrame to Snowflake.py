
import snowflake.connector 
from snowflake.connector import DictCursor
import pandas as pd




import snowflake.connector
con = snowflake.connector.connect(
  user='user',
  password='password',
  account='account',
)
cur = con.cursor()
try:
    cur.execute("drop table DATABASENAME.SCHEMANAME.TABLENAME")
except:pass
finally:
    cur.close()
df.to_sql("TABLENAME",engine_sf,schema="SCHEMANAME",index=False,if_exists="replace")
