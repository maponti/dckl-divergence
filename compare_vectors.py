# Code for paper:
# A decision cognizant Kullback–Leibler divergence
# M Ponti, J Kittler, M Riva, T de Campos, C Zor
# Pattern Recognition 61, 470-478, 3, 2017

# compares two probability vectors files with an specified divergence measure

import sys, os, ast

import divergences

if (len(sys.argv) < 4):
	print "Usage: compare_vectors <vectors 1> <vectors 2> <divergence>"
	print "\nAvailable divergence measures:"
	print "\tkl - regular Kullback-Leibler divergence"
	print "\tdckl - decision cognizant Kullback-Leibler divergence"
	print "\tdelta - Delta divergence"
	print "\tif - Conditional divergence"
	sys.exit(-1)

# Open both prob vectors files and the output file
vector1File = open(sys.argv[1], "r")
vector2File = open(sys.argv[2], "r")
outFile = open(sys.argv[1] + ".div", "w")

# Assess the divergence function
if (sys.argv[3] == "kl"):
	divergence = divergences.KullbackLeiblerDivergence
elif (sys.argv[3] == "dckl"):
	divergence = divergences.DecisionCognizantDivergence
elif (sys.argv[3] == "delta"):
	divergence = divergences.DeltaDivergence
elif (sys.argv[3] == "if"):
	divergence = divergences.ConditionalDivergence
else:
	print "{} is not a valid divergence measure!".format(sys.argv[3])
	sys.exit(-1)

# Iterate over both generators
for vector1line, vector2line in zip(vector1File, vector2File):
	# convert vector lines to float lists
	vector1 = ast.literal_eval(vector1line)
	vector2 = ast.literal_eval(vector2line)

	# calculating the specified divergence
	divValue = divergence(vector1, vector2)

	outFile.write(str(divValue) + "\n")
