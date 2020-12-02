import tkinter as tk

window = tk.Tk()
window.title("Welcome to tkinter app")
window.geometry('300x100')

count = 0

label1 = tk.Label(window, text=("count: "+str(count)), font=("Courier",30))
label1.grid(column=0, row=0)


def counter_click():
    global count
    count += 1
    label1.configure(text="count: "+str(count))
    if count == 20:
        count = 0


button1 = tk.Button(window, text="counter", command=counter_click)
button1.grid(column=0, row=1)

window.mainloop()
