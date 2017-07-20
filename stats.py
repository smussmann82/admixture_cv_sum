from __future__ import print_function

#from collections import defaultdict
from decimal import *

import math

class CVStats():
	'Class for calculating summary statistics on CV output'
	
	def __init__(self, dictoflists):
		self.d = dictoflists
		self.dmeans = dict()
		self.dstdev = dict()
		self.dmed = dict()
		self.dmin = dict()
		self.dmax = dict()

	def calcStats(self):
		for k,l in self.d.iteritems():
			mean = self.calcMeans(l)
			stdev = self.calcStdev(l,mean)
			med = self.calcMed(l)
			self.dmeans[k] = mean
			self.dstdev[k] = stdev
			self.dmed[k] = med
			self.dmin[k] = min(l)
			self.dmax[k] = max(l)
		print(self.dmeans)
		print(self.dstdev)
		print(self.dmed)
		print(self.dmin)
		print(self.dmax)
	
	def calcMeans(self,l):
		total = self.calcSum(l)
		mean = (total/len(l))
		return mean

	def calcSum(self, l):
		total = Decimal()
		for item in l:
			total+=item
		return total

	def calcStdev(self, l, mean):
		vals = list()
		for val in l:
			dev = (val-mean)**2
			vals.append(dev)
		total = self.calcSum(vals)
		temp = total/Decimal((len(l)-1))
		stdev = Decimal(math.sqrt(temp))
		return stdev

	def calcMed(self,l):
		sl = sorted(l)
		llen = len(l)
		i = (llen-1) // 2

		if(llen % 2):
			return sl[i]
		else:
			return Decimal((sl[i] + sl[i+1])/Decimal(2))

	def printStats(self):
		for k,v in self.dmeans.iteritems():
			print(k)
			print(round(v,4))
