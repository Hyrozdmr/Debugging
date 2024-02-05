# {{PROBLEM}} Class Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Class Interface

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskTracker():
    def __init__(self, task):
        pass # No code here yet

    def add(self, task):
       # Parameters:
       #   Task: String representing a task 

    def list_incomplete(self):
        # Return:
        # A list incomplete tasks
        pass # No code here yet

    def mark_complete(self, index):
        # {Parameter}:
        #   index: An integer representing the task to complete reminding
        # Side-effects:
        #   Removes the task at index from the list of tasks
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Initially, There are no tasks

"""
tracker = TaskTracker()
tracker.list_incomplete() # => []

"""
When we add a task
It is reflected in the list of tasks

"""
tracker = TaskTracker()
tracker.add("study weekend")
tracker.listincomplete() # => ["study weekend"]

"""
When we add multiple task 
They are all reflected in the list of tasks

"""
tracker = TaskTracker()
tracker.add("study weekend")
tracker.add("learn python")
tracker.add("watch football game")
tracker.listincomplete() # => ["study weekend", "learn python", "watch football game"]

"""
When we add multiple task 
And mark one as completed
It disappers from the task 
"""
tracker = TaskTra)
tracker.add("learn python")cker()
tracker.add("study weekend"
tracker.add("watch football game")
tracker.mark_complete(0)
tracker.listincomplete() # => ["learn python", "watch football game"]

"""
if we try to mark task does not exist
It raises an error
"""
tracker = TaskTracker()
tracker.add("study weekend")
tracker.add("learn python")
tracker.mark_complete(2) # => Raises an error "No such task to mark complete

```


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
