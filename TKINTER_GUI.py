import math
import tkinter as tk
window=tk.Tk()

def command(x):
    var = x.get()
    print(var)

a = tk.Label(window,text="Cement")
ab = tk.Entry(window)

b = tk.Label(window,text="Gravel")
bb = tk.Entry(window)

c = tk.Label(window,text="Sand")
cb = tk.Entry(window)

alist = [a,ab,b,bb,c,cb]
entry_list = [ab,bb,cb]

for thing in alist:
    thing.pack()
    
button=tk.Button(window, height=1, width=10, text="Go!",command=lambda: command(ab))
#ab is an entry spot
#look at function "command" above

button.pack()
#button.grid(row = 5,column = 2)

window.mainloop()
