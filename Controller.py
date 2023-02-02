import tkinter as tk
from tkinter import *
from tkinter import filedialog
import configfile as configfile
from Model import Model
from View import View

self = tk.Tk()
self.withdraw()


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)

    def main(self):
        self.view.main()


    def click_names(self):
        file_path = filedialog.askopenfilename()
        with open(file_path, 'r', encoding='utf8') as f:
            self.view.box_names.insert(INSERT, f.read())

    def click_tasks(self):
        file_path = filedialog.askopenfilename()
        with open(file_path, 'r', encoding='utf8') as f:
            self.view.box_tasks.insert(INSERT, f.read())

    def click_shuffle(self):
        pass

    def click_save(self):
        pass

    def click_clear(self):
        self.view.box_names.delete("1.0", self.END)
        self.view.box_tasks.delete("1.0", self.END)
        self.view.btn_names['state'] = 'normal'
        self.view.btn_tasks['state'] = 'normal'
