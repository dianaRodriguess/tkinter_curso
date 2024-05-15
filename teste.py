from tkinter import *

root = Tk()

def butao():
    # mylabel1 = Label(root, text="Hello world!")
    # mylabel2 = Label(root, text="Daenarys Targaryan, a primeira de seu nome.")
    # mylabel1.pack()
    # mylabel2.pack()
    msg = "ola " + e.get()
    mylabel1 = Label(root, text=msg)
    mylabel1.pack()

# .grid todo elemento é relativo um ao outro
# mylabel2.grid(row=1, column=5), aparentaria o mesmo pq não há nada nas colunas 1, 2, 3, 4
# mylabel1.grid(row=0, column=0)
# mylabel2.grid(row=1, column=0)

e = Entry(root, width=50)
e.pack()
e.insert(0, "Enter your name:")
mybutton = Button(root, text="butão", pady=30, padx=10, command=butao, fg="red", bg="#e44abc")
mybutton.pack()

root.mainloop()