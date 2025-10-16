class TodoList:
    def __init__(self):
        self._todos = []

    def add(self, todo):
        self._todos.append(todo)

    def incomplete(self):
        return [todos for todos in self._todos if todos.complete == False]

    def complete(self):
        return [todos for todos in self._todos if todos.complete == True]

    def give_up(self):
        if self._todos == []:
            raise Exception('No tasks added yet')
        [setattr(todos, 'complete', True) for todos in self._todos]