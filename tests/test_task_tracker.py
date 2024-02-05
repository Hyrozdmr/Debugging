import pytest
from lib.task_tracker import *
"""
Initially, There are no tasks
"""
def test_if_there_are_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []
 
"""
When we add a task
It is reflected in the list of tasks

"""
def test_add_task_reflected_in_tasks():
    tracker = TaskTracker()
    tracker.add("study weekend")
    assert tracker.list_incomplete() == ["study weekend"]

"""
When we add multiple task 
They are all reflected in the list of tasks

"""
def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("study weekend")
    tracker.add("learn python")
    tracker.add("watch football game")
    assert tracker.list_incomplete() == ["study weekend", "learn python", "watch football game"]

"""
When we add multiple task 
And mark one as completed
It disappers from the task 
"""
def test_mark_tasks_copmlete():
    tracker = TaskTracker()
    tracker.add("learn python")
    tracker.add("study weekend")
    tracker.add("watch football game")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == ["learn python", "watch football game"]

"""
if we try to mark task does not exist
It raises an error
"""
def test_mark_task_is_too_low_complete():
    tracker = TaskTracker()
    tracker.add("study weekend")
    with pytest.raises(Exception) as err:
      tracker.mark_complete(-1)
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["study weekend"]