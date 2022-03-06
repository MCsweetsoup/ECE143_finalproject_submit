# ECE 143 Final Project
Food Insecurtiy<br>

# Authors
Tanvir Hussain<br>
Zehua Tang<br>
Haoyan Xin<br>
Lingxi Li<br>
Krystal Chan<br>


# Overview
Food security is a measure of an individual’s ability to access healthy and nutritious food; food insecurity or the lack of access to healthy food is a persistent issue around the globe. Society recognizes the problem of food insecurity yet it is unclear what are the significant factors. The cause of food insecurity is manifold. Social, political, and economical reasons are easy to identify, but the order of importance is often debated. With the unprecedented strike of COVID-19, food insecurity has become relevant now more than ever when lack of access to nutritional food has skyrocketed. With the bloom of big data, our ability to better understand the reasons behind food insecurity has been greatly enhanced. In our work, we wish to analyze and rank different factors that potentially contribute to food insecurity in order to strongly correlate food insecurity to relevant factors, and even offer possible solutions to some of the challenges. 

# Data source
We wish to use a combination of multiple datasets studying aspects of food insecurity. One such example is the United States Census Bureau's Pulse Survey. These datasets contain racial, ethnic, and geographical and socioeconomic status of respondents which can be correlated to their level of food security. There are also recent datasets regarding the impact of COVID-19 on food insecurity.

# Third party
panda<br>
numpy<br>
matplotlib.pyplot<br>
matplotlib<br>
folium<br>
plotly<br>
pgeocode<br>
plotly-geo<br>
geopandas<br>
tkinter<br>
mpltoolkits<br>


# File Structure
Code: This folder contains all scripts used for generating visualizations. A detailed explanation of each file is provided in code description sections.

Data: This folder contains all raw data csv file. A detailed explanation of each dataset we have used is given in dataset description section. 

Image: This folder contains all visualizations used for final presentation. 

# Code Description
California_Map.py: This script loads all food bank locations and superimposes them onto a heatmap of California food insecure rates in different county. Run $python California_Map.py to get the result.

California_Map_Food_Banks.py: This script generates a map California with various food bank locations superimposed on it. Run python California_Map_Food_Banks.py to get the result.

Food Security Status of U.S. Households with Children in 2020.py: This script generates a pie chart with three levels of food insecurity for family with children. Run $python Food Security Status of U.S. Households with Children in 2020.py to generate the result.

Trends in Prevalence Rates of Food Insecurity by Year.py: This script generates a plot with trends of food insecurity levels over a span of 20 years. Two levels of insecurities are plotted: food insecure and very food insecure. Also some notable timestamps have been marked out, such as 2009 Great Recession. Run $python Trends in Prevalence Rates of Food Insecurity by Year.py to get the result. 

US heatmap with food insecurity percentage.py: This script plots a heatmap over the entire US, with food insecurity level of each state drawn out. Run $python US heatmap with food insecurity percentage.py to get the visualization.

nick_food_insecurity.py: This script plots a heatmap of food insecurity level by different counties in California. Run $python nick_food_insecurity.py to see the result.

nick_poverty.py: This script contains a heatmap of California poverty level of different counties. Run $python nick_poverty.py to the result. 

zehua.py: Generate 3 graphs in total. The first is food insecure family percentage by race or ethinicity and by month in California. The second is average food insecure family percentage by race. The thrid graph is the top 10 states with food insecure family. Run $python zehua.py to get the results.


# Dataset Description
"county food insercuity in CA.csv": dataset of the people have food insecurity problem for each county in California<br>
https://map.feedingamerica.org/county/2019/overall/california<br>

"2022 food insecurity vs race .csv":It contains two datasets<br>
First dataset: It contains the people have food insecurity on different race  compare to its own race population in California on each month in 2020<br>
Second dataset: It contains the people have the food insecurity on different race by each states in 2020<br>
https://www.ipr.northwestern.edu/state-food-insecurity.html<br>

"States percents.csv": dataset of the percent of each states in USA that have food insecurity<br>
https://www.ipr.northwestern.edu/state-food-insecurity.html<br>

"Trends in Prevalence Rates of Food Insecurity by Year.csv" : data set of percentage of people in US that are food insecure from 1995-2020<br>
https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-u-s/key-statistics-graphics/#:~:text=in%20Excel%20format.-,Trends%20in%20Prevalence%20Rates,to%2010.5%20percent%20in%202019<br>

