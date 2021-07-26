from tkinter import *

#root

root=Tk()

root.title("CDG")

#root.geometry("800x600")

root.resizable(0,0)

#labels

label1=Label(root, text="lift height")
label1.grid(row=0,column=0,sticky="e",padx=10)

label2=Label(root, text="left wheelbase")
label2.grid(row=1,column=0,sticky="e",padx=10)

label3=Label(root, text="right wheelbase")
label3.grid(row=2,column=0,sticky="e",padx=10)

label3=Label(root, text="vehicle rear track")
label3.grid(row=3,column=0,sticky="e",padx=10)

label4=Label(root, text="vehicle front track")
label4.grid(row=4,column=0,sticky="e",padx=10)

label5=Label(root, text="lifted vehicle wheel diameter")
label5.grid(row=5,column=0,sticky="e",padx=10)

label6=Label(root, text="lifted vehicle flattened wheel")
label6.grid(row=6,column=0,sticky="e",padx=10)

label6=Label(root, text="rear left wheel mass")
label6.grid(row=7,column=0,sticky="e",padx=10)

label7=Label(root, text="front left wheel mass")
label7.grid(row=8,column=0,sticky="e",padx=10)

label8=Label(root, text="front left wheel mass")
label8.grid(row=9,column=0,sticky="e",padx=10)

label9=Label(root, text="front right wheel mass")
label9.grid(row=10,column=0,sticky="e",padx=10)

label10=Label(root, text="lifted rear left wheel mass")
label10.grid(row=11,column=0,sticky="e",padx=10)

label11=Label(root, text="lifted rear right wheel mass")
label11.grid(row=12,column=0,sticky="e",padx=10)

cmlabel1=Label(root, text="cm")
cmlabel1.grid(row=0,column=3,sticky="w",padx=10)

cmlabel2=Label(root, text="cm")
cmlabel2.grid(row=1,column=3,sticky="w",padx=10)

cmlabel3=Label(root, text="cm")
cmlabel3.grid(row=2,column=3,sticky="w",padx=10)

cmlabel4=Label(root, text="cm")
cmlabel4.grid(row=3,column=3,sticky="w",padx=10)

cmlabel5=Label(root, text="cm")
cmlabel5.grid(row=4,column=3,sticky="w",padx=10)

cmlabel6=Label(root, text="cm")
cmlabel6.grid(row=5,column=3,sticky="w",padx=10)

cmlabel7=Label(root, text="cm")
cmlabel7.grid(row=6,column=3,sticky="w",padx=10)

kglabel1=Label(root, text="kg")
kglabel1.grid(row=7,column=3,sticky="w",padx=10)

kglabel2=Label(root, text="kg")
kglabel2.grid(row=8,column=3,sticky="w",padx=10)

kglabel2=Label(root, text="kg")
kglabel2.grid(row=9,column=3,sticky="w",padx=10)

kglabel3=Label(root, text="kg")
kglabel3.grid(row=10,column=3,sticky="w",padx=10)

kglabel4=Label(root, text="kg")
kglabel4.grid(row=11,column=3,sticky="w",padx=10)

kglabel5=Label(root, text="kg")
kglabel5.grid(row=12,column=3,sticky="w",padx=10)

label12=Label(root, text="Center of Gravity:")
label12.grid(row=16,column=0, columnspan=2)

label13=Label(root, text="X=")
label13.grid(row=17,column=0)
label13.config(fg="red")

label14=Label(root, text="Y=")
label14.grid(row=18,column=0)
label14.config(fg="green")

label15=Label(root, text="Z=")
label15.grid(row=19,column=0)
label15.config(fg="blue")

#labelspace0=Label(root)
#labelspace0.grid(row=0,column=0)

labelspace1=Label(root)
labelspace1.grid(row=13,column=0)

labelspace2=Label(root)
labelspace2.grid(row=15,column=0)

#entries

entry1=Entry(root)
entry1.grid(row=0,column=1)

entry2=Entry(root)
entry2.grid(row=1,column=1)

entry3=Entry(root)
entry3.grid(row=2,column=1)

entry4=Entry(root)
entry4.grid(row=3,column=1)

entry5=Entry(root)
entry5.grid(row=4,column=1)

entry6=Entry(root)
entry6.grid(row=5,column=1)

entry7=Entry(root)
entry7.grid(row=6,column=1)

entry8=Entry(root)
entry8.grid(row=7,column=1)

entry9=Entry(root)
entry9.grid(row=8,column=1)

entry10=Entry(root)
entry10.grid(row=9,column=1)

entry11=Entry(root)
entry11.grid(row=10,column=1)

entry12=Entry(root)
entry12.grid(row=11,column=1)

entry13=Entry(root)
entry13.grid(row=12,column=1)

#buttons

button1=Button(root, text="calculate")
button1.grid(row=14,column=0)

button2=Button(root, text="clear")
button2.grid(row=14,column=1)

root.mainloop()
