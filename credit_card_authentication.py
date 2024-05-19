from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root=Tk()
root.title("Credit Card Authentication")
root.geometry("600x400")

root.configure(background="gold")

input_box = Entry()
input_box.place(relx=0.5, rely=0.3, anchor = CENTER)

img=ImageTk.PhotoImage(Image.open ("credit.jpg"))
label = Label(root, image=img)


def authentication():
        input_value = int(input_box.get())
        messagebox.showinfo("Alert","Credit card accepted.")
        get_input = input_box.get()
        try:
            print(text + message)
        except(ValueError):
             messagebox.showinfo("Error", "Credit card not accepted.Please put valid Pin Code.")

btn = Button(root, text = "check credit card", command = authentication)
btn.place(relx=0.5, rely=0.4, anchor = CENTER)
label.place(relx=0.5, rely=0.7, anchor = CENTER)

root.mainloop()