import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

'''
This graph is about the food Insecurity percent by different races in each month in 2020 in California
data: represent each race percent encounter food insecurity compare to the overall each race in california by month
'''
plt.rcParams.update({'font.size': 20})
data = pd.read_csv('https://raw.githubusercontent.com/MCsweetsoup/ECE143_finalproject_submit/master/data/2022%20food%20insecurity%20vs%20race%20.csv')
# data = pd.read_csv('C:\School\ECE_143\Final_Project\data\\2022 food insecurity vs race .csv')
plt.figure(figsize=(15,8))
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#Asian Plot
plt.plot(data['Asian'][7:12],label=r'Asian',c='#c35b7e')

#white plot
plt.plot(data['white'][7:12],label=r'White',c='#f8c928')

#black plot
plt.plot(data['black'][7:12],label=r'Black',c='#866ba8')

#Hispanic or Latino plot
plt.plot(data['Hispanic or Latino'][7:12], label=r'Hispanic',c='#f13710')

#Other race plot
plt.plot(data['Other race'][7:12],label=r'Other',c='#910736')

ind = np.arange(len(month)) 
# plt.axvline(x=0,color ='black',ls =':',alpha=0.45)
# plt.axvline(x=3,color ='black',ls =':',alpha=0.45)
# plt.axvline(x=6,color ='black',ls =':',alpha=0.45)
# plt.axvline(x=10,color ='black',ls =':',alpha=0.45)
# plt.annotate('Daily Average of 176,740 Covid Cases', rotation = 90, xy = (10.05, 0.5), fontsize = 15)
# plt.axvline(x=11,color ='black',ls =':',alpha=0.45)
# plt.axhline(y=max(data['Asian']),color ='red',ls =':',alpha=0.45)
# plt.axhline(y=data['white'][11],color ='red',ls =':',alpha=0.45)
# plt.axhline(y=max(data['black']),color ='red',ls =':',alpha=0.45)
# plt.axhline(y=data['Hispanic or Latino'][11],color ='red',ls =':',alpha=0.45)
# plt.axhline(y=max(data['Other race']),color ='red',ls =':',alpha=0.45)
plt.xticks(ind, month)
plt.legend(loc='upper left')
plt.xlabel("Month")
plt.ylabel("Percent of Households")
plt.title('Food insecurity rate by race per month in 2020')
plt.ylim(0, 45)
plt.xlim(7,11)
# end for the first graph code


'''
This graph is about the average of the food insercurity in 2020 by different races
'''

name= ["Asian",'White','Black','Hispanic','Other']
average = [data['Asian'].sum()/12,data['white'].sum()/12,data['black'].sum()/12,data['Hispanic or Latino'].sum()/12,data['Other race'].sum()/12]
plt.figure(figsize=(10,7))
plt.bar(name,average,color=['#c35b7e', '#910736', '#866ba8', '#f13710', '#f8c928'])
plt.ylabel("Percent %")
plt.xlabel("Races")
plt.title('Food Insecurity percent by Races in 2020 In California')
# #end for this graph

'''
This graph is the top ten population states in USA for food insecurity percent in 2020 by different races
data: each races encounter food insecurity percent in different states
'''
states= ["CA",'TX','FL','NY','PA','IL','OH','GA','NC','MI']      
California = {}
asian = [i for i in data['Asian_s'] if math.isnan(i) == False]
white = [i for i in data['white_s'] if math.isnan(i) == False]
black = [i for i in data['black_s'] if math.isnan(i) == False]
latino =[i for i in data['Hispanic_s'] if math.isnan(i) == False] 
other = [i for i in data['other_s'] if math.isnan(i) == False]

plt.figure(figsize=(10,7))
ind = np.arange(len(states)) 
width = 0.15
plt.bar(ind,asian,width,color='#c35b7e',label = 'Asian')
plt.bar(ind+width,white,width,color='#910736',label = 'White')
plt.bar(ind+width*2,black,width,color='#866ba8',label = 'Black')
plt.bar(ind+width*3,latino,width,color='#f13710',label = 'Hispanic or Latino')
plt.bar(ind+width*4,other,width,color='#f8c928',label = 'Other race')
plt.xticks(ind, states)
plt.legend(loc='upper right')
plt.ylabel("Percent%")
plt.xlabel("States")
plt.title('Food Insecurity percent in each states with different races')
plt.ylim(5, 50)
plt.show()
#end for this graph
