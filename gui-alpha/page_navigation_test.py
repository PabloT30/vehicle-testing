from tkinter import *
from tkinter import ttk
from typing import Collection
from tkcalendar import Calendar
from PIL import ImageTk,Image

#------------------------------------------------------------ROOT---------------------------------------------------------------------#
root = Tk()
root.title("CDG")
#root.iconbitmap("carro.ico")
#root.geometry("480x640")
root.geometry("240x320")
root.resizable(0,0)

#------------------------------------------------------------FRAMES-------------------------------------------------------------------#
#Operator Registration
OpRegframe=Frame(root)
OpRegframe.place(relwidth="1",relheight="1")
OpRegframe.columnconfigure(index=0, weight=1)
OpRegframe.rowconfigure(index=0, weight=1)
OpRegframe.rowconfigure(index=1, weight=5)
OpRegframe.rowconfigure(index=2, weight=1)
#Vehicle Data
VehiDataframe=Frame()
VehiDataframe.place(relwidth="1",relheight="1")
VehiDataframe.columnconfigure(index=0, weight=1)
VehiDataframe.rowconfigure(index=0, weight=1)
VehiDataframe.rowconfigure(index=1, weight=5)
VehiDataframe.rowconfigure(index=2, weight=1)
#Center of gravity calculation
Calcframe=Frame()
Calcframe.place(relwidth="1",relheight="1")
Calcframe.columnconfigure(index=0, weight=1)
Calcframe.rowconfigure(index=0, weight=1)
Calcframe.rowconfigure(index=1, weight=5)
Calcframe.rowconfigure(index=2, weight=1)

#--------------------------------------------------------------FUNCTIONS--------------------------------------------------------------#
#Operator Registration
def OpRegNext():
    VehiDataframe.lift()    
#Vehicle Data
def VehiDataNext():
    Calcframe.lift()   
def VehiDataBack():
    OpRegframe.lift()
#Center of gravity calculation
def CalcBack():
    VehiDataframe.lift()
def FinishCalc():
    root.destroy()
 
#----------------------------------------------------------------WIDGETS--------------------------------------------------------------#
#Operator Registration
Opregtitle=ttk.Label(OpRegframe,text="Operator registration",font=("",12))
NextOpReg=ttk.Button(OpRegframe,text="NEXT",command= OpRegNext)
Boxlabelframe=ttk.LabelFrame(OpRegframe)
Boxlabelframe.columnconfigure(index=0,weight=1)
Operatorslist=["David","Carlos","Sebastian"]
a = StringVar()
b = StringVar()
a.set("Operator 1")
b.set("Operator 2")
Operator1optionmenu=OptionMenu(Boxlabelframe,a,*Operatorslist)
Operator2optionmenu=OptionMenu(Boxlabelframe,b,*Operatorslist)
#Vehicle Data
VehiDatatitle=ttk.Label(VehiDataframe,text="Vehicle data",font=("",12))
Entrylabelframe=ttk.Labelframe(VehiDataframe)
Entrylabelframe.columnconfigure(index=0,weight=1)
Entrylabelframe.columnconfigure(index=1,weight=1)
Entrylabelframe.rowconfigure(index=0,weight=1)
Entrylabelframe.rowconfigure(index=1,weight=1)
Entrylabelframe.rowconfigure(index=2,weight=1)
Calendarpng=PhotoImage(file="calendar.png")
Datelabel=ttk.Label(Entrylabelframe, text="Pick a date")
Datebutton=Button(Entrylabelframe,image=Calendarpng)
Datebutton["border"] = "0"
Seriallabel=ttk.Label(Entrylabelframe,text="Serial number")
Serialentry=ttk.Entry(Entrylabelframe)
Filelabel=ttk.Label(Entrylabelframe, text="Picture")
Filebutton=ttk.Button(Entrylabelframe, text="Upload")
Buttonlabelframe=ttk.LabelFrame(VehiDataframe)
Buttonlabelframe.columnconfigure(index=0,weight=1)
Buttonlabelframe.columnconfigure(index=1,weight=1)
Buttonlabelframe.rowconfigure(index=0,weight=1)
BackVehiData=ttk.Button(Buttonlabelframe,text="BACK",command=VehiDataBack)
NextVehiData=ttk.Button(Buttonlabelframe,text="NEXT",command=VehiDataNext)
#Center of gravity calculation
Calctitle=ttk.Label(Calcframe,text="Center of gravity calculation",font=("",12))
Button2labelframe=ttk.Labelframe(Calcframe)
Button2labelframe.columnconfigure(index=0, weight=1)
Button2labelframe.columnconfigure(index=1, weight=1)
Button2labelframe.rowconfigure(index=0,weight=1)
BackCalc=ttk.Button(Button2labelframe,text="BACK", command=CalcBack)
FinishCalc=ttk.Button(Button2labelframe,text="FINISH", command=FinishCalc)
#-------------------------------------------------------------------GRID---------------------------------------------------------------#
#Operator Registration
Opregtitle.grid(row=0)
NextOpReg.grid(row=2)
Boxlabelframe.grid(row=1,sticky="nsew")
Operator1optionmenu.grid(row=0,padx=5, pady=10,sticky="ew")
Operator2optionmenu.grid(row=1,padx=5, pady=10,sticky="ew")
#Vehicle Data
VehiDatatitle.grid(row=0)
Entrylabelframe.grid(row=1,sticky="nsew")
Datelabel.grid(row=0,column=0)
Datebutton.grid(row=0,column=1)
Seriallabel.grid(row=1,column=0)
Serialentry.grid(row=1,column=1)
Filelabel.grid(row=2, column=0)
Filebutton.grid(row=2, column=1)
Buttonlabelframe.grid(row=2,sticky="nsew")
BackVehiData.grid(column=0,row=0)
NextVehiData.grid(column=1,row=0)
#Center of gravity calculation
Calctitle.grid(row=0)
Button2labelframe.grid(row=2,sticky="nsew")
BackCalc.grid(column=0, row=0)
FinishCalc.grid(column=1,row=0)

#-------------------------------------------------------------------END---------------------------------------------------------------#

OpRegframe.lift()

root.mainloop()

