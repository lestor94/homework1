import datetime
class Task():

    def __init__(self, task, priority, deadline=0):
        self.task = task
        self.priority = priority
        self.deadline = deadline
        self.date = datetime.datetime.now()
        self.id = int(self.get_id()) +1

    def get_id(self):
        with open('id_counter','w') as id_file:
            return id_file.read().strip()

    def update_id(self):
        with open('id_counter','w') as id_file:
            id_file.write(self.id)
if __name__ == '__main__':
    t1 = Task(1,1)
    t2 = Task(2,2)
    print(Task.ID)