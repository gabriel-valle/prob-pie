from collections import Counter

def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

def perm(n, k):
    return fact(n)/fact(n-k)

def choose(n,k):
    return fact(n)/(fact(k)*fact(n-k))

def union(*events):
    return lambda result: any([ev(result) for ev in events])
    
def intersection(*events):
    return lambda result: all([ev(result) for ev in events])
   
def complement(event):
    return lambda result: not event(result)

class Experiment:
    def __init__(self, result_drawer):
        self.sample_draw = result_drawer
        self.events = {}

    def estimate(self, event, n=10000):
        draws = []
        for _ in range(n):
            draws.append(self.sample_draw())
        results = list(map(event, draws))
        return results.count(True)/n