#!/usr/bin/python

from comline import ComLine
from cv import CV

import sys



def main():
	input = ComLine(sys.argv[1:])
	cvFile = CV(input.args.cv)
	cvFile.readText()
	cvFile.printText()

main()

raise SystemExit
