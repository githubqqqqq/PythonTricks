#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from pathlib import Path
import os
from datetime import date, datetime, timedelta
import pandas as pd
import time


# In[3]:


pd.__version__


# In[4]:


path_base = '//path/path'
path_ext = '/path/Python Code'
path = Path(path_base + path_ext)
os.chdir(path)


# In[ ]:


engine = create_engine("mssql+pyodbc:// : @BIA_DM")
reserveQuery = open("TestQuery.sql").read()
with engine.connect() as con:
##    ATTEMPTS = 1 ##60 this is the number of attempts
##    DELAY = 1 ## this is how frequently the attempt is scheduled in minutes
    for attempt in range(ATTEMPTS):
        try:
            refresh_date = (pd.read_sql("""select max(dateadd(day,1inq_date))
                                        as refresh_date
                                       from xxxx_data""",
                                       con,
                                       parse_dates=['refresh_date']).
                                       iloc[0, 0])
        except SQLAlchemyError as e:
            refresh_date = None
        if pd.to_datetime(date.today()) == refresh_date:
            print("data is  updated. Running script.")
            break
        else:
            print("data  not refreshed."
                  f" Will try again in {DELAY} minutes.")
            time.sleep(DELAY*60) ##changing it to minutes

    con.execute(reserveQuery)
    daily_reserve = pd.read_sql("select * from #opps", con)


# In[8]:


engine = create_engine("mssql+pyodbc:// : @BIA_DM")
productMap = pd.read_sql("select * from vw_Product_Map",
                         engine, parse_dates=["UpdateTimeStamp"])
productMap.head()


# In[9]:


engine = create_engine("mssql+pyodbc:// : @BIA_DM3")
reserveQuery = open("TestQuery.sql").read()
with engine.connect() as con:
    con.execute(reserveQuery)
    daily_reserve = pd.read_sql("select * from #opps", con)


# In[10]:


daily_reserve.head()


# In[ ]:


####run directly without creating a table
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from pathlib import Path
import os
from datetime import date, datetime, timedelta
import pandas as pd
import time

path_base = '//path/path'
path_ext = '/path'
path = Path(path_base + path_ext)
os.chdir(path)

engine = create_engine("mssql+pyodbc:// : @BIA_DM")
query = open("code_name.sql").read()
with engine.connect() as con:
    con.execute(query) 
##the query needs to be clear, no comments, only queries that generate tables, no print results. when dropping table needs drop table xxx if exists

