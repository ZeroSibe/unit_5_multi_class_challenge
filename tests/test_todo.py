import pytest
from lib.todo import Todo

"""
Initially, when we create a new todo
with task
We get it's `task` and it's `complete` status as False back
"""
def test_construct_task_and_get_task_and_complete_status():
    todo = Todo('task 1')
    assert todo.task == 'task 1'
    assert todo.complete == False

"""
When we create a new todo task 
and #mark_complete that task
We get it's `task` and it's `complete` status as True back
"""

def test_mark_complete_task_and_get_complete_status_false():
    todo = Todo('task 1')
    todo.mark_complete()
    assert todo.task == 'task 1'
    assert todo.complete == True

"""
Given an invalid task,
Throws error 
"""
def test_invalid_task_entry_raises_error():
    with pytest.raises(TypeError) as e:
        todo = Todo(123)
    assert str(e.value) == "Invalid task entry, please provide a string"

def test_empty_task_entry_raises_error():
    with pytest.raises(Exception) as e:
        todo = Todo("")
    assert str(e.value) == "No task provided"