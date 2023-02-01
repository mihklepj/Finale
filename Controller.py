from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)

    def main(self):
        self.view.main()

    def click_names(self):
        self.view.btn_names['state'] = 'disabled'

    def click_tasks(self):
        self.view.btn_names['state'] = 'disabled'
        self.view.btn_tasks['state'] = 'disabled'

    def click_shuffle(self):
        pass

    def click_save(self):
        pass

    def click_clear(self):
        self.view.btn_names['state'] = 'normal'
        self.view.btn_tasks['state'] = 'normal'
