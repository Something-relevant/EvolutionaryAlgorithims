import string

def setup():
    size(500, 500)

################ GENERATE POPULATION ################
population = []

for i in range(10): # change this value for population size
    r = int(random(0, 8))
    c1 = string.ascii_letters[r]
    r = int(random(8, 16))
    c2 = string.ascii_letters[r]
    r = int(random(16, 26))
    c3 = string.ascii_letters[r]
    population.append(c1 + c2 + c3) # DNA

print('initial population', population)

for i in range(10000):
    
################ ASSESS FITNESS ################
    scores = []

    for dna in population:
        # 'fitness' function
        score = 1
        
        if dna[0] == 'c':
            score += 5
        if dna[1] == 'o':
            score += 5
        if dna[2] == 'w':
            score += 5
        scores.append(score)
    
    for p, s in zip(population, scores):
        print('fitness score', p, s)
    
    ################ SELECTION ################
    
    mating_odds = [] # the 'parents'
    
    for p, s in zip(population, scores):
        # i've avoided the % method here; i think clive's proposal is fine
        for i in range(int(s)):
            mating_odds.append(p)
    
    print('mating odds', mating_odds) 
    
            
    ################ REPRODUCTION ################
    children = []
    

    parent1 = mating_odds[int(random(0, len(mating_odds)))]
    parent2 = mating_odds[int(random(0, len(mating_odds)))]
    Mutate = int(random(3000))
    

    
    for i in range(len(population)):
        
        x = int(random(1,3))
        
        if x == 1:
            n1 = parent1[0]
            n2 = parent2[1]
            n3 = parent1[2]
            
            if Mutate == 1:
                n1  = string.ascii_letters[int(random(0, 8))]
    
            if Mutate == 2:
                n2  = string.ascii_letters[int(random(8, 16))]
            
            if Mutate == 3:
                n3  = string.ascii_letters[int(random(16, 26))]
                
            xover1 = n1 + n2 + n3
            
            children.append(xover1)
    

        if x == 2:
               
            s1 = parent2[0]
            s2 = parent1[1]
            s3 = parent2[2]
        
            if Mutate == 1:
                s1  = string.ascii_letters[int(random(0, 8))]
    
            if Mutate == 2:
                s2  = string.ascii_letters[int(random(8, 16))]
            
            if Mutate == 3:
                s3  = string.ascii_letters[int(random(16, 26))]
                
            xover2 = s1 + s2 + s3
            
            children.append(xover2)
        
    
        death = 0
        population.pop(death)
    
        death += 1

    population = children
    print(population)
    
    print("---------------" + "New Gen" + "---------------")



def draw():

    pass
