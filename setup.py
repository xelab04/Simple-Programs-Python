import tkinter as tk
import subprocess
import os

window = tk.Tk()
window.geometry("800x400")
window.configure(bg="#ff8800")
directory = "C:/Program Files (x86)/Steam Market Tracker"
accepted_pressed=False
parent_path = ((os.path.dirname(os.path.realpath(__file__))).replace("\\","/"))

def dirs(new_window):
    dir_folder = True
    new_window.destroy()

def close(xnew_window):
    xnew_window.destroy()

def directory_n_exist():
    new_window = tk.Toplevel(window)
    text = tk.Label(new_window,text="Attention, directory does not exist. If you proceed, directory will be created")
    text.pack()
    dir_button = tk.Button(new_window,text="Proceed",height=2,width=20,command=lambda: dirs(new_window))
    dir_button.pack()
    new_window.mainloop()

def view_license():
    try:
        license_dir = parent_path + "/license.txt"
        subprocess.Popen(["notepad.exe",license_dir])
    except:
        pass
    
def accept(accepted_pressed):
    accepted_pressed = True

def install(accepted_pressed):
    directory=str(textBox.get())
    directory = os.path.join(directory)
    if os.path.exists(directory):
        dir_folder = True
    else:
        dir_folder = False
        #DRAW ERROR BOX
        directory_n_exist()
        #END DRAW ERROR BOX
    #print(accepted_pressed)
    if accepted_pressed == True:
        folder = open(directory,"w+")
        csv_file = open(directory + "/ITEMS.csv" ,"w+")
        txt_file = open(parent_path + "/text.txt" ,"w+")
        
    else:
        #DRAW ERROR FOR ACCEPT
        xnew_window = tk.Toplevel(window)
        n_accept_lbl = tk.Label(xnew_window,text = "You did not accept T&C")
        n_accept_lbl.pack()
        n_accept_btn = tk.Button(xnew_window,text="Oops",command=lambda: xnew_window.destroy())
        n_accept_btn.pack()
        xnew_window.mainloop()
        #END DRAW ERROR FOR ACCEPT
        
def helps():
    print("HELP")
    help_dir = parent_path + "/help.txt"
    help_dir = help_dir.replace("/","\\")
    subprocess.Popen(["notepad.exe",help_dir])

#START DRAW

lbl = tk.Label(window,height=1,width=15,text="Directory (/)")
lbl.grid(column=0,row=200,pady=(290,5))

textBox=tk.Entry(window,width=40)
textBox.grid(column=20,row=200,pady=(290,5))


def view_license_draw():
    view_license_button = tk.Button(window,height=2,width=15,text="View License",command=view_license())
    view_license_button.grid(column=0,row=220)

def accept_draw():
    accept_button = tk.Checkbutton(window,height=2,width=30,text="Accept License Terms and Conditions",command = accept(accepted_pressed))
    accept_button.grid(column=20,row=220)

def install_draw():
    install_button= tk.Button(window, height=2, width=15, text="Install",command= lambda: install(accepted_pressed))
    install_button.grid(column=60,row=220)

def help_draw():
    help_button=tk.Button(window, height=2, width=15, text="Help",command=helps())
    help_button.grid(column=80,row=220)

#END DRAW

view_license_draw()
install_draw()
accept_draw()
help_draw()

window.mainloop()
