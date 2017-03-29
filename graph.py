import matplotlib.pyplot as plt
import numpy as np

#one line function
#f1 = lambda = x: x

class Graph:
	def __init__(self, funk=lambda x: x):
		#self stores a variable to this class
		#we want init in this case because we're passing a variable into this class
		self.eqn = funk

	def plot(self, name="Your Graph"):
		plt.title(name)
		plt.xlabel("x, fool", fontsize=30)
		plt.ylabel("y, god", fontsize=30)

		xmin, xmax = 0, 10
		ymin, ymax = 0, 10
		plt.axis([xmin,xmax,ymin,ymax])

		plt.xticks([0, 2, 4, 6, 8, 10], fontsize=30)
		plt.yticks([0, 2, 4, 6, 8, 10], fontsize=30)
		plt.title(name, fontsize=30)

		indep = np.arange(0, 10, 0.1)
		y = []
		for i in indep:
			y.append(self.eqn(i))
		print 
		plt.plot(indep, y)
		
		fig=plt.gcf()
		plt.show()
		fig.savefig(name + '.png')