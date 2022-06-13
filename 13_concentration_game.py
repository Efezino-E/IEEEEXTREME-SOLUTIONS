import numpy as np
N = int(input())

dicta = {}
for i in range(0,N):
    dicta[i+1] = []
    
def checker(N,dicta):
    for i in range(1,N+1):
        if len(dicta[i]) == 2:
            print(dicta[i][0],dicta[i][1], flush = True)
            
possible_guesses = np.array([],dtype = int)

for i in range(0,2*N):
    possible_guesses = np.append(possible_guesses,i+1)

for i in range(1,2*N+1,2):
    guess = [possible_guesses[i-1],possible_guesses[i]]
    
    print(guess[0],guess[1], flush = True)
    k = input()
    if k == 'MATCH':
        pass
    else:
        k = k.split(' ')
        dicta[int(k[0])].append(possible_guesses[i-1])
        dicta[int(k[1])].append(possible_guesses[i])
#for i in range(1,N+1):
 #   checker(N,dicta)
    
checker(N,dicta)
print(-1)
