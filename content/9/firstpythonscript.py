import sys
import random
import numpy as np

# calculate the average of gaussian noise, which is centered about 1
# calculate the average until we are within a threshold (first arg)
precision=float(sys.argv[1])
arrsize=100
arr=np.zeros((arrsize,arrsize))
sum=0
val=0
iter=0
while abs(val-1) > precision:
  iter+=1
  for j in range(arrsize):
    for k in range(arrsize):
      arr[j,k]=random.gauss(1,50)

  # add elements to cumulative sum
  for j in range(arrsize):
    for k in range(arrsize):
      sum+=arr[j,k]

  val=sum/iter/arrsize**2
  if iter % 100 == 0:
    diff=abs(1-val)
    print("iteration = ",iter, "value = ", val,"diff = ", diff)

print("Converged to within {:f} after {:d} iterations".format(precision,iter))
