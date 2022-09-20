# Estimating the number of turns required for the probability of getting a head to be equal to the theoretical probability
import random
import seaborn as sns

numTurn=int(input("Enter number of tosses (Default:100000): ") or 100000) # Number of experiments(coin tosses)
heads=0 # Count head outcomes
tails=0 # Count tail outcomes
sequence=[1,2] # Representation of H&T. 1-> Heads, 2 -> Tails
probH=list() # List of cumulative probabilites of H outcome
probT=list() # List of cumulative probability of T outcome

i=0
while i < numTurn:
    outcome=random.choice(sequence)
    if outcome == 1:
        heads+=1
    elif outcome==2:
        tails+=1
    else:
        print("Something went drastically wrong.")
    probH.append(heads/(heads+tails))
    probT.append(tails/(heads+tails))
    i+=1

print("Final Probabilies: ")
print("1. Heads: ", probH[(numTurn-1)])
print("2. Tails: ", probT[(numTurn-1)])

## Explicit results
#print("Heads: ", probH)
#print("Tails: ", probT)

# Draw Graph

