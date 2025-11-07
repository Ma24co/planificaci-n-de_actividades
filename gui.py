import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from logic import add_task, delete_task, list_tasks_sorted, DATETIME_FMT
from storage import load_tasks, save_tasks
from reminder import ReminderManager


def iniciar_app():
    root = tk.Tk()
    root.title("Planificador de Actividades")

    tareas = load_tasks()
    reminder = ReminderManager(lambda t, m: messagebox.showinfo(t, m))
    reminder.start()
    reminder.schedule_for_tasks(tareas)

    def refrescar_lista():
        for item in tree.get_children():
            tree.delete(item)
        for t in list_tasks_sorted(tareas):
            tree.insert("", "end", iid=t["id"],
                        values=(t["title"], t["due_at"], "Sí" if t["done"] else "No"))

    def agregar_tarea():
        titulo = entryTitulo.get()
        fecha = entryFecha.get()
        if not titulo or not fecha:
            messagebox.showwarning("Error", "Complete todos los campos.")
            return
        try:
            add_task(tareas, titulo, "", fecha)
            save_tasks(tareas)
            reminder.schedule_for_tasks(tareas)
            refrescar_lista()
            entryTitulo.delete(0, "end")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def eliminar_tarea():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Atención", "Seleccione una tarea.")
            return
        delete_task(tareas, sel[0])
        save_tasks(tareas)
        refrescar_lista()

    tk.Label(root, text="Nombre de actividad:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entryTitulo = tk.Entry(root, width=25)
    entryTitulo.grid(row=0, column=1, padx=10)

    tk.Label(root, text=f"Fecha (formato {DATETIME_FMT}):").grid(row=1, column=0, padx=10, sticky="e")
    entryFecha = tk.Entry(root, width=25)
    entryFecha.insert(0, datetime.now().strftime(DATETIME_FMT))
    entryFecha.grid(row=1, column=1, padx=10)

    btnAdd = tk.Button(root, text="Agregar tarea", command=agregar_tarea)
    btnAdd.grid(row=2, column=0, columnspan=2, pady=10)

    tree = ttk.Treeview(root, columns=("Título", "Fecha", "Hecho"), show="headings", height=8)
    for col in ("Título", "Fecha", "Hecho"):
        tree.heading(col, text=col)
    tree.grid(row=3, column=0, columnspan=2, pady=10)

    btnDel = tk.Button(root, text="Eliminar seleccionada", command=eliminar_tarea)
    btnDel.grid(row=4, column=0, columnspan=2, pady=10)

    refrescar_lista()
    root.mainloop()
