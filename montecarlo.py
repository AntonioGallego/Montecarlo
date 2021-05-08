'''
Antonio Gallego May 2021
Wonderful article on Montecarlo methods found in Hacker News
https://ggcarvalho.dev/posts/montecarlo/
The code was Go, as an exercise I rewrote it in Python
https://en.wikipedia.org/wiki/Monte_Carlo_method
https://en.wikipedia.org/wiki/Monty_Hall_problem'
'''

from random import random,randint,choice,normalvariate
import math

class Point(object):
    '''Creates a point on a coordinate plane with values x and y.'''
    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.x = x
        self.y = y
    def __str__(self):
        return "Point(%s,%s)" % (self.x, self.y)

def euler():
    'Try adding random numers between 0-1 until sum>1, that sum averages to e'
    n=0
    rounds=0
    while n<1:
        n += random()
        rounds +=1
    return rounds

def birthdayParadox(PEOPLE,tries):
    success=0
    for i in range(tries):
        birthdays = {}
        for j in range(PEOPLE):
            try:
                birthday = randint(1,365)
                birthdays[birthday] += 1 # if it exists I add 1, ski
                success += 1
                break
            except:
                birthdays[birthday] = 1 # first appearece of this birthday
    bApprox = success/tries
    return bApprox

def f_to_be_integrated(x):
    return math.exp(-x * x)  # 1.77 = sqrt(pi) [-20,20]
    # return (x*x)+1 # 14/3 = 4.666 [0,2]

def montecarlo_integrator(f,a,b,tries):
    area = 0
    for i in range(tries):
        area += f(a+((b-a)*random()))
    area*=(b-a)/tries
    return area

def gaussian(x):
    return (1 / math.sqrt(2*math.pi)) * math.exp(-0.5*x*x)

def bsmCallValue(S0, K, T, r, sigma, n):
    d1 = math.log(S0/K) + T*(r+0.5*sigma*sigma)/(sigma*math.sqrt(T))
    d2 = math.log(S0/K) + T*(r-0.5*sigma*sigma)/(sigma*math.sqrt(T))
    mciD1 = montecarlo_integrator(gaussian, -20.0, d1, n)
    mciD2 = montecarlo_integrator(gaussian, -20.0, d2, n)
    return S0*mciD1 - K*math.exp(-r*T)*mciD2

def rectifier(x):
    'calculates max(x, 0)'
    if x >= 0.0:
        return x
    return 0.0

def main():
    print("Pi's Montecarlo approach")
    success = 0
    points = 100000
    for i in range(points):
        p = Point(2*random()-1, 2*random()-1)
        # Check if point lies within the circular region:
        if  p.x * p.x + p.y * p.y < 1:
            success += 1
    piApprox = 4.0 * (success/points)
    errorPct = 100.0 * abs(piApprox - math.pi) / math.pi
    print("After {} rounds Pi approaches {}".format(points,piApprox))
    print("Error {:.2f}%".format(errorPct))
    print()

    print("Euler's number")
    tries=100000
    total=0
    for i in range(tries):
        total+=euler()
    eApprox = total/tries
    errorPct = 100.0 * abs(eApprox - math.e) / math.e
    print("After {} rounds e approaches {}".format(tries,eApprox))
    print("Error {:.2f}%".format(errorPct))
    print()


    print("Birthday's Paradox")
    PEOPLE = 23
    tries = 1000
    bApprox = birthdayParadox(PEOPLE, tries)
    print("After {} rounds probability of birthday collision for a group of size {} approaches {}%".format(tries,PEOPLE,bApprox))
    print("n\tP(n)")
    for PEOPLE in (1,5,10,20,23,30,40,50,60,70,75,100,366):
        bApprox = birthdayParadox(PEOPLE, tries)
        print("{}\t{:.2f}%".format(PEOPLE,bApprox*100))
    print()

    print("Monty Hall Problem")
    tries = 10000
    # No-Switch Doors, pure random Strategy expected success 33%
    success = 0
    for i in range(tries):
        slots = list(range(1,4))
        car=choice(slots)
        slots.remove(car)
        goat1 = choice(slots)
        slots.remove(goat1)
        goat2 = slots.pop()
        firstChoice = randint(1,3)
        if firstChoice==car:
            success+=1
    noChangeSuccess=success/tries
    print("After {} games 'no-switch' success approaches {:.2f}%".format(tries, noChangeSuccess))
    # Switch Doors Strategy, expected success 66%
    success = 0
    for i in range(tries):
        slots = list(range(1,4))
        car=choice(slots)
        slots.remove(car)
        goat1 = choice(slots)
        slots.remove(goat1)
        goat2 = slots.pop()
        firstChoice = randint(1,3)
        #calculating second choice
        slots = list(range(1, 4))
        slots.remove(firstChoice)
        if goat1 in slots:
            slots.remove(goat1)
        else:
            slots.remove(goat2)
        secondChoice=slots.pop()
        if secondChoice==car:
            success+=1
    ChangeSuccess=success/tries
    print("After {} games 'switch' success approaches {:.2f}%".format(tries, ChangeSuccess))
    print()

    print("Montecarlo Integration")
    tries = 1000000
    area = montecarlo_integrator(f_to_be_integrated,-20,20,tries)
    print("After {} tests area is determined as {}".format(tries,area))
    print()

    print("Option Pricing Using the Black-Scholes Model, discretized version of the BSM model (Euler discretization)")
    # Parameters
    S0 = 100.0 # initial value
    K = 105.0 # strike price
    T = 1.0 # maturity
    r = 0.05 # risk free short rate
    sigma = 0.2 # volatility
    numPoints = 250000
    optionPrice = bsmCallValue(S0, K, T, r, sigma, numPoints)
    numPoints = 250000
    print("Initial value: {} Strike price: {} Maturity: {} Risk free short rate: {} Volatility {} Tests: {}".format(S0, K, T, r, sigma, numPoints))
    print("Benchmark value using the BSM formula and (our) Monte Carlo integrator")
    print("European Option Value: {:.8f}".format(optionPrice))

    # Parameters
    S0 = 100.0 # initial value
    K = 105.0 # strike price
    T = 1.0 # maturity
    r = 0.05 # risk free short rate
    sigma = 0.2 # volatility
    M = 50 # number of time steps
    dt = T / M # length of time interval
    I = 50000 # number of paths / simulations
    S=[] # Paths
    # Simulating  numPaths paths with M time steps
    for i in range(1,I+1):
        path=[]
        for t in range(0,M+1):
            if t == 0:
                path=[S0]
            else:
                z = normalvariate(0,1) #  (mean = 0, stddev = 1)
                St = path[t-1] * math.exp((0.5* sigma * sigma * dt) + (sigma * math.sqrt(dt) * z))
                path.append(St)
        S.append(path)
    # Calculating the Monte Carlo estimator
    sumVal = 0
    for p in S:
        sumVal += rectifier(p[-1] - K)
    C0 = math.exp(-r * T) * sumVal / I
    print("Monte Carlo estimator for the European call option, exploring {} paths of {} steps".format(I,M))
    print("European Option Value: {:.3f}".format(C0))

if __name__ == "__main__":
    main()