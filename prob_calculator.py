import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs) -> None:
        self.set_contents(**kwargs)

    def set_contents(self, **kwargs):
        contents = []

        for key in kwargs:
            for n in range(kwargs[key]):
                contents.append(key)
        self.contents = contents

    def draw(self, quantity):
        contents = self.contents
        draws = []

        if quantity < len(contents):
            for n in range(quantity):
                i = random.randrange(len(contents))
                draws.append(contents[i])
                contents = contents[0:i] + contents[i + 1:]
            self.contents = contents
            return draws
        return contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    bad = 0

    for n in range(num_experiments):
        # seed of the experiment
        exp = copy.deepcopy(hat)
        prova = exp.draw(num_balls_drawn)
        for v in expected_balls.keys():
            count = 0
            for x in range(len(prova)):
                if prova[x] == v:
                    count += 1
            if count < expected_balls[v]:
                bad += 1
                break

    return 1 - bad / num_experiments
