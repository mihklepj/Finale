import os
import random


class Model:

    def __init__(self):
        self.names = 'TAK22_Names.txt'
        self.tasks = random.choice(os.listdir("databases"))
