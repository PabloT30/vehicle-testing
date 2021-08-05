import math
from tkinter import *
from tkinter import Label, ttk
from tkinter import font
from PIL import ImageTk,Image
from tkinter import filedialog


root=Tk()
root.title("Centro de Gravedad")
root.geometry("1000x600")
#root.iconbitmap(file="carro.ico")

#Panel para las pestañas
nb = ttk.Notebook(root)
nb.pack(fill="both", expand="yes")

#Pestañas
p1 = ttk.Frame(nb)
p1.columnconfigure(index=0,weight=1)
p1.rowconfigure(index=0,weight=1)
p1.rowconfigure(index=1,weight=1)
p1.rowconfigure(index=2,weight=1)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)

nb.add(p1, text = "Registro de Operarios")
nb.add(p2, text = "Datos del Vehiculo")
nb.add(p3, text = "Calculo del Centro de Gravedad")

#Pestaña 1


#Funciones de la pestaña 1

def ingresar_operario_uno(registrar):
    print("El operario uno es: ", registrar)

def ingresar_operario_dos(registrar):
    print("La operario dos es: ", registrar)

def seleccionar_operario_uno(selection):
    for i in range(RegOpoptionmenu2["menu"].index("end")+1):
        RegOpoptionmenu2["menu"].entryconfig(i,state="normal")
    RegOpoptionmenu2["menu"].entryconfig(selection,state="disabled")

def seleccionar_operario_dos(selection):
    for i in range(RegOpoptionmenu1["menu"].index("end")+1):
        RegOpoptionmenu1["menu"].entryconfig(i,state="normal")
    RegOpoptionmenu1["menu"].entryconfig(selection,state="disabled")


RegOptitulo =ttk.Label(p1, text="Registro de los Operarios", font=40)
RegOptitulo.grid(column=0, row=0)
#RegOptitulo.place(relx=0.5, rely=0, relwidth=0.75, relheight=0.4, anchor="n" )

Optionmenuframe=ttk.LabelFrame(p1,text="")
Optionmenuframe.columnconfigure(index=0,weight=1)
Optionmenuframe.rowconfigure(index=0)
Optionmenuframe.rowconfigure(index=1)
Optionmenuframe.grid(column=0,row=1,sticky="nsew")



Operarioslista=["David Ramírez","Sebastián Pérez","Fernando Casanova","Jorge Lopera","Cristian Muñoz","Pablo Torres","Jhon Pazos"]
a=StringVar()
b=StringVar()
a.set("Operario 1")
b.set("Operario 2")
RegOpoptionmenu1=OptionMenu(Optionmenuframe, a,*Operarioslista,command=seleccionar_operario_uno)
RegOpoptionmenu1.grid(row=0,padx=5, pady=10)
RegOpoptionmenu1.config(font=20)
RegOpoptionmenu2=OptionMenu(Optionmenuframe, b,*Operarioslista,command=seleccionar_operario_dos)
RegOpoptionmenu2.grid(row=1,padx=5, pady=10)
RegOpoptionmenu2.config(font=20)

#label2 = Label(p1, text="Operario 1", font=40)
#label2.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.1, anchor="n")

#label3 = Label(p1, text="Operario 2", font=40)
#label3.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1, anchor="n")

#operario_uno = Entry(p1, font=40)
#operario_uno.place(relx=0.5, rely=0.3, relwidth=0.4, relheight=0.1)

#operario_dos = Entry(p1, font=40)
#operario_dos.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.1)

registro = Button(p1, text="Registrar", command=lambda: [ingresar_operario_uno(operario_uno.get()),ingresar_operario_dos(operario_dos.get())])
registro.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)

#Pestaña 2

#Funciones de la pestaña 2
def imagen_carro():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="C:/", title="Upload the car image")
    my_label = Label(p2, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_label_image = Label(image=my_image).pack()

def ingresar_matricula(registro):
    return print("La matricula del vehículo es: ", registro)

def ingresar_fecha(registro):
    return print("La fecha del ensayo es: ", registro)


#Seleccionar la foto del vehiculo
texto_carro = Label(p2, text="Ingrese la foto del Vehículo",font="20",)
texto_carro.place(relx=0.1, rely=0.6, relwidth=0.5, relheight=0.1)

btn_imagen_carro = Button(p2, text="Open File", command=imagen_carro)
btn_imagen_carro.place(relx=0.65, rely=0.6, relwidth=0.3, relheight=0.1)

#Ingresar la matricula del vehiculo
texto_matricula = Label(p2,text="Ingrese la matricula del vehículo", font=40)
texto_matricula.place(relx=0.1, rely=0.4, relwidth=0.5, relheight=0.1)

ent_matricula = Entry(p2, font=40 )
ent_matricula.place(relx=0.65, rely=0.4, relwidth=0.3, relheight=0.1)

#Ingresar la fecha del ensayo.
texto_fecha = Label(p2,text="Ingrese la fecha", font=40)
texto_fecha.place(relx=0.1, rely=0.2, relwidth=0.5, relheight=0.1)

ent_fecha = Entry(p2, font=40 )
ent_fecha.place(relx=0.65, rely=0.2, relwidth=0.3, relheight=0.1)

#Boton para aceptar

registrar = Button(p2, text="Registrar", command=lambda: [ingresar_matricula(ent_matricula.get()),ingresar_fecha(ent_fecha.get())])
registrar.place(relx=0.4, rely=0.8, relwidth=0.3, relheight=0.1)

#Pestaña 3

def get_lift_height(calcular_centro_de_gravedad):
    """Get lift height from user input in mm"""
    return print("Please enter the lift height in mm: ",calcular_centro_de_gravedad)

def get_left_wheelbase(calcular_centro_de_gravedad):
    """Get left wheelbase from user input in mm."""
    return print("Please enter the left wheelbase in mm: ",calcular_centro_de_gravedad)

def get_right_wheelbase(calcular_centro_de_gravedad):
    """Get right wheelbase from user input in mm."""
    return print("Please enter the right wheelbase in mm: ",calcular_centro_de_gravedad)

def get_mean_wheelbase(left_wheelbase, right_wheelbase):
    """Return mean wheelbase from vehicle's left and right wheelbases in mm.
    Arguments:
    left_wheelbase -- vehicle's left wheelbase in mm.
    right_wheelbase -- vehicle's right wheelbase in mm.
    Return values:
    The mean vehicle wheelbase.
    """
    return (left_wheelbase + right_wheelbase) / 2

def get_rear_track(calcular_centro_de_gravedad):
    """Return vehicle rear track from user input in mm."""
    return print("Please enter vehicle rear track in mm: ", calcular_centro_de_gravedad)

def get_front_track(calcular_centro_de_gravedad):
    """Return vehicle front track from user input in mm."""
    return print("Please enter vehicle front track in mm: ", calcular_centro_de_gravedad)

def get_wheel_diameter(calcular_centro_de_gravedad):
    """Get lifted vehicle wheel diameter from user input in mm."""
    return print("Please enter lifted vehicle wheel diameter in mm: ", calcular_centro_de_gravedad)

def get_flattened_wheel_diameter(calcular_centro_de_gravedad):
    """Get lifted vehicle flattened wheel diameter from user input in mm."""
    return print("Please enter lifted vehicle flattened wheel diameter in mm: ", calcular_centro_de_gravedad)

def get_static_wheel_radius(wheel_diameter, flattened_wheel_diameter):
    """Return static wheel radius.
    Arguments:
    wheel_diameter -- lifted vehicle wheel_diameter in mm
    flattened_wheel_diameter -- lifted vehicle flattened_wheel_diameter in mm
    Return values:
    The static wheel radius in mm.
    """
    return flattened_wheel_diameter - (wheel_diameter / 2)

def get_rear_left_wheel_mass(calcular_centro_de_gravedad):
    """Get rear left wheel mass from user input in kg."""
    return print("Please enter the rear left wheel mass in kg: ", calcular_centro_de_gravedad)

def get_rear_right_wheel_mass(calcular_centro_de_gravedad):
    """Get rear right wheel mass from user input in kg."""
    return print("Please enter the rear right wheel mass in kg: ", calcular_centro_de_gravedad)

def get_front_left_wheel_mass(calcular_centro_de_gravedad):
    """Get front left wheel mass from user input in kg."""
    return print("Please enter the front left wheel mass in kg: ", calcular_centro_de_gravedad)

def get_front_right_wheel_mass(calcular_centro_de_gravedad):
    """Get front right wheel mass from user input in kg."""
    return print("Please enter the front right wheel mass in kg: ", calcular_centro_de_gravedad)

def get_rear_axle_mass(rear_left, rear_right):
    """Return rear axle mass from wheel masses in kg.
    Arguments:
    rear_left -- rear left wheel mass in kg.
    rear_right -- rear right wheel mass in kg.
    """
    return rear_left + rear_right

def get_front_axle_mass(front_left, front_right):
    """Return front axle mass form wheel masses in kg.
    Arguments:
    front_left -- front left wheel mass in kg.
    front_right -- front right wheel mass in kg.
    Return values:
    The frontal axle mass in kg.
    """
    return front_left + front_right

def get_vehicle_mass(rear_axle_mass, front_axle_mass):
    """Return vehicle mass from wheel masses in kg.
    Arguments:
    rear_axle_mass -- vehicle rear axle mass in kg.
    front_axle_mass -- vehicle front axle mass in kg.
    Return values:
    The total vehicle mass in kg.
    """
    return rear_axle_mass + front_axle_mass

def get_lifted_angle(lift_height, mean_wheelbase):
    """Return lifted angle from vehicle lift height and mean wheelbase.
    Arguments:
    lift_height -- lift height in mm.
    mean_wheelbase -- mean wheelbase in mm.
    Return values:
    The lifted angle in radians.
    """
    return math.atan(lift_height / mean_wheelbase)

def get_lifted_rear_left_wheel_mass(calcular_centro_de_gravedad):
    """Get lifted rear left wheel mass from user input in kg."""
    return print("Please enter the lifted rear left wheel mass in kg: ", calcular_centro_de_gravedad)

def get_lifted_rear_right_wheel_mass(calcular_centro_de_gravedad):
    """Get lifted rear right wheel mass from user input in kg."""
    return print("Please enter the lifted rear right wheel mass in kg: ", calcular_centro_de_gravedad)

def get_lifted_rear_axle_mass(lifted_rear_left_wheel_mass, lifted_rear_right_wheel_mass):
    """Return rear axle mass from wheel masses in kg.
    Arguments:
    rear_left -- rear left wheel mass in kg.
    rear_right -- rear right wheel mass in kg.
    """
    return lifted_rear_left_wheel_mass + lifted_rear_right_wheel_mass

def get_longitudinal_distance(vehicle_mass, rear_axle_mass, mean_wheelbase):
    """Return longitudinal distance in mm.
    Arguments:
    vehicle_mass -- vehicle total mass in kg..
    rear_axle_mass -- rear axle mass in kg.
    mean_wheelbase -- mean wheelbase in mm.
    Return values:
    The longitudinal distance of the center of gravity in mm.
    """
    return (rear_axle_mass / vehicle_mass) * mean_wheelbase

def get_transverse_distance(front_track, rear_track, rear_right_mass,
                            rear_left_mass, front_left_mass, front_right_mass, vehicle_mass):
    """Return transverse distance in mm.
    Arguments:
    front_track -- front track in mm.
    rear_track -- rear track in .
    rear_right_mass -- rear right wheel mass in kg.
    rear_left_mass -- rear left wheel mass in kg.
    front_left_mass -- front left wheel mass in kg.
    front_right_mass -- front right wheel mass in kg.
    vehicle_mass -- total vehicle mass in kg.
    Return values:
    The transverse distance of the center of gravity in mm.
    """
    return ((front_track * (front_left_mass - front_right_mass))
            + (rear_track * (rear_left_mass - rear_right_mass))) / (2 * vehicle_mass)

def get_height(mean_wheelbase, lifted_rear_axle_mass, rear_axle_mass, vehicle_mass, lifted_angle, static_wheel_radius):
    """Return height of the center of gravity in mm.
    Arguments:
    Return values:
    The height of the center of gravity in mm.
    """
    return ((mean_wheelbase * (lifted_rear_axle_mass - rear_axle_mass))
            / (vehicle_mass * math.tan(lifted_angle))) + static_wheel_radius

def get_center_of_gravity(vehicle_mass, rear_axle_mass, mean_wheelbase, front_track,
                          rear_track, rear_right_mass, rear_left_mass, front_left_mass,
                          front_right_mass, lifted_rear_axle_mass, lifted_angle, static_wheel_radius):
    """Return a vehicle's center of gravity.
    Argument:
    longitudinal_distance -- the longitudinal distance of the center of gravity.
    transverse_distance -- the transverse distance of the center of gravity.
    height -- the height of the center of gravity.
    Return values:
    A tuple made up from the XYZ coordinates of the center of gravity in mm.
    """
    longitudinal_distance = get_longitudinal_distance(vehicle_mass, rear_axle_mass, mean_wheelbase)
    transverse_distance = get_transverse_distance(front_track, rear_track, rear_right_mass,
                                                  rear_left_mass, front_left_mass, front_right_mass, vehicle_mass)
    height = get_height(mean_wheelbase, lifted_rear_axle_mass, rear_axle_mass,
                        vehicle_mass, lifted_angle, static_wheel_radius)

    return longitudinal_distance, transverse_distance, height

#enter the lift height in mm
lbl_lift_height = Label(p3,text="Please enter the lift height in mm: ")
lbl_lift_height.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.04)

lift_height = Entry(p3)
lift_height.place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.04)

#enter the left wheelbase in mm
lbl_left_wheelbase = Label(p3,text="Please enter the left wheelbase in mm: ")
lbl_left_wheelbase.place(relx=0.1, rely=0.15, relwidth=0.3, relheight=0.04)

left_wheelbase = Entry(p3)
left_wheelbase.place(relx=0.65, rely=0.15, relwidth=0.1, relheight=0.04)

#Enter the right wheelbase in mm
lbl_right_wheelbase = Label(p3,text="Please enter the right wheelbase in mm: " )
lbl_right_wheelbase.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.04)

right_wheelbase = Entry(p3)
right_wheelbase.place(relx=0.65, rely=0.2, relwidth=0.1, relheight=0.04)

#Enter vehicle rear track in mm
lbl_rear_track = Label(p3,text="Please enter vehicle rear track in mm: " )
lbl_rear_track.place(relx=0.1, rely=0.25, relwidth=0.3, relheight=0.04)

rear_track = Entry(p3)
rear_track.place(relx=0.65, rely=0.25, relwidth=0.1, relheight=0.04)

#Enter vehicle front track in mm
lbl_front_track = Label(p3,text="Please enter vehicle front track in mm: ")
lbl_front_track.place(relx=0.1, rely=0.3, relwidth=0.3, relheight=0.04)

front_track = Entry(p3)
front_track.place(relx=0.65, rely=0.3, relwidth=0.1, relheight=0.04)

#Enter lifted vehicle wheel diameter in mm
lbl_wheel_diameter = Label(p3,text="Please enter lifted vehicle wheel diameter in mm: ")
lbl_wheel_diameter.place(relx=0.1, rely=0.35, relwidth=0.3, relheight=0.04)

wheel_diameter = Entry(p3)
wheel_diameter.place(relx=0.65, rely=0.35, relwidth=0.1, relheight=0.04)

#enter lifted vehicle flattened wheel diameter in mm
lbl_flattened_wheel_diameter = Label(p3,text="Please enter lifted vehicle flattened wheel diameter in mm: ")
lbl_flattened_wheel_diameter.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.04)

flattened_wheel_diameter = Entry(p3)
flattened_wheel_diameter.place(relx=0.65, rely=0.4, relwidth=0.1, relheight=0.04)

#Enter the rear left wheel mass in kg
lbl_rear_left_wheel_mass = Label(p3,text="Please enter the rear left wheel mass in kg: ")
lbl_rear_left_wheel_mass.place(relx=0.1, rely=0.45, relwidth=0.3, relheight=0.04)

rear_left_wheel_mass = Entry(p3)
rear_left_wheel_mass.place(relx=0.65, rely=0.45, relwidth=0.1, relheight=0.04)

#Enter the rear right wheel mass in kg
lbl_rear_right_wheel_mass = Label(p3,text="Please enter the rear right wheel mass in kg: ")
lbl_rear_right_wheel_mass.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.04)

rear_right_wheel_mass = Entry(p3)
rear_right_wheel_mass.place(relx=0.65, rely=0.5, relwidth=0.1, relheight=0.04)

#Enter the lifted rear left wheel mass in kg
lbl_front_left_wheel_mass = Label(p3,text="Please enter the lifted rear left wheel mass in kg: ")
lbl_front_left_wheel_mass.place(relx=0.1, rely=0.55, relwidth=0.3, relheight=0.04)

front_left_wheel_mass = Entry(p3)
front_left_wheel_mass.place(relx=0.65, rely=0.55, relwidth=0.1, relheight=0.04)

#Enter the lifted rear right wheel mass in kg
lbl_front_right_wheel_mass = Label(p3,text="Please enter the lifted rear right wheel mass in kg: ")
lbl_front_right_wheel_mass.place(relx=0.1, rely=0.6, relwidth=0.3, relheight=0.04)

front_right_wheel_mass = Entry(p3)
front_right_wheel_mass.place(relx=0.65, rely=0.6, relwidth=0.1, relheight=0.04)

#Enter the lifted rear left wheel mass in kg
lbl_lifted_rear_left_wheel_mass = Label(p3,text="Please enter the lifted rear right wheel mass in kg: ")
lbl_lifted_rear_left_wheel_mass.place(relx=0.1, rely=0.65, relwidth=0.3, relheight=0.04)

lifted_rear_left_wheel_mass = Entry(p3)
lifted_rear_left_wheel_mass.place(relx=0.65, rely=0.65, relwidth=0.1, relheight=0.04)

#Enter the lifted rear right wheel mass in kg
lbl_lifted_rear_right_wheel_mass = Label(p3,text="Please enter the lifted rear right wheel mass in kg: ")
lbl_lifted_rear_right_wheel_mass.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.04)

lifted_rear_right_wheel_mass = Entry(p3)
lifted_rear_right_wheel_mass.place(relx=0.65, rely=0.7, relwidth=0.1, relheight=0.04)


#Boton para calcular el centro de gravedad
calcular_centro_de_gravedad = Button(p3, text="Calcular", command=lambda: [
                                                                            get_lift_height(lift_height.get()),
                                                                            get_left_wheelbase(left_wheelbase.get()),
                                                                            get_right_wheelbase(right_wheelbase.get()),
                                                                            get_rear_track(rear_track.get()),
                                                                            get_front_track(front_track.get()),
                                                                            get_wheel_diameter(wheel_diameter.get()),
                                                                            get_flattened_wheel_diameter(flattened_wheel_diameter.get()),
                                                                            get_rear_left_wheel_mass(rear_left_wheel_mass.get()),
                                                                            get_rear_right_wheel_mass(rear_right_wheel_mass.get()),
                                                                            get_front_left_wheel_mass(front_left_wheel_mass.get()),
                                                                            get_front_right_wheel_mass(front_right_wheel_mass.get()),
                                                                            get_lifted_rear_left_wheel_mass(lifted_rear_left_wheel_mass.get()),
                                                                            get_lifted_rear_right_wheel_mass(lifted_rear_right_wheel_mass.get())
    ])

calcular_centro_de_gravedad.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)



root.mainloop()