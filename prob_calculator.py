import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = list()

        for color, amount in kwargs.items():
            for i in range(0, amount):
                self.contents.append(color)

    def draw(self, draw_amount):
        drawn_balls = list()
        if draw_amount > len(self.contents):
            # shallow copy constructs a new compound object referencing the old object
            drawn_balls = copy.copy(self.contents)
            self.contents.clear()
            return drawn_balls
        else:
            for i in range(0, draw_amount):
                ball = self.contents.pop(random.randint(0, len(self.contents)-1))
                drawn_balls.append(ball)
            return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_actual = 0

    for i in range(0, num_experiments):
        experimental_hat = copy.deepcopy(hat)
        balls = experimental_hat.draw(num_balls_drawn)

        if all([balls.count(key) >= value for key, value in expected_balls.items()]):
            num_actual += 1

    return num_actual / num_experiments
