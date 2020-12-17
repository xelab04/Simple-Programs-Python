
import tkinter as tk

window = tk.Tk()
window.geometry("825x425")
window.configure(bg="#0dff00")

def butt():
    entry_1 = entry.get()
    if entry_1.isdigit() == False:
        print("entry is text")
    else:
        entry_1 = int(entry_1)
        final_res = entry_1 + 5
        print(final_res)

def butt_2():
    print("Hello World!")
    
label = tk.Label(window ,text = "Label text" , height = 2 , width = 10)
entry = tk.Entry(window ,width = 15)
button = tk.Button(window, text = "Finish" , height = 1, width = 25, command=lambda: butt())
button_2 = tk.Button(window, text = "HW" , height = 1, width = 25, command=lambda: butt_2())

label.grid(column = 0 , row = 0, padx = (5,5) , pady = (5,5))
entry.grid(column = 1 , row = 0, padx = (5,5) , pady = (5,5))
button.grid(column = 2,  row = 0, padx = (5,5) , pady = (5,5))
button_2.grid(column = 2, row = 1, padx = (5,5) , pady = (5,5))
window.mainloop()
