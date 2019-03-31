import numpy as np
import prob

def inEvent(draw):
    count = {"red":0, "green":0, "blue":0}
    for elem in draw:
        count[elem] += 1
    return count["red"] == 3 and count["green"] == 2 and count["blue"] == 2

space = ["red"]*12 + ["green"]*18 + ["blue"]*16
def drawball():
    return np.random.choice(space, size=7)

print(prob.experiment(inEvent, drawball))