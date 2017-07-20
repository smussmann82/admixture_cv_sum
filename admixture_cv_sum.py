#!/usr/bin/python

from comline import ComLine
from cv import CV
from graphics import Graphics
from stats import CVStats

import sys



def main():
	input = ComLine(sys.argv[1:])
	cvFile = CV(input.args.cv)
	cvFile.readText()
	cvFile.printText()

	so = CVStats(cvFile.d)
	so.calcStats()
	so.printStats()

	plot = Graphics(cvFile.d)
	plot.printFigure()

main()

raise SystemExit
