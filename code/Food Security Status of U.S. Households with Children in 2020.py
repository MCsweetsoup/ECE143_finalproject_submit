"""
Food Security Status of U.S. Households with Children in 2020
Data comes from : https://www.ers.usda.gov/topics/food-nutrition-assistance/food-security-in-the-u-s/key-statistics-graphics/
"""
import matplotlib.pyplot as plt
# create data
names = ['85.2% Food secure',
         '7.2% Food insecure adults',
         '6.8% Food insecure children', '0.8% Very high food insecure children']
size = [85.2, 7.2, 6.8, 0.8]
# Create a circle at the center of the plot
my_circle = plt.Circle((0, 0), 0.7, color='white')
colors = ['#f8c928','#c35b7e', '#866ba8', '#910736']
plt.figure()
plt.pie(size, colors=colors)
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.title("Food Insecurity of U.S. Households with Children in 2020")

# Show the graph
plt.legend(names, loc="lower center")
# plt.tight_layout()
plt.show()