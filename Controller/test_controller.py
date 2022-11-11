
from celery_construct import create_task


class ApiController:

    @staticmethod
    def handle_task():
        print("mno")
        task = create_task.delay()
        print(task.id)
        return {
            "data": task.id
        }

