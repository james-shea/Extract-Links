#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import libraries that we will be using
#BeautifulSoup for extracting data from html
from bs4 import BeautifulSoup
#urllib for working with urls
import urllib
#pandas for working with data
import pandas as pd
#csv for working with csv files
import csv


# In[2]:


#load the website given by the task
census = urllib.request.urlopen("http://www.census.gov/programs-surveys/popest.html")


# In[3]:


#check to ensure url loaded correctly
census


# In[4]:


#Use beautifulsoup to retrieve data
results = BeautifulSoup(census, from_encoding=census.info().get_param('charset'))


# In[5]:


#check that data was retreived correctly
results


# In[6]:


#Write the data retrieved by beautiful soup to text file
with open ('html_code.txt', 'w', encoding = 'utf-8') as html_code:
    html_code.write(str(results))


# In[7]:


#Just double checking
print(results())


# In[8]:


#Put all hyperlinks/hypertexts in a list
weblinks = results.find_all("a")


# In[9]:


#Total links found
len(weblinks)


# In[10]:


weblinks #review the result to see what we are left with


# In[11]:


#create a set for our final run through
final_set = set()


# In[12]:


#This for loop will cycle through and complete tasks as listed below
for link in weblinks:
    
    hyper = str(link.get("href"))
    
    #This stage grabs all links that start with http - relative links will be leftover and dealt with next         
    if hyper.startswith("#http"):
            final_set.add(hyper[1:])
            
    #This stage deals with the relative links that were left above by converting them to absolute urls        
    elif hyper.startswith("/"):
            final_set.add ("https://www.census.gov" + hyper)    
    
    #Alternative cases
    elif hyper.startswith("#") or hyper.startswith("None"):
            ''
            
    #Here we add a '/' to all url's that end with .gov, combined with a set not being able to contain duplicates, 
    #all duplicates are now taken care of                  
    elif hyper.endswith(".gov"):
            final_set.add (hyper + "/")
            
    else:
            final_set.add(hyper)  


# In[13]:


#See how many are left
len(final_set)


# In[14]:


#View set to check data
final_set


# In[15]:


#save all the websites to a csv
with open("unique_websites.csv", 'w', newline= '') as output:
    wr = csv.writer(output, dialect='excel')
    for row in final_set:
        wr.writerow([row])
    output.close()


# In[ ]:




