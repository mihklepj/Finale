import tkinter as tk
from tkinter import *
from tkinter import filedialog
#import configfile as configfile
from Model import Model
from View import View

#self.withdraw()


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)
        print(self.model.task_list)

    def main(self):
        self.view.main()


    def click_names(self):
        self.view.box_names.delete(1.0, END)
        self.model.show_names()
        for name in self.model.name_list:
            self.view.box_names.insert(INSERT, name)

    def click_tasks(self):
        self.view.box_tasks.delete(1.0, END)
        self.model.show_tasks()
        for task in self.model.task_list:
            self.view.box_tasks.insert(INSERT, task)
        for result in self.model.result_list:
            self.view.box_result.insert(INSERT, result)

    def click_shuffle(self):
        self.view.box_tasks.delete("1.0","end")
        self.model.shuffle_tasks()
        for task in self.model.task_list:
            self.view.box_tasks.insert(INSERT, task)
        for result in self.model.result_list:
            self.view.box_result.insert(INSERT, result)


    def click_save(self):
        self.model.save_result()

    def click_clear(self):
        self.model.clear_fields()

