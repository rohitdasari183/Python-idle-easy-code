from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess
import os
root=Tk()
root.title("Python IDLE")
root.geometry("1280x720+150+80")
root.configure(bg="lightgreen")
file_path=" "

def set_file_path(path):
    global file_path
    file_path=path
    
def open_file():
    path=askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path,'r') as file:
        code=file.read()
        code_input.delete('1.0',END)
        code_input.insert('1.0',code)
def save():
    if file_path==" ":
        path=asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path=file_path
    with open(path,"w") as file:
        code=code_input.get('1.0',END)
        file.write(code)
        set_file_path(path)
def run():
    if file_path==" ":
        messagebox.showerror("Python IDLE","Save your Code")
        return
    command=f'{file_path}'
    process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output , error=process.communicate()
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)
def cut():
    code_input.event_generate(("<<Cut>>"))
def copy():
    code_input.event_generate(("<<Copy>>"))
def paste():
    code_input.event_generate(("<<Paste>>"))

MenuBar=Menu(root)
editmenu=Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
root.config(menu=MenuBar)

code_input=Text(root,font="cosolas 18")

code_input.place(x=180,y=0,width=680)

code_output=Text(root,font="cosolas 15",bg="orange",fg="black")
code_output.place(x=860,y=0,width=420,height=720)

openim=PhotoImage(file="open.png")
saveim=PhotoImage(file="save.png")
runim=PhotoImage(file="run.png")

Button(root,image=openim,bg="orange",bd=0,command=open_file).place(x=30,y=30)
Button(root,image=saveim,bg="orange",bd=0,command=save).place(x=30,y=145)
Button(root,image=runim,bg="orange",bd=0,command=run).place(x=30,y=260)

root.mainloop()




