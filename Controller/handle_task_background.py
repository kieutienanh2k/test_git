
import time


class HandleTask:
    @staticmethod
    def worker_task():
        time.sleep(5)
        print("abc")

    @staticmethod
    def worker_task_2():
        time.sleep(3)
        print("mno")

    @staticmethod
    def worker_task_3():
        time.sleep(1)
        print("xyz")
