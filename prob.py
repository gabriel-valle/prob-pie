from collections import Counter

def fact(n):
    for i in range(1,n):
        n *= i
    return n

def perm(n, k):
    low = max(n,n-k)
    for i in range(low, n):
        n *= i
    return n

def choose(n,k):
    return perm(n, k)/fact(min(n,n-k))

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

    def estimate(self, event, given=None, n=10000):
        draws = []
        for _ in range(n):
            draws.append(self.sample_draw())
        if callable(given):
            draws = filter(given, draws)
        results = list(map(event, draws))
        return results.count(True)/len(results)