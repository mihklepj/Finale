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

        self.geometry('515x200')
        self.title('Ülesannete määraja')
        self.center(self)

        # Create frames
        self.frame_top, self.frame_center, self.frame_names, self.frame_tasks, self.frame_bottom = self.create_frames()

        # Create buttons
        self.btn_names, self.btn_tasks, self.btn_shuffle, self.btn_save, self.btn_clear = self.create_all_buttons()

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
        frame_names = Frame(self, bg='green').grid(column=0, row=0)
        frame_tasks = Frame(self, bg='yellow').grid(column=1, row=0)
        frame_bottom = Frame(self, bg='white')

        frame_top.pack(fill=BOTH)
        frame_center.pack(expand=True, fill=BOTH)
        frame_names.pack(expand=True, fill=BOTH)
        frame_tasks.pack(expand=True, fill=BOTH)
        frame_bottom.pack(expand=True, fill=BOTH)

        return frame_top, frame_center, frame_names, frame_tasks, frame_bottom

    def create_all_buttons(self):
        btn_names = Button(self.frame_top, text='Nimed', font=self.default_style, command=self.controller.click_names)
        btn_tasks = Button(self.frame_top, text='Ülesanded', font=self.default_style,
                           command=self.controller.click_tasks)
        btn_shuffle = Button(self.frame_top, text='Sega', font=self.default_style,
                             command=self.controller.click_shuffle)
        btn_save = Button(self.frame_top, text='Salvesta', font=self.default_style, command=self.controller.click_save)
        btn_clear = Button(self.frame_top, text='Tühjenda', font=self.default_style,
                           command=self.controller.click_clear)

        # Three buttons on frame
        btn_names.grid(row=0, column=0, padx=5, pady=2, sticky=EW)
        btn_tasks.grid(row=0, column=1, padx=5, pady=2, sticky=EW)
        btn_shuffle.grid(row=0, column=2, padx=5, pady=2, sticky=EW)
        btn_save.grid(row=0, column=3, padx=5, pady=2, sticky=EW)
        btn_clear.grid(row=0, column=4, padx=5, pady=2, sticky=EW)

        return btn_names, btn_tasks, btn_shuffle, btn_save, btn_clear
