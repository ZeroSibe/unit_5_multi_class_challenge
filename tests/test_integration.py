from lib.todo import Todo
from lib.todo_list import TodoList

"""
Given I #add two todos
It is reflected in the #incomplete list
"""

def test_add_multiple_todo_tasks_and_list_in_incomplete():
    todo_list = TodoList()
    todo_one = Todo('task one')
    todo_two = Todo('task two')
    todo_list.add(todo_one)
    todo_list.add(todo_two)
    assert todo_list.incomplete() == [todo_one, todo_two]

"""
Given I #add two todos
And I #mark_complete one of the todos
I see only one todos in the #incomplete list
"""

def test_add_two_todo_tasks_and_mark_complete_one_lists_one_incomplete():
    todo_list = TodoList()
    todo_one = Todo('task one')
    todo_two = Todo('task two')
    todo_list.add(todo_one)
    todo_list.add(todo_two)
    todo_one.mark_complete()
    assert todo_list.incomplete() == [todo_two]


"""
Given I #add two todos
And I #mark_complete one of the todos
I see only one todos in the #complete list
"""

def test_add_two_todo_tasks_and_mark_complete_one_lists_one_complete():
    todo_list = TodoList()
    todo_one = Todo('task one')
    todo_two = Todo('task two')
    todo_list.add(todo_one)
    todo_list.add(todo_two)
    todo_one.mark_complete()
    assert todo_list.complete() == [todo_one]


"""
Given I #add multiple todos
And I #give_up the todos
I see all todos in the #complete list
"""

def test_give_up_and_list_in_complete():
    todo_list = TodoList()
    todo_one = Todo('task one')
    todo_two = Todo('task two')
    todo_list.add(todo_one)
    todo_list.add(todo_two)
    todo_list.give_up()
    assert todo_list.complete() == [todo_one, todo_two] 