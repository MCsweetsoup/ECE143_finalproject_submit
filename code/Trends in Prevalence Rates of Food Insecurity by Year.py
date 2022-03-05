from tkinter import Y
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

#read data
#Change to project directory
PROJECT_ROOT_DIR = "/Users/mcsweetsoup/Desktop/ECE143_finalproject_submit/"

#Read in data
fname = PROJECT_ROOT_DIR + 'data/Trends in Prevalence Rates of Food Insecurity by Year.csv'
#plot data'
data = pd.read_csv(fname)

#plot data
plt.figure(figsize=(7,7))

#Food Insecure People Plot
plt.plot(data['Food insecurity '], label = r'Food Insecure', c = '#f8c928', linewidth = 4)

#Very low food security plot
plt.plot(data['Very low food security'], label = r'Very Food Insecure', c = '#c35b7e', linewidth = 4)

year = range(1995,2020)

ind = np.arange(len(year))

#make the plot
#label tick marks
plt.xticks(ind, year, rotation = 90)
plt.locator_params(axis="x", nbins=8)

#mark important year line dates from 1995-2020
plt.axvline(x = 14, color = 'black', ls = ':', alpha = 0.75)
plt.annotate('2009 Great Recession', rotation = 90, xy = (14.2, 0.5), fontsize = 11)

#mark important percentages
plt.axhline(y = 12, color = 'red', ls = '--' ,alpha = 0.5 )
plt.annotate('Severe Food Insecurity', xy = (0, 12.2), fontsize = 11, color = 'red')
plt.axhline(y = 5, color = 'red',ls = '--', alpha = 0.5)
plt.annotate('Severe Very Food Insecure', xy = (0, 5.2), fontsize = 11, color = 'red')

#place legend
plt.legend(loc='upper right')

#plot x,y axis and title
plt.xlabel("Year")
plt.ylabel("Percentage of US Households %")
plt.title('Trends in Prevalence Rates of Food Insecurity by Year')

#adjust the ylimit
plt.ylim(0, 18)
plt.show()