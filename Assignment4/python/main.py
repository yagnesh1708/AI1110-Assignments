#By the solution we showed that given result is true lets verify it in a dice experiment.
#Let random variable Y=1 represent getting an even number and Y=0 represent getting an odd number in throwing a dice.
#let assume random variable X takes values of dice for that outcome and 
#let x=3 
#Pr(Y=1)=  Pr (Y = 1|X ≤ x) F(x) + Pr (Y = 1|X > x) [1 - F(x)] 


#Pr(Y=1)
Pr=0.5
#F(x)
F=0.5
#Pr (Y = 1|X ≤ x)
PrYx=1/3
#Pr (Y = 1|X > x)
PrY=2/3

if(Pr==PrYx*F+PrY*(1-F)):
    print ("The result is verified and true.")