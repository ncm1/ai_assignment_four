import timeit;
import copy;
import numpy;

def main():
	start_time = timeit.default_timer();
	e = 0.00001;
	y = 0.7;
	i = 0;
	s = [1,2,3,4];
	a = [1,2,3,4];
	T = {(1,1,1):0.2, (1,1,2):0.8, (1,2,1):0.2, (1,2,4):0.8,
		 (2,2,2):0.2, (2,2,3):0.8, (2,3,2):0.2, (2,3,1):0.8,
		 (3,4,2):1.0, (3,3,4):1.0, (4,1,4):0.1, (4,1,3):0.9,
		 (4,4,4):0.2, (4,4,1):0.8};
	r = [0,0,1,0];
	# Original utilities
	Un = [0,0,0,0];
	U = [0,0,0,0];
	pi = [0,0,0,0];

	delta = 1000;
	iter = 0;
	while (e * (1 - y) / y <= delta ):
		iter = iter + 1;
		U = copy.deepcopy(Un); delta = 0;
		i = 0;
		for i in s:
			actionCand = [];
			actionCandArgs = [];
			for j in a:
				sum = 0;
				for k in s:
					try:
						sum = sum + T[i,j,k] * U[k-1];	# sum of policy* next state
						#	print("%f, %f, %f" %(sum, T[i,j,k], U[k-1]))
						#print("(%d, %d, %d) %f" %(i,j,k, sum));
					except KeyError:
						continue;
				actionCand.append(sum); #collect candidates
				actionCandArgs.append([i,j,k]);
			#print("iterating state: %d, %d, %d" %(i,j,k))
			#print("action cand: ", actionCand);
			Un[i-1] = r[i-1] + y*max(actionCand);
			arg = numpy.argmax(actionCand);
			pi[i-1] = actionCandArgs[arg]; #print("Un %f" % Un[i-1]);
			diff = abs(Un[i-1] - U[i-1]); #print("difference: %f" % diff);
			if diff > delta:
				delta = diff;
		# if (iter == 5 or iter == 10 or iter == 15 or iter == 20 or iter == 25):
		# 	print("Iter %d" % iter);
		# 	print("Un {:06.5f}, {:06.5f}, {:06.5f}, {:06.5f}".format(*Un));
		# 	print("pi ",  pi);
	elapsed = timeit.default_timer() - start_time;
	print("Elapsed time (s: %f" % elapsed)
	print("Number of iterations: %d" %iter)
	print("Optimal Utilities Un: {:06.5f}, {:06.5f}, {:06.5f}, {:06.5f}".format(*Un));
	#print("Un: ",Un);
	print("Optimal Policies pi: ",pi);

main();