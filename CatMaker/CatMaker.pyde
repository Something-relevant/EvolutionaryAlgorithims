import string


def setup():
    size(500, 830)
    
    
    population = []
    
    for i in range(3): # change this value for population size
        r = int(random(0, 8))
        c1 = string.ascii_letters[r]
        r = int(random(8, 16))
        c2 = string.ascii_letters[r]
        r = int(random(16, 26))
        c3 = string.ascii_letters[r]
        population.append(c1 + c2 + c3) # DNA
    
    print('initial population', population)
    global population

def draw():

    Rebirth(population)
            
def Rebirth(population):
    
    for i in range(3000):    
 
        scores = []
        
        
        for dna in population:
            # 'fitness' function
            score = 1
            
            if dna[0] == 'c':
                score += 1
            if dna[1] == 'o':
                score += 1
            if dna[2] == 'w':
                score += 1
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
        print(parent1,parent2, 'parents')
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
        
        print('children',children)
        
        print("---------------" + "New Gen" + "---------------")
    
        for i in range(len(population)):
            
            if 'c' in population[i][0]:
                CatHead(0)
            
            if population[i][1] == 'o':
                CatEyes(0)
                
            if population[i][2] == 'w':
                CatMouth(0)
                
            if 'a' or 'b' or 'd' or 'f' or 'h' in population[i][0]:
                CatHead(10)
            
            if 't' or 's' or 'm' or 'n' or 'p' in population[i][1]:
                CatHead(50)
            
            
            if 'w' or 'x' or 'z' or 'y' or 's' in population[i][2]:
                CatHead(50)

    
                
                    
            
                    

def CatHead(x):
    h1 = createShape()
    h1.beginShape()
    h1.fill(246, 176, 66)
    h1.strokeWeight(4)
    h1.stroke(000000)
    h1.vertex(50 + x, 150 - x)
    h1.vertex(50 + x, 50)
    h1.vertex(100,150 - x)
    h1.vertex(400,150 - x)
    h1.vertex(450,50 + x)
    h1.vertex(450 + x,150)
    h1.vertex(450 - x,550)
    h1.vertex(50 + x,550)
    h1.vertex(50 + x, 150 - x)
    h1.endShape()
    
    shape(h1,1,1)
    
def CatEyes(x):
    #eyes

    noFill()
    stroke(0)
    strokeWeight(4)
    circle(150,300,100 - x)
    circle(350,300,100 + x)
    
    fill(0)
    circle(150,325,50 - x/2)
    circle(350,325,50 + x)

def CatMouth(x):
    #nose
    triangle(250 + X,435, 200,380 - x, 300 + x,380)
    
    #wh1iskers
    line(205 + x,425, 50,445)
    line(205 + x,445, 50,465)
    line(205 + x,465, 50,485)
    
    line(295 - x,425, 450,445)
    line(295 - x,445, 450,465)
    line(295 -x,465, 450,485)
