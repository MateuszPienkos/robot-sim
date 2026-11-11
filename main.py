import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import msvcrt

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, cmd):
        if cmd == "w":
            self.y += 1
        elif cmd == "s":
            self.y -= 1
        elif cmd =="a":
            self.x -= 1 
        elif cmd =="d":
            self.x += 1
        elif cmd =="q":
            pass
        else:
             print("Invalid value")       


def main():
    robot1 = Robot(np.random.randint(0,100), np.random.randint(0,100))
    print('Forward "w" Backwars "s" Left "a" Right "d" quit "q"')
    while(True):
         plt.plot(robot1.x, robot1.y, dotsize=200)
         plt.show()
         key = msvcrt.getch().decode('utf-8', errors='ignore')
         robot1.move(key)
         if key == "q":
              break
         print(robot1.x, robot1.y)

if __name__ == "__main__":
    main()