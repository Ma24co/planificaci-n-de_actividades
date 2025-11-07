from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from datetime import datetime
from logic import DATETIME_FMT

class ReminderManager:
    def __init__(self, notify_fn):
        self.notify_fn = notify_fn
        self.scheduler = BackgroundScheduler()

    def start(self):
        if not self.scheduler.running:
            self.scheduler.start()

    def schedule_for_tasks(self, tareas):
        now = datetime.now()
        for t in tareas:
            if t["done"]:
                continue
            try:
                dt = datetime.strptime(t["due_at"], DATETIME_FMT)
                if dt > now:
                    trigger = DateTrigger(run_date=dt)
                    self.scheduler.add_job(
                        self.notify_fn,
                        trigger=trigger,
                        args=["Recordatorio", f"La tarea '{t['title']}' vence pronto."]
                    )
            except Exception:
                continue
