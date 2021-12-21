# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:22:27 2021

@author: hp
"""
# to read data and displaying it

import pandas as pd
dataset=pd.read_csv("Wuzzuf_jobs.csv")
dataset.describe()
dataset

# to clean dublicated and null values

# a): sorting by title
dataset.sort_values("Title", inplace = True)

#  b): dropping ALL duplicated values

dataset.drop_duplicates(subset ="Title",
                       keep = False , inplace = True)
# to remove rows dublicated
dataset.drop_duplicates()	

# c): clean null values

dataset.dropna()

# another way to drop the rows where all elements are missing 
dataset.dropna(how='all')

# there are no nulls value in the dataset

dataset['Level'].isnull()
print (dataset['Level'].isnull())
 
# to count jobs for each company and displaying it in order 

jobs=dataset['Title'].value_counts()

# sorting company
dataset.sort_values("Title", inplace = True)


# pie chart
import matplotlib.pyplot as plt
plt.pie(jobs)  
plt.show() 



#import numpy as np
import matplotlib.pyplot as plt



# bar chart for title 

data2= {'Xceed ':'    .NET Angular Software Developer', 'Confidential':'  .NET Back-End Web Developer', 'IKEN Technology':'  .NET Developer - Internship',
		'Obeikan Digital Solutions':'  .Net Core Developer'}
Company = list(data2.keys())
Title = list(data2.values())

plt.bar(Company, Title, color ='maroon',
		width = 0.6)

plt.xlabel("company name ")
plt.ylabel("Title of jobs")
plt.title("jobs in different companies")
plt.show()

#bar chart for areas
data = {'Xceed ':'    Maadi', 'Confidential':'  Cairo', 'IKEN Technology':'  Maadi',
		'Obeikan Digital Solutions':'  New Cairo'}
Company = list(data.keys())
Location = list(data.values())

plt.bar(Company, Location, color ='maroon',
		width = 0.6)

plt.xlabel("company name ")
plt.ylabel("location of company")
plt.title("LOcation of different companies")
plt.show()




# to print skills elements

Skills=dataset['Skills'].value_counts()
dataset.sort_values("Skills", inplace = True)

# to convert skills column into list 
skills=dataset.Skills.tolist()
for skill in skills :
    print(skill)
    print ()
