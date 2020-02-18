from tkinter import *

root = Tk()
root.title("Convertor")
Title = Label(root,text = "multiConnverter\n Cm to m")
Title.pack()
e = Entry(root)
e.pack()

def myClick():
    w = chose.curselection()

    if w[0] == 0:
        Option = e.get()
        cmtom = float(Option)
        e.delete(0, END)
        e.insert(0, cmtom / 100)

    elif w[0] == 1:
        Option1= e.get()
        mtocm = float(Option1)
        e.delete(0,END)
        e.insert(0, mtocm * 100)
    elif w[0] == 2:
        Option2 = e.get()
        inchtom = float(Option2)
        e.delete(0,END)
        e.insert(0, inchtom / 39.37)
    elif w[0] == 3:
        Option3 = e.get()
        mtoinch = float(Option3)
        e.delete(0,END)
        e.insert(0, mtoinch *39.37)

chose = Listbox(root)
chose.insert(0,"1.cm to m")
chose.insert(1,"2.m to cm")
chose.insert(2,"3.inch to m")
chose.insert(3,"4.m to inch")
chose.insert(4,"5.km to m")
chose.insert(5,"6.m to km")
#chose.insert(6,"7.mile to km")
#chose.insert(7,"8.km to mile")
#chose.insert(8,"9.kg to g")
#chose.insert(9,"10.g to kg")
#chose.insert(10,"11.")
#chose.insert(11,"12.")
#chose.insert(12,"13.")
chose.pack()
myboutto = Button(root,text = "Convert",command  = myClick)
#wider
myboutto.pack()

root.mainloop()
