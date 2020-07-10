import tkinter as tk
from tkinter import filedialog

class MenuBar:
    def __init__(self, parent):
        font_style = ('ubutnu', 12)
        MenuBar = tk.Menu(parent.master, font=font_style)
        parent.master.config(menu=MenuBar)

        file_dropdown = tk.Menu(MenuBar, font=font_style, tearoff=0)
        file_dropdown.add_command(label="New File", command=parent.new_file)
        file_dropdown.add_command(label='Open File', command=parent.open_file)
        file_dropdown.add_command(label='Save File', command=parent.save)
        file_dropdown.add_command(label='Save As', command=parent.save_as)

        MenuBar.add_cascade(label='File', menu=file_dropdown) 

class textEditor:
    def __init__(self, master):
        master.title('Untitled - BText')
        master.geometry('1200x700')

        font_style = ('ubutnu', 17)

        self.master = master
        self.filename = None

        self.textarea = tk.Text(master, font=font_style)
        self.scroll =  tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.MenuBar = MenuBar(self)

    def set_window_title(self, name=None):
        if name:
            self.master.title(name = " - BText")
        else:
            self.master.title('Untitled - BText')
    def new_file(self):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()
    def open_file(self):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[
                ('Text Files', '*.txt'),
                ('Python Scipts', '*py')
            ]
        )
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, 'r') as f:
                self.textarea.insert(1.0, f.read())
    def save(self):
        if self.filename:
            try:
                text_area_input = self.textarea.get(1.0, tk.END)
                with open(self.filename, 'w') as f:
                    f.write(text_area_input)
            except Exception as e:
                print(e)
        else:
            self.save_as
    def save_as(self):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile='Untitled.txt',
                filetypes = [('Text Files', '*.txt'),
                ('Python Scipts', '*.py')
                ])
            text_area_input = self.textarea.get(1.0, tk.END)
            with open(new_file, 'w') as f:
                f.write(text_area_input)
            self.filename = new_file
            self.set_window_title(self.filename)
        except Exception as e:
            print(e)
def main():
    master = tk.Tk()
    btext = textEditor(master)
    master.mainloop()

main()