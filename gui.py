import tkinter as tk


class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Top Secret")
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.pack(pady=100, padx=100)

        # Create a Tkinter variable
        tkvar = tk.StringVar(root)

        # Dictionary with options
        choices = {'Pizza', 'Lasagne', 'Fries', 'Fish', 'Potatoe'}
        tkvar.set('Pizza')  # set the default option

        popupMenu = tk.OptionMenu(self, tkvar, *choices)
        tk.Label(self, text="Choose a dish").grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

        # on change dropdown value

        def change_dropdown(*args):
            print(tkvar.get())

        # link function to change dropdown
        tkvar.trace('w', change_dropdown)

        #tk.Label(self, text="Biological Sciences").pack()

        temp_titles = ["AAAAAAAAAAAA", "BBBBBBBBBBBBBB", "CCCCCCCCCCCCCC"]
        temp_links = ["google.com", "apple.com", "facebook.com"]

        def displayInfo():
            for msg in temp_titles:
                w = tk.Message(self, text=msg)
            w.pack()

        def toggle():
            '''
            use
            t_btn.config('text')[-1]
            to get the present state of the toggle button
            '''
            if t_btn.config('text')[-1] == 'True':
                t_btn.config(text='False')
                displayInfo()
            else:
                t_btn.config(text='True')

        t_btn = tk.Button(text="True", width=12,
                          command=toggle, highlightbackground='blue')
        t_btn.pack(pady=5)


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
