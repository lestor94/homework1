from Storage import FileStorage
from Task import Task

class TodoApp():

    def __init__(self, storage):
        self.storage = storage

    def add_task(self):

        while True:
            task = input('Please enter task: ')
            priority = input('Enter priority: ')
            deadline = input("Is any deadline?: ")
            if task and priority:
                task = Task(task, priority, deadline)
                self.storage.save_data(task)
            if not input('Press enter to exit'):
                break

    def get_tasks(self):
        data = self.storage.get_data()


file_storage = FileStorage()