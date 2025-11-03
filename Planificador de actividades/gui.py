
import tkinter as tk #importar libreria para la interfaz gráfica
from tkinter import messagebox,ttk #importar messagebox y ttk para mejorar la interfaz gráfica

def iniciar_app():
    
     root=tk.Tk() #Crear la ventana principal
     root.tittle("Planificador de actividades") # Titulo de la ventana
     
     
     labelActividad=tk.Label(root,text="Nombre de la actividad:") #Crear una etiqueta para la entrada de actividades
     labelActividad.grid(row=1,column=0,padx=30, sticky="e") # e alinea a la derecha,w izquierda
     
     entryActividad=tk.Entry(root,width=20) #Crear un campo de entrada de texto
     entryActividad.grid(row=1, column=1,padx=30) #Alinear el campo de entrada junto a la etiqueta
     
     def mostrar_actividad():
     
       actividad=entryActividad.get() #Obtener el texto ingresado en el campo de entrada
       messagebox.showinfo("Actividad agregada",f"Actividad"{actividad}" agregada exitosamente.") #Mostrar un mensaje de confirmación
     
       botonMostrar=tk.Button(root,text="Agregar actividad",command=mostrar_actividad) # Crear un boton para agregar actividades
       botonMostrar.grid(row=2,column=0,columnspan=2,pady=10) # Alinear el boton debajo del campo de entrada y centrarlo
     
     root.mainloop() # Iniciar el bucle principal de la interfaz gráfica