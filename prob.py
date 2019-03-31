from collections import Counter

def experiment(event, sample_draw, n=10000):
    draws = []
    for _ in range(n):
        draws.append(sample_draw())
    results = list(map(event, draws))
    return results.count(True)/n