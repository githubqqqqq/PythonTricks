#!/usr/bin/env python
# coding: utf-8

# In[1]:


##!pip install sweetviz


# In[2]:


import pandas as pd
import datetime
import pyodbc


# In[3]:


conn = pyodbc.connect('DSN=BIA_DM;Trusted_Connection=yes;')
strQuery= """ select * from bi_analytics_dm.dbo.Walden_Top_of_Funnel   """
df = pd.read_sql(sql=strQuery, con=conn)


# In[4]:


##df.info()


# In[23]:


df_sub=df[['Channel','Degree','prob_grp','Complete90Days','Application_Started__c','OpenEmail','ClickAllEmails','OppSFId']].copy()


# # SweetViz

# In[15]:


import sweetviz as sv

my_report=sv.analyze( source=df_sub,
            target_feat = 'Complete90Days',
            feat_cfg = None,
            pairwise_analysis = 'on')

my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"


# # Pands Profiling

# In[ ]:


##!pip install pandas-profiling


# In[7]:


from pandas_profiling import ProfileReport


# In[10]:


profile = ProfileReport(df_sub, title='Pandas Profiling Report', explorative=True)


# In[11]:


profile.to_file("your_report.html")


# In[12]:


##profile.to_notebook_iframe()


# # SpeedML

# In[17]:


##!pip install speedml


# In[18]:


from speedml import Speedml


# In[31]:


df_sub.to_csv("data.csv")


# In[32]:


sml = Speedml("data.csv",  "data.csv",target='Complete90Days', uid='OppSFId')
sml.plot.correlate()
sml.eda()


# # ExploriPy
# 

# In[30]:


##!pip install ExploriPy


# In[33]:


df_sub.info()


# In[36]:


from ExploriPy import EDA
import pandas as pd
CategoricalFeatures = ['Channel','Degree']
eda = EDA(df,CategoricalFeatures,OtherFeatures=['prob_grp'],title='Exploratory Data Analysis for Big Mart Sales III - Based on Item_Outlet_Sales')
eda.TargetAnalysis('Complete90Days')


# In[ ]:




