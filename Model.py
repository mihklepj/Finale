import os
import random
from tkinter import INSERT, filedialog


class Model:

    def __init__(self):
        self.name_list = []  # Empty list for names
        self.nimed = []
        self.task_list = []  # Empty list for tasks
        self.result_list = []  # Empty list for result

    def show_names(self):
        self.name_list = []
        name_file = filedialog.askopenfilename()
        with open(name_file, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
            for name in all_lines:

                self.name_list.append(name)

    def show_tasks(self):
        self.task_list = []
        task_file = filedialog.askopenfilename()
        with open(task_file, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
            for task in all_lines:
                self.task_list.append(task)

    def shuffle_tasks(self):
        random.shuffle(self.task_list)


    def show_result(self):
        if len(self.name_list) > 0 and len(self.task_list) > 0:
            self.name_list = map(lambda s: s.strip(), self.name_list)
            #x = 0
            #for name in self.nimed:
                #name.strip()
                #self.result_list.append(name + ' - ' + self.task_list[x])
            kriips = ' - '
            self.result_list = [i + j for i, j in zip(self.name_list, self.task_list)]
                #x += 1

        print(self.nimed)
        print(self.task_list)
        print('Tulemus:')
        print(self.result_list)

    def save_result(self):
        pass

    def clear_fields(self):
        pass

