#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas-profiling


# In[ ]:


#1. DataPrep
DataPrep lets you prepare your data using a single library with a few lines of code. 
The DataPrep ecosystem currently consists of three components:
1.Connector:- The connector enables a simple data collection from web APIs by providing a standard set of operations.
2.EDA:-  The EDA component handles the exploratory data analysis,
3.Clean API:- clean API provides functions for efficiently cleaning and validating data."""


# In[2]:


pip install dataprep


# In[4]:


import pandas as pd
from dataprep.eda import create_report
df= pd.read_csv(r"C:\Users\npnpa\Downloads\Dataset\Dataset\data1\Travel.csv")
create_report(df)


# In[ ]:


2. Pandas Profiling
Pandas Profiling generates profile reports from a Pandas DataFrame and enables you to perform EDA.
It has an extensive use case and more tutorials than all of the packages.
With just one line of code, you can generate an EDA report using Pandas Profiling with
descriptive statistics, correlations, missing value, text analysis and more.


# In[3]:


from pandas_profiling import ProfileReport
profile = ProfileReport(df,title="Report")
profile


# In[ ]:


3. SweetViz
SweetViz offers an in-depth EDA (target analysis, comparison, feature analysis, correlation) and 
interactive EDA in two lines of code! In addition, SweetViz allows you to compare two data sets,
such as training and test data sets for your machine learning projects.


# In[2]:


pip install sweetviz


# In[9]:


import sweetviz as sv
Analysis_Report = sv.analyze(df)
Analysis_Report.show_html('Analysis_Report.html', open_browser = False)


# In[10]:


Analysis_Report.show_html()


# In[ ]:


4. AutoViz
Note that you don’t even need Pandas to read the data. AutoViz will load it when you provide the path to the data set. 


# In[12]:


pip install autoviz


# In[13]:


pip install matplotlib


# In[19]:


from autoviz.AutoViz_Class import AutoViz_Class
AV = AutoViz_Class()
df_AV = AV.AutoViz(r"C:\Users\npnpa\Downloads\Dataset\Dataset\data1\Travel.csv")


# In[ ]:




