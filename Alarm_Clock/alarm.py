#Making an alarm clock 

# Importing GUI and time
from time import strftime
from tkinter import Label, Tk 


# Configuring Alarm clock window 

window = Tk()
window.title("")
window.geometry("200x200")
window.configure(bg="green")
window.resizable(False,False)


# adding logic to the code
clock_label = Label(window, bg="green", fg="white", font = ("Times", 30), relief="flat")
clock_label.place(x = 20, y = 20)

def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

update_label()
window.mainloop()