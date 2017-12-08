# Code for paper:
# A decision cognizant Kullback–Leibler divergence
# M Ponti, J Kittler, M Riva, T de Campos, C Zor
# Pattern Recognition 61, 470-478, 3, 2017

# Definition for the divergence measures
# Shorthand:	* 't' is tilde (Pt is 'P tilde')
# 				* 'mu' is dominant class
#				* 'clutter' is non-dominant classes
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

from sys import float_info
from math import log

# Calculate difference between Pmu and Ptmu
def DominantDifference(P, Pt):
	mu = P.index(max(P))

	return abs(P[mu] - Pt[mu])

# Calculate regular KL divergence
def KullbackLeiblerDivergence(P, Pt):
	assert len(P) == len(Pt), "P and Pt are of different sizes!"
	assert isclose(sum(P), 1) and isclose(sum(Pt), 1), "P ({}) or Pt ({}) doesn't sum up to 1!".format(sum(P), sum(Pt))

	return sum([Pti*log((Pti+float_info.epsilon)/(Pi+float_info.epsilon)) for Pti, Pi in zip(Pt,P)])

# Calculate decision cognizant KL divergence
def DecisionCognizantDivergence(P, Pt):
	assert len(P) == len(Pt), "P and Pt are of different sizes!"
	assert isclose(sum(P), 1) and isclose(sum(Pt), 1), "P ({}) or Pt ({}) doesn't sum up to 1!".format(sum(P), sum(Pt))

	mu = P.index(max(P)); mut = Pt.index(max(Pt))
	PDC = [P[mu], sum([P[i] for i in range(len(P)) if i != mu and i != mut])]
	if mu != mut:
		PDC.append(P[mut])
	PtDC = [Pt[mu], sum([Pt[i] for i in range(len(Pt)) if i != mu and i != mut])]
	if mu != mut:
		PtDC.append(Pt[mut])
		
	return sum([Pti*log((Pti+float_info.epsilon)/(Pi+float_info.epsilon)) for Pti, Pi in zip(PtDC,PDC)])

# Calculate decision cognizant delta divergence
def DeltaDivergence(P, Pt):
	assert len(P) == len(Pt), "P and Pt are of different sizes!"
	assert isclose(sum(P), 1) and isclose(sum(Pt), 1), "P ({}) or Pt ({}) doesn't sum up to 1!".format(sum(P), sum(Pt))

	mu = P.index(max(P)); mut = Pt.index(max(Pt))
	PDC = [P[mu], sum([P[i] for i in range(len(P)) if i != mu and i != mut])]
	if mu != mut:
		PDC.append(P[mut])
	PtDC = [Pt[mu], sum([Pt[i] for i in range(len(Pt)) if i != mu and i != mut])]
	if mu != mut:
		PtDC.append(Pt[mut])

	return sum([abs(Pti-Pi) for Pti, Pi in zip(PtDC, PDC)])/2.0

# Calculate conditional divergence
def ConditionalDivergence(P, Pt):
	mu = P.index(max(P)); mut = Pt.index(max(Pt))

	if P[mu] > 0.60 and Pt[mut] > 0.60:
		divergence = 1
	elif P[mu] > 0.40 and Pt[mut] > 0.40:
		divergence = 0.5
	else:
		divergence = 0
	if (mut == mu):
		divergence = -1*divergence

	return divergence

# # Calculate regular clutter
# def KullbackLeiblerClutter(P, Pt):
# 	assert len(P) == len(Pt), "P and Pt are of different sizes!"
# 	assert isclose(sum(P), 1) and isclose(sum(Pt), 1), "P ({}) or Pt ({}) doesn't sum up to 1!".format(sum(P), sum(Pt))

# 	mu = P.index(max(P)); mut = Pt.index(max(Pt))
# 	PClutter = [P[i] for i in range(len(P)) if i != mu and i != mut]
# 	PtClutter = [Pt[i] for i in range(len(Pt)) if i != mu and i != mut]

# 	return sum([Pti*log(Pti/Pi) for Pti, Pi in zip(PtClutter,PClutter)])

# # Calculate decision cognizant clutter
# def DecisionCognizantClutter(P, Pt):
# 	assert len(P) == len(Pt), "P and Pt are of different sizes!"
# 	assert isclose(sum(P), 1) and isclose(sum(Pt), 1), "P ({}) or Pt ({}) doesn't sum up to 1!".format(sum(P), sum(Pt))

# 	mu = P.index(max(P)); mut = Pt.index(max(Pt))
# 	PClutter = sum([P[i] for i in range(len(P)) if i != mu and i != mut])
# 	PtClutter = sum([Pt[i] for i in range(len(Pt)) if i != mu and i != mut])

# 	return PtClutter*log(PtClutter/PClutter)
