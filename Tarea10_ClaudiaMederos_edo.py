import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def enviar_datos():
    nombre = entry_nombre.get()
    curp = entry_curp.get()
    rfc = entry_rfc.get()
    sexo = sexo_var.get()

    # Servicios seleccionados
    servicios = []
    if servicio1_var.get() == 1:
        servicios.append("Tutoría personalizada")
    if servicio2_var.get() == 1:
        servicios.append("Regularización académica")
    if servicio3_var.get() == 1:
        servicios.append("Preparación para exámenes")

    servicios_str = ", ".join(servicios) if servicios else "Ninguno"

    mensaje = (
        f"Nombre: {nombre}\n"
        f"CURP: {curp}\n"
        f"RFC: {rfc}\n"
        f"Sexo: {sexo}\n"
        f"Servicios de interés: {servicios_str}"
    )

    messagebox.showinfo("Datos del Cliente", mensaje)


# Ventana principal
ventana = tk.Tk()
ventana.title("Registro – Asesorías Educativas")
ventana.geometry("520x650")
ventana.config(bg="#f4f4f4")

# Ícono de la ventana
ventana.iconbitmap("icono.ico")

# ----- Imagen -----
imagen = Image.open("imagen.png")
imagen = imagen.resize((350, 180))
img = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(ventana, image=img, bg="#f4f4f4")
label_imagen.pack(pady=10)

# ----- Frame principal -----
frame = tk.Frame(ventana, bg="#f4f4f4")
frame.pack(pady=10)

# Nombre
tk.Label(frame, text="Nombre completo:", bg="#f4f4f4").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(frame, width=40)
entry_nombre.grid(row=0, column=1, pady=5)

# CURP
tk.Label(frame, text="CURP:", bg="#f4f4f4").grid(row=1, column=0, sticky="w")
entry_curp = tk.Entry(frame, width=40)
entry_curp.grid(row=1, column=1, pady=5)

# Estado de procedencia
tk.Label(frame, text="Estado de procedencia:", bg="#f4f4f4").grid(row=1, column=0, sticky="w")
entry_edo = tk.Entry(frame, width=40)
entry_edo.grid(row=3, column=1, pady=5)

# RFC
tk.Label(frame, text="RFC:", bg="#f4f4f4").grid(row=2, column=0, sticky="w")
entry_rfc = tk.Entry(frame, width=40)
entry_rfc.grid(row=2, column=1, pady=5)

# ----- Sexo (RadioButtons) -----
tk.Label(frame, text="Sexo:", bg="#f4f4f4").grid(row=3, column=0, sticky="w")

sexo_var = tk.StringVar()
sexo_var.set("Femenino")

radio_f = tk.Radiobutton(frame, text="Femenino", variable=sexo_var, value="Femenino", bg="#f4f4f4")
radio_m = tk.Radiobutton(frame, text="Masculino", variable=sexo_var, value="Masculino", bg="#f4f4f4")

radio_f.grid(row=4, column=1, sticky="w")
radio_m.grid(row=4, column=1, sticky="e")

# ----- Servicios (CheckButtons) -----
tk.Label(frame, text="Servicios de interés:", bg="#f4f4f4", pady=10).grid(row=5, column=0, sticky="w")

servicio1_var = tk.IntVar()
servicio2_var = tk.IntVar()
servicio3_var = tk.IntVar()

check1 = tk.Checkbutton(frame, text="Tutoría personalizada", variable=servicio1_var, bg="#f4f4f4")
check2 = tk.Checkbutton(frame, text="Regularización académica", variable=servicio2_var, bg="#f4f4f4")
check3 = tk.Checkbutton(frame, text="Preparación para exámenes", variable=servicio3_var, bg="#f4f4f4")

check1.grid(row=6, column=1, sticky="w")
check2.grid(row=7, column=1, sticky="w")
check3.grid(row=8, column=1, sticky="w")

# ----- Botón enviar -----
btn_enviar = tk.Button(ventana, text="Registrar Cliente", width=20, height=2, command=enviar_datos, bg="#4a90e2", fg="white")
btn_enviar.pack(pady=20)

ventana.mainloop()
