from tkinter import *
import random

#-------------------------------------------------
# FUNCIONES PARA FUNCIONAR LA FUNCIÓN
#-------------------------------------------------

def jugar(eleccion):
    opciones = ["piedra", "papel", "tijera"]
    pc = random.choice (opciones)

    if eleccion == pc:
        res = f"Empate: {eleccion} vs {pc}, no está tan mal."
    elif (eleccion == "piedra" and pc == "tijera") or \
         (eleccion == "papel" and pc == "piedra") or \
         (eleccion == "tijera" and pc == "papel"):
        res = f"Ganaste, ¡yeiii!: {eleccion} vs {pc}"
    else:
        res = f"Perdiste, que mal: {eleccion} vs {pc}"

    t_resultados.delete("1.0", END)
    t_resultados.insert(END, res)

#------------------------------------------------------
# ventana principal
#------------------------------------------------------

ventana = Tk()
ventana.title("Piedra Papel o Tijeras")
ventana.geometry("800x500")
ventana.config(bg="violet")

# etiqueta para el titulode la app
titulo = Label(ventana,text="ESCOGE UNA OPCIÓN")
titulo.config(bg="pink", fg="white",font=("arial",16))
titulo.place(x=278,y=10)

# imagen logo de la app
logo = PhotoImage(file="img/logo.png")
Label_logo=Label(ventana, image=logo)
Label_logo.place(x=305,y=100)

# Botnes
img_piedra = PhotoImage(file="img/piedra.png")
Button(ventana, image=img_piedra, command=lambda: jugar("piedra")).place(x=135, y=220)

img_papel = PhotoImage(file="img/papel.png")
Button(ventana, image=img_papel, command=lambda: jugar("papel")).place(x=335, y=220)

img_tijera = PhotoImage(file="img/tijera.png")
Button(ventana, image=img_tijera, command=lambda: jugar("tijera")).place(x=535, y=220)

# Resultado
t_resultados = Text(ventana, width=50, height=3, bg="pink", fg="white", font=("Arial", 20))
t_resultados.place(x=20, y=350)

ventana.mainloop()