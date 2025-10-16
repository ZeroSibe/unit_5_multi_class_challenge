class Todo:
    def __init__(self, task):
        if not isinstance(task, str):
            raise TypeError("Invalid task entry, please provide a string")
        if task == "":
            raise Exception("No task provided")
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True