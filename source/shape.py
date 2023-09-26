from pygame import *
import math

class SuperShape:
    n1 = 1
    n2 = 1
    n3 = 1
    m = 0
    a = 1
    b = 1
    def __init__(self, window:Surface) -> None:
        self.window = window
        self.TWOPIRANGE:list[float] = []
        for i in range(630):self.TWOPIRANGE.append(i/100)

    def getR(self, theta):
        r = 1
        parts = [
            math.pow(abs((1/self.a)*math.cos(theta*self.m/4)), self.n2),
            math.pow(abs((1/self.b)*math.sin(theta*self.m/4)), self.n3),
            None
        ]
        parts[2] = self.n1 * math.sqrt(parts[0]+parts[1])

        if parts[2] == 0:return 0

        return 1 / parts[2]

    def draw(self):
        center = [
            self.window.get_width()/2,
            self.window.get_height()/2
        ]
        old = None
        for angle in self.TWOPIRANGE:
            r = self.getR(angle)
            x = center[0]+100*r*math.cos(angle)
            y = center[1]-100*r*math.sin(angle)

            pos = [x,y]
            if old != None:
                draw.line(
                    self.window,
                    (255,255,255),
                    old, pos
                )
            old = pos

        self.m += 0.001