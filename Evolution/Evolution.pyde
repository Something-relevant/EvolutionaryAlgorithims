#spell a word - assign a variable to each letter and that draws a component of something
#Phenotype is the physical manifestation of what the gene does
#ininite monkey therom

import string

def setup():
    size(500,500, P3D);
    textSize(50);
population = [];

for i in range(111): #population generator , change value for population size
    #ascii = phenetic alphabet
    r = int(random(0, 8));
    c1 = string.ascii_letters[r];
    r = int(random(8, 16));
    c2 = string.ascii_letters[r];
    r = int(random(16, 26));
    c3 = string.ascii_letters[r];
    population.append(c1+c2+ c3); # DNA
    

#print(population);

scores = [];

for dna in population:  #fitness function = how to measure success
    score = 1;
    
    if dna[0] =='c':
        score += 1
    if dna[1] =='o':
        score += 1;
    if dna[2] =='w':
        score += 1;
    
    scores.append(score);
        
for p, s in zip(population, scores):
    print(p,s);
        
mating_odds = [] #the 'parents'

for i in range(len(population)):
    percent = float(scores[i])/sum(scores)*100; #percentage calculator
    #print(percent);
    
    for j in range(int(percent)):
        mating_odds.append(population[i]);
        
parent1 = mating_odds[int(random(0, len(mating_odds)))];
parent2 = mating_odds[int(random(0, len(mating_odds)))];



        
#print(mating_odds);

#reproduction

print(parent1);
print(parent2);

def draw():
    
    pass;
    
  # if c1 + c2 + c3 == 'cow':
  #  background(0);
  #  text(str(frameCount),200,250);
    
