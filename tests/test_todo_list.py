import pytest
from lib.todo_list import TodoList

"""
Initially, #incomplete todos is an empty list
"""

def test_initially_has_no_incomplete_todos():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

"""
Initially, #complete todos is an empty list
"""

def test_initially_has_no_incomplete_todos():
    todo_list = TodoList()
    assert todo_list.incomplete() == []

"""
Initially, #give_up raises error
"""

def test_initially_give_up_raises_error():
    todo_list = TodoList()
    with pytest.raises(Exception) as e:
        todo_list.give_up()
    assert str(e.value) == 'No tasks added yet'






