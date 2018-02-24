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
		return ftrain, ftest, leaf_threshold



def parseDate(file):
	data, metadata = sa.loadaff(file)
	feature_range = []
	for name in metadata.names():
		feature_range.append(metadata[name][1])
	return data, metadata, feature_range


buildtree



