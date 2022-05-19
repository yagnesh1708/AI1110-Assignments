import matplotlib.pyplot as plt
import numpy as np

#let the probability of drawing a defective one from each box be 

defe = {1:0.05,2:0.4,3:0.1,4:0.1}


#the probability of selecting each box is 

sel=0.25

#the probability of drawing a defective one 

prob=sel*defe[1]+sel*defe[2]+sel*defe[3]+sel*defe[4]

plt.stem(['Y=0(defective)','Y=1(nondefective)'],[prob,(1-prob)])

plt.ylabel('probability')
plt.xlabel('Y')
plt.title('pmf')
plt.show()

print ('probability of drawing defective one is ',prob)

#given a defective one is drawn probability of it being from a  box is


proba= [defe[1]*sel/prob,defe[2]*sel/prob,defe[3]*sel/prob,defe[4]*sel/prob]

plt.stem(['X=0|Y=0','X=1|Y=0','X=2|Y=0','X=3|Y=0'],proba)
plt.xlabel('boxes')
plt.ylabel('probability')
plt.title('pmf')
plt.show()

print('the probablity of it being drawn from 2nd box is',proba[1])




