from logic import add_task, delete_task, DATETIME_FMT
from datetime import datetime, timedelta

def test_add_and_delete():
    tareas = []
    fecha = (datetime.now() + timedelta(hours=1)).strftime(DATETIME_FMT)
    t = add_task(tareas, "Test", "", fecha)
    assert t in tareas
    delete_task(tareas, t["id"])
    assert not tareas
