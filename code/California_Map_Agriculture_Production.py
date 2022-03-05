from pydoc import visiblename
import pandas as pd #For reading in data
import pgeocode #For converting zip code to longitude/latitude
import matplotlib.pyplot as plt #for plotting
import plotly.figure_factory as ff
import matplotlib.image as mpimg
import os

california_img = mpimg.imread('../image/cal-counties-agriculture-productin.jpg')
plt.imshow(california_img)
plt.title("California Agriculture Production by County")
plt.axis('off')
plt.show()