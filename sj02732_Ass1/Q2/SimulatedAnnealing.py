import random
import math


def function(fun,x,y):
    return eval(fun)

def Min_SimulatedAnnealing(fun,rangex,rangey):
    current = []
    current.append(random.randint(rangex[0], rangex[1]))
    current.append(random.randint(rangey[0], rangey[1]))
    temperature = function(fun, current[0], current[1]) * 2
    factor = 2
    m = 0
    div = 0
    bounds = [0.5, -0.5]
    while temperature > 0.0005:
        for j in range(100):
            temp = []
            randbound = random.randint(0, 1)
            temp.append(current[0] + bounds[randbound])
            temp.append(current[1] + bounds[randbound])
            while (temp[0] > rangex[1]) | (temp[0] < rangex[0]):
                randbound = random.randint(0, 1)
                temp[0] = current[0] + bounds[randbound]
            while (temp[1] > rangey[1]) | (temp[1] < rangey[0]):
                randbound = random.randint(0, 1)
                temp[1] = current[1] + bounds[randbound]
            diff = function(fun, temp[0], temp[1]) - function(fun, current[0], current[1])
            if diff < 0:
                current = temp
            else:
                p = random.randint(1, 100) / 100
                div = diff / temperature
                m = math.exp(-div)
                if p < m:
                    current = temp
        temperature = temperature/factor
    return current[0], current[1], function(fun, current[0], current[1])

def Max_SimulatedAnnealing(fun,rangex,rangey):
    current=[]
    current.append(random.randint(rangex[0],rangex[1]))
    current.append(random.randint(rangey[0],rangey[1]))
    temperature=function(fun,current[0],current[1])*2
    factor=2
    m=0
    div=0
    bounds=[0.5,-0.5]
    while temperature>0.00005:
        for j in range(100):
            temp=[]
            randbound=random.randint(0,1)
            temp.append(current[0]+bounds[randbound])
            temp.append(current[1]+bounds[randbound])
            while (temp[0] > rangex[1]) | (temp[0] < rangex[0]):
                randbound = random.randint(0, 1)
                temp[0]=current[0] + bounds[randbound]
            while (temp[1] > rangey[1]) | (temp[1] < rangey[0]):
                randbound = random.randint(0, 1)
                temp[1]=current[1] + bounds[randbound]
            diff=function(fun,temp[0],temp[1])-function(fun,current[0],current[1])
            if diff>0:
                current=temp
            else:
                p=random.randint(1,100)/100
                div=diff/temperature
                m=math.exp(div)
                if p<m:
                    current=temp
        temperature=temperature/factor
    return current[0],current[1],function(fun,current[0],current[1])

Sphere= '(x**2)+(y**2)'
Rosenbrock='100*(((x**2)-y)**2)+(1-x)**2'
Griewank='(((x**2) + (y**2))/4000)-(math.cos(x)*math.cos(y/math.sqrt(2)))+1'
print('Global Maximum of Sphere',Max_SimulatedAnnealing(Sphere,[-5,5],[-5,5]))
print('Global Maximum of Rosenbrock',Max_SimulatedAnnealing(Rosenbrock,[-2,2],[-1,3]))
print('Global Maximum of Griewank',Max_SimulatedAnnealing(Griewank,[-30,30],[-30,30]))