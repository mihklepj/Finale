from tkinter import *
import tkinter.font as tkfont


class View(Tk):

    def __init__(self, controller, model):
        super().__init__()
        self.controller = controller
        self.model = model

        # Fonts
        self.big_font_style = tkfont.Font(family='Courier', size=18, weight='bold')
        self.default_style_bold = tkfont.Font(family='Verdana', size=10, weight='bold')
        self.default_style = tkfont.Font(family='Verdana', size=10)

        # GUI window
        self.geometry('1000x500')
        self.title('Ülesannete määraja')
        self.center(self)

        # Create frames
        self.frame_top, self.frame_center, self.frame_bottom = self.create_frames()

        # Create buttons
        self.btn_names, self.btn_tasks, self.btn_shuffle, self.btn_save, self.btn_close = self.create_all_buttons()

        # Create textboxes
        self.box_names, self.box_tasks, self.box_result = self.create_textboxes()

    def main(self):
        self.mainloop()

    @staticmethod
    def center(win):
        """
        https://stackoverflow.com/questions/3352918/how-to-center-a-window-on-the-screen-in-tkinter
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def create_frames(self):
        frame_top = Frame(self, bg='blue', height=50)
        frame_center = Frame(self, bg='black')
        frame_bottom = Frame(self, bg='white')

        frame_top.pack(fill=BOTH)
        frame_center.pack(expand=True, fill=BOTH)
        frame_bottom.pack(expand=True, fill=BOTH)

        return frame_top, frame_center, frame_bottom

    def create_textboxes(self):
        box_names = Text(self.frame_center, bg='white', height=100, width=20, font=self.default_style)
        box_tasks = Text(self.frame_center, bg='white', height=100, width=40, font=self.default_style)
        box_result = Text(self.frame_center, bg='white', height=100, width=60, font=self.default_style)

        box_names.pack(side=LEFT, padx=5, pady=5)
        box_tasks.pack(side=LEFT, padx=5, pady=5)
        box_result.pack(side=LEFT, padx=5, pady=5)

        return box_names, box_tasks, box_result

    def create_all_buttons(self):
        btn_names = Button(self.frame_top, text='Nimed...', font=self.default_style_bold,
                           command=self.controller.click_names, width=18)
        btn_tasks = Button(self.frame_top, text='Ülesanded...', font=self.default_style_bold,
                           command=self.controller.click_tasks, width=35)
        btn_shuffle = Button(self.frame_top, text='Sega', font=self.default_style_bold,
                             command=self.controller.click_shuffle, state='disabled')
        btn_save = Button(self.frame_top, text='Salvesta...', font=self.default_style_bold,
                          command=self.controller.click_save, state='disabled')
        btn_close = Button(self.frame_top, text='Sulge', font=self.default_style_bold,
                           command=self.destroy)

        # Buttons on top frame
        btn_names.grid(row=0, column=0, padx=2, pady=5, sticky=EW)
        btn_tasks.grid(row=0, column=1, padx=2, pady=5, sticky=EW)
        btn_shuffle.grid(row=0, column=2, padx=15, pady=5, sticky=EW)
        btn_save.grid(row=0, column=3, padx=15, pady=5, sticky=EW)
        btn_close.grid(row=0, column=4, padx=30, pady=5, sticky=EW)

        return btn_names, btn_tasks, btn_shuffle, btn_save, btn_close
