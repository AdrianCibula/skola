import tkinter, random
canvas = tkinter.Canvas(height=300, width=300)
canvas.pack()

def text():
        x=random.randint(1,300)
        y=random.randint(1,300)
        a=entry.get()
        canvas.create_text(x,y,text=a,color=farby)

def nic():
        canvas.delete('all')

farby=choice['blue','red','green','yellow']
a=kinter.Entry()
entry.pack()
button=tkinter.Button(text='reset',command=nic)
button.pack()
