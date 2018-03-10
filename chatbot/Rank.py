from math import log

k1 = 1.2
k2 = 100
b = 0.75
R = 0.0

def bm25(n=0, f=0, qf=0, r=0, N=0, dl=0, avdl=0):
	K = compute_K(dl, avdl)
	idf = log(((r + 0.5) / (R - r + 0.5)) / ((n - r + 0.5) / (N - n - R + r + 0.5)))
	second = ((k1 + 1) * f) / (K + f)
	third = ((k2 + 1) * qf) / (k2 + qf)
	return idf * second * third

def compute_K(dl, avdl):
	return k1 * ((1 - b) + b * (float(dl) / float(avdl)))
