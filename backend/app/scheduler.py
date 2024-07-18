from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def blanket_control_task():
    print(f"Blanket control task executed at {datetime.now()}")

scheduler = BackgroundScheduler()
scheduler.add_job(func=blanket_control_task, trigger="interval", minutes=10)
scheduler.start()