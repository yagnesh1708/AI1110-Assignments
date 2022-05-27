import numpy as py
import math
#The average number of major storms in your city is 2 per year. 
#lets use this question to prove our result

sum=0
for i in range (1,4):
    sum=sum+((math.exp(-2))*(2**i))/math.factorial(i)

if(sum>0.5):
    print ("the result is verified")

