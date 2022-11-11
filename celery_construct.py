
import celery

from Controller.handle_task_background import HandleTask

celery = celery.Celery(
    "abc",
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)


@celery.task()
def create_task():
    HandleTask.worker_task_3()




