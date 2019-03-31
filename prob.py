from collections import Counter

def experiment(event, sample_draw, n=10000):

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