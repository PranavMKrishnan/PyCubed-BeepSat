# Import cubesat- Starting point of all programs
from pycubed import cubesat

import os
import sys

for f in os.listdir("Tasks"):
    if f=="stop_tasks.py" or f=="task.py":
        continue
    str = "Tasks." + f[:-3]
    obj = __import__(str, globals(), locals(), [], 0)
    cubesat.scheduled_objects.append(
        cubesat.schedule(
            obj.Task(cubesat).frequency,
            obj.Task(cubesat).main_task,
            obj.Task(cubesat).priority,
            obj.Task(cubesat).task_id,
        )
    )
    print(cubesat.scheduled_objects)

cubesat.run()


"""
for i in os.listdir('Tasks'):
    exec('import Tasks.{}'.format(i[:-3]))
    str= 'Tasks.'+ i
    obj=eval(str[:-3])
    print(obj)
"""
