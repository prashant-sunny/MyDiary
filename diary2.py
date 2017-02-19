import Tkinter
from Tkinter import*
from ScrolledText import*
from tkFileDialog import askopenfilename
import tkMessageBox
from time import localtime,strftime

root = Tkinter.Tk(className = " Write in Diary")
textPad = ScrolledText(root,width=100,height=80)

#Create the menus & define function for each menu item

def open_command():
    file = open("diary.txt",mode='r')
    contents = file.read()
    showDiary = Tkinter.Tk(className = " Diary")
    textPad1 = ScrolledText(showDiary,width=100,height=80)
    textPad1.insert('1.0',contents)
    file.close()
    textPad1.pack()
    showDiary.mainloop()

def save_command():
    date = strftime("%Y-%m-%d %H:%M:%S",localtime())
    file = open("diary.txt","a")
    t = textPad.get('1.0',END+'-1c')
    file.write("\nDate : "+date+"\n")
    file.write(t)
    file.close()
           
def exit_command():
    if tkMessageBox.askokcancel("Quit","Do yo really want to quit?"):
        root.destroy()

def about_command():
    label = tkMessageBox.showinfo("About","Created By: Prashant Jha\nVersion: 1.0")

    
#Creating All Menu Item
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open",command=open_command)
filemenu.add_command(label="Save",command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit_command)

helpmenu = Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About",command=about_command)

#End of creating All Menu Item

textPad.pack()
root.mainloop()
