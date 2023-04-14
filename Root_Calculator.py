from tkinter import Tk,Label,Button,Entry

windows=Tk()
windows.title("Square root calculator")
windows.minsize(width=500,height=300)
windows.config(padx=20,pady=20)

a_label=Label(text="a=",font=("Arial",24,"bold"))
a_label.grid(column=0,row=0)

a_input=Entry(width=15,font=("Arial",24,"bold"))
a_input.grid(column=1,row=0)

b_label=Label(text="b=",font=("Arial",24,"bold"))
b_label.grid(column=0,row=1)

b_input=Entry(width=15,font=("Arial",24,"bold"))
b_input.grid(column=1,row=1)

c_label=Label(text="c=",font=("Arial",24,"bold"))
c_label.grid(column=0,row=2)

c_input=Entry(width=15,font=("Arial",24,"bold"))
c_input.grid(column=1,row=2)

Root1=Label(text="root1= root1",font=("Arial",24,"underline"))
Root1.grid(column=1,row=3)

Root2=Label(text="root2= root2",font=("Arial",24,"underline"))
Root2.grid(column=1,row=4)
def calculate():
    a=int(a_input.get())
    b=int(b_input.get())
    c=int(c_input.get())
    root1=((-1*b)+((b**2)-4*a*c)**(1/2))/(2*a)
    root2 = ((-1 * b) - ((b ** 2) - 4 * a * c) ** (1 / 2)) / (2 * a)
    Root1.config(text=f"root1= {root1}")
    Root2.config(text=f"root2= {root2}")

    print("clicked")
button=Button(text="Calculate",font=("Arial",18,"italic"),command=calculate)
button.grid(column=1,row=5)
windows.mainloop()