import numpy
import scipy
import scipy.io.arff as sa
import sys


def takeInput():
	if len(sys.argv) != 3:
		print("usage: dt-learn <train-set-file> <test-set-file> m")
		invalid_input = true
	else:
		ftrain = str(sys.argv[0])
		ftest = str(sys.argv[1])
		leaf_threshold = int(argv[2])



