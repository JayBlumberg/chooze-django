from tkinter import *
root = Tk()
v = IntVar()
Label(root,
      text="""Choose a
Toolbox option:""",
      justify = LEFT,
      padx = 20).pack()
def ShowChoice():
    print(v.get())
    x = v.get()
    print(x)
Radiobutton(root,
            text="Amazon",
            indicatoron = 0,
            width = 20,
            padx = 20,
            variable=v,
            command=ShowChoice,
            value=1).pack(anchor=W)


Radiobutton(root,
            text="Zappos",
            indicatoron = 0,
            width = 20,
            padx = 20,
            variable=v,
            command=ShowChoice,
            value=2).pack(anchor=W),



mainloop()

