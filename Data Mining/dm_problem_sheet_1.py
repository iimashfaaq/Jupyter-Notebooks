# -*- coding: utf-8 -*-
"""DM_problem_sheet_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i-5pkFdOAHwePg1FI8r6xEuRgltzm11O

# DM - Assignment 1
By Ashfaaq IIM - 17PW07

(Note: Open this notebook at https://colab.research.google.com for best performance)

##  Import Modules
"""

import matplotlib.pyplot as plt
import pandas as pd

"""## Reading Input Data"""

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Data_set_1.csv')
data.head(5)

"""## Questions

### Question - 1 <br>
<b>Quantitative variables</b> -  Quantitative variables are numerical. They repesent a measurable quantity. <br>
<b>Qualitative variables</b> - Also called as categorical vairable. They aren't numerical. They are more of a description type variable. <br>

From the given dataset,
- Quantitative variables are
    - calories
    - protein
    - fat
    - carbo
    - sugars
    - potass
    - vitamins
    - weight
    - cups
- Qualitative variables are
    - shelf
    - mfr
    - type

### Question - 2

Histograms of association between shelf positions (Bottom, Middle, Top) and sugar content of the cereals from the shelf
"""

import numpy as np
# print(data['shelf'].unique())
top_shelf = data[(data['shelf'] == 'Top')]
middle_shelf = data[(data['shelf'] == 'Middle')]
bottom_shelf = data[(data['shelf'] == 'Bottom')]

fig, axs = plt.subplots(1, 3, figsize=(16,5))
fig.tight_layout()

axs[0].hist(top_shelf['sugars'], bins=14, color='#0504aa', alpha=1, rwidth=0.85)
axs[0].set_xlabel('Sugar Count')
axs[0].set_ylabel('Count of Cereals')
axs[0].set_title('Top Shelf Sugar', fontsize=15)

axs[1].hist(middle_shelf['sugars'], bins=14, color='#050400', alpha=1, rwidth=0.85)
axs[1].set_xlabel('Sugar Count')
axs[1].set_ylabel('Count of Cereals')
axs[1].set_title('Middle Shelf Sugar', fontsize=15)

axs[2].hist(bottom_shelf['sugars'], bins=14, color='#05aa0a', alpha=1, rwidth=0.85)
axs[2].set_xlabel('Sugar Count')
axs[2].set_ylabel('Count of Cereals')
axs[2].set_title('Bottom Shelf Sugar', fontsize=15)

top_shelf['sugars'].mean(), middle_shelf['sugars'].mean(), bottom_shelf['sugars'].mean()

"""### Question - 3

From the histogram, 
- All the three shelves have sugar content ranging from 0 to 14.
- Averages show **middle** shelf has most sugar content (avg of 9.6) followed by **top** (avg of 6.5) and **bottom** (avg of 5.1). 

Hence the order is
- Middle
- Top
- Bottom

### Question - 4
Five-number summary plot for the variable 'fiber'...
"""

# Pandas describe function provides these information
plt.boxplot(data['fiber'])
print("The summary for Fibre:")
print(data['fiber'].describe())
print("\n\nBoxplot is shown to support the summary,")

"""### Question - 5

Scatter plot between calories and carbohydrates
"""

plt.scatter(data['carbo'], data['calories'])
plt.title('Scatter Plot - Calories vs Carbohydrates')
plt.ylabel('Calories')
plt.xlabel('Carbohydrates')
print("Correlation: ", data['carbo'].corr(data['calories']))

"""###Observation
From the scatter plot, we observe that the value of calories increases as the carbohydrates value increases. Therefore, there exists a positive correlation between them but this relationship is weakly positive because the correlation value is close to zero (i.e. 0.25 in our case). <br>
Hence, we can conclude that these two variables have **positive** correlation with **weak** relationship.
"""