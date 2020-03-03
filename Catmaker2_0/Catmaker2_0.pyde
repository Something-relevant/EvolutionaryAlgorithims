import string

def CatHead(x,y):
    h1 = createShape()
    h1.beginShape()
    h1.fill(246 - y, 176 - x, 66- x)
    h1.strokeWeight(4)
    h1.stroke(000000)
    h1.vertex(50 + x, 150 - x)
    h1.vertex(50 + x, 50)
    h1.vertex(100,150 - x)
    h1.vertex(400,150 - x)
    h1.vertex(450 - y,50 + x)
    h1.vertex(450 + x,150 - y)
    h1.vertex(450 - x,550)
    h1.vertex(50 + x,550)
    h1.vertex(50 + x, 150 - x)
    h1.endShape()
    
    shape(h1,1,1)
    
def CatEyes(x,y):
    #eyes

    noFill()
    stroke(0 + x, 0 + y, 0 + y)
    strokeWeight(4)
    circle(150,300 -y,100 - x)
    circle(350,300 -y ,100 + x)
    
    fill(x,255,x)
    circle(150,325 +y,50 - x/2)
    circle(350,325 +y,50 + x)

def CatMouth(x,y):
    #nose
    triangle(250 + X,435 - y, 200,380 - x, 300 + x,380)
    stroke(0 + x, 0 + y, 0 + y)
    
    #wh1iskers
    line(205 + x,425 - y, 50,445)
    line(205 + x,445 - y, 50,465)
    line(205 + x,465 - y, 50,485)
    
    line(295 - x,425 + y, 450,445)
    line(295 - x,445 + y, 450,465)
    line(295 -x,465 + y, 450,485)

def setup():
    size(1000,1000)
    color(0)
    textSize(32)

################ GENERATE POPULATION ################
    x = 0
    y = 0
    
    population = []
    #shapes = [CatHead(x,y), CatMouth(x,y), CatEyes(x,y)]
    
    
    
    
    for i in range(100): # change this value for population size
        r = int(random(0, 256))
        x = r
        r = int(random(0,500))
        y = r
    
        population.append(x + y) # DNA
    
    print('initial population', population)
    
    for i in range(1000):
        
        
    ################ ASSESS FITNESS ################
        scores = []
    
        for dna in population:
            # 'fitness' function
            score = 1
                
            if dna <= 10:
                score += 5
                
            if dna <= 50:
                score += 4
            
            if dna <= 100:
                score += 3
                
            if dna <= 200:
                score += 2
            
            if dna <= 255:
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
        
        ################ changes from growing up ################
        enviroment = i * 0.05
        
    
        parent1 = enviroment + mating_odds[int(random(0, len(mating_odds)))]
        parent2 = enviroment - mating_odds[int(random(0, len(mating_odds)))]
        Mutate = int(random(3000))
        
        print('parents', parent1, parent2)
        
    
        
        for i in range(len(population)):
            
            mut = int(random(1,3))
            
            if mut == 1:
                
                if Mutate == 1:
                    parent1 = parent1 - int(random(0, 10))
        
                if Mutate == 2:
                    parent2  = parent2 * int(random(0,8))
                    
                xover1 = parent1 + parent2
                
                children.append(xover1)
        
    
            if mut == 2:

            
                if Mutate == 1:
                    parent1 = parent1 * int(random(0, 5))
        
                if Mutate == 2:
                    parent2  = parent2 + int(random(8, 16))
                    
                xover2 = parent1 - parent2
                
                children.append(xover2)
            
        
            population.pop(0)
            
        
    
        population = children
        print(population)
        
        print("---------------" + "New Gen" + "---------------")
        
        x = population[0]
        y = population[1]
        
        background(255)
        
        CatHead(x,y)
        CatEyes(x,y)
        CatMouth(x,y)
        
        text("Generation" + str(i), width/2, height - 20 );
    


def draw():

    pass
