from datetime import datetime
from uuid import uuid4

DATETIME_FMT = "%Y-%m-%d %H:%M"


def add_task(tareas, title, description, due_at):
    datetime.strptime(due_at, DATETIME_FMT)  # valida formato
    tarea = {
        "id": str(uuid4()),
        "title": title.strip(),
        "description": description,
        "due_at": due_at,
        "done": False
    }
    tareas.append(tarea)
    return tarea


def delete_task(tareas, task_id):
    for i, t in enumerate(tareas):
        if t["id"] == task_id:
            tareas.pop(i)
            return
    raise KeyError("Tarea no encontrada")


def list_tasks_sorted(tareas):
    return sorted(tareas, key=lambda t: t["due_at"])
