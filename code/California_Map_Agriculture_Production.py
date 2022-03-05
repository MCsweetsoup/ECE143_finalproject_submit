from pydoc import visiblename
import pandas as pd #For reading in data
import pgeocode #For converting zip code to longitude/latitude
import matplotlib.pyplot as plt #for plotting
import plotly.figure_factory as ff
import matplotlib.image as mpimg
import os

#Change to project directory
PROJECT_ROOT_DIR = "C:\School\ECE_143\Final_Project\\"

california_img = mpimg.imread(PROJECT_ROOT_DIR + 'image\\' + 'cal-counties-agriculture-productin.jpg')
plt.imshow(california_img)
plt.title("California Agriculture Production by County")
plt.axis('off')
plt.show()