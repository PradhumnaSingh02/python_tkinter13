from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('644x456')
root.title('RadioButton')

def order():
    tmsg.showinfo('Order Recieved!'f"We have recieve your order for {var.get()}.Thanks for Order")

Label(root, text='What would u like to Order??..Sir!!', font='lucida 19 bold', justify=LEFT, padx=14).pack()
var = IntVar()

radio = Radiobutton(root, text='Paneer', padx=10, variable=var, value=1).pack(anchor='w')
radio = Radiobutton(root, text='Kashmiri Aloo', padx=10, variable=var, value=2).pack(anchor='w')
radio = Radiobutton(root, text='Dosa', padx=10, variable=var, value=3).pack(anchor='w')
radio = Radiobutton(root, text='Bread', padx=10, variable=var, value=4).pack(anchor='w')
radio = Radiobutton(root, text='Lemon Juice', padx=10, variable=var, value=5).pack(anchor='w')
radio = Radiobutton(root, text='Chokha', padx=10, variable=var, value=6).pack(anchor='w')
radio = Radiobutton(root, text='Jalebi', padx=10, variable=var, value=7).pack(anchor='w')
radio = Radiobutton(root, text='Samosa', padx=10, variable=var, value=8).pack(anchor='w')

Button(root, text='Submit', padx=10, bg='Green', command=order).pack()
root.mainloop()