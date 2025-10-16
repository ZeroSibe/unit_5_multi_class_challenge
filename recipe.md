# TodoList Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a User
I can create a task

As a User 
I can mark my task complete

As a User
I can add a task

As a User
I can see a list of incomplete task

As a User
I can see a list of complete task

As a User 
I can mark all tasks as complete


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ TodoList                   │
│                            │
│ - todos                    │
│ - add(todo)                │
│ - incomplete()             │
│   => [{Todos,False}...]    │
| - complete()               |
|  => [{Todos, True}...].    |
| - give_up()
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Todo(task)              │
│                         │
│ - task                  │
│ - complete              │
│ - mark_complete()       │
│                         │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class TodoList:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python

"""
Given I #add two todos
It is reflected in the #incomplete list
"""


    todo_list = TodoList()
    todo_one = Todo('task one')
    todo_two = Todo('task two')
    todo_list.add(todo_one)
    todo_list.add(todo_two)
    todo_list.incomplete() #==> [todo_one, todo_two]

"""
Given I #add two todos
And I #mark_complete one of the todos
I see only one todos in the #incomplete list
"""

    todo_list = TodoList()
    todo_one = Todo('task one')
    todo_two = Todo('task two')
    todo_list.add(todo_one)
    todo_list.add(todo_two)
    todo_one.mark_complete()
    todo_list.incomplete() #==> [todo_two]


"""
Given I #add two todos
And I #mark_complete one of the todos
I see only one todos in the #complete list
"""

    todo_list = TodoList()
    todo_one = Todo('task one')
    todo_two = Todo('task two')
    todo_list.add(todo_one)
    todo_list.add(todo_two)
    todo_one.mark_complete()
    todo_list.complete() #==> [todo_one]


"""
Given I #add multiple todos
And I #give_up the todos
I see all todos in the #complete list
"""

    todo_list = TodoList()
    todo_one = Todo('task one')
    todo_two = Todo('task two')
    todo_list.add(todo_one)
    todo_list.add(todo_two)
    todo_list.give_up()
    todo_list.complete() #==> [todo_one, todo_two] 

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

"""
Initially, when we create a new todo
with task
We get it's `task` and it's `complete` status as False back
"""

todo = Todo('task 1')
todo.task #==> 'task 1'
todo.complete #==> False


"""
TodoList
Initially, #incomplete todos is an empty list
"""

todo_list = TodoList()
todo_list.incomplete() #==> []


"""
TodoList
Initially, #complete todos is an empty list
"""

    todo_list = TodoList()
    todo_list.complete() #==> []

"""
When we create a new todo task 
and #mark_complete that task
We get it's `task` and it's `complete` status as True back
"""

    todo = Todo('task 1')
    todo.mark_complete()
    todo.task #==> 'task 1'
    todo.complete #==> True


"""
TodoList
Initially, #give_up raises error
"""

todo_list = TodoList()
todo_list.give_up() #==> 'No tasks added yet'

"""
Given an invalid task,
Throws error 
"""
 todo = Todo(123) #=> "Invalid task entry, please provide a string"

"""
Given a task as an empty string,
Throws error 
"""

todo = Todo("") #=> "No task provided"




```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
