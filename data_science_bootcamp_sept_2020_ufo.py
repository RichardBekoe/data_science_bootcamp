#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('Data science bootcamp!')


# $$(X^TX)^{-1}X^Ty = \hat{\beta}$$

# In[ ]:


# The Pandas library is for data analysis and data cleaning.
# It is like Excel and Google Sheets
# Option 

import pandas as pd


# In[ ]:


# .read_csv() will pull a .csv file into Pandas
pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')


# In[ ]:


# create a variable that contains the data
# dataframe
ufo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv')


# In[ ]:


ufo.head()


# In[ ]:


ufo['Shape Reported']

# One column is called a Series


# In[ ]:


# most reported shapes
# default values

ufo['Shape Reported'].value_counts(normalize=True)


# In[ ]:





# In[ ]:


# Set to be a different value.
pd.options.display.max_rows = 100


# In[ ]:


ufo


# In[ ]:


#How many missing values do I have in my data?
ufo.isnull().sum()


# In[ ]:


# How many sightings are there per state?
ufo['State'].value_counts()


# In[ ]:


ufo['State'].str.upper().value_counts()


# In[ ]:


pd.to_datetime(ufo['Time'])


# In[ ]:




