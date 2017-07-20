import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot

class Graphics():
	'Class to print plots of data'

	def __init__(self,data):
		self.data = data


	def printFigure(self):
		data_to_plot = self.prepData()

		fig = matplotlib.pyplot.figure(1, figsize=(9,6))		
		ax = fig.add_subplot(111)
		bp=ax.boxplot(data_to_plot)
		fig.savefig('fig1.png', bbox_inches='tight')

	def prepData(self):
		lists = list()
		for k,v in self.data.iteritems():
			templist = list()
			for item in v:
				templist.append(float(item))
			lists.append(templist)

		return lists
