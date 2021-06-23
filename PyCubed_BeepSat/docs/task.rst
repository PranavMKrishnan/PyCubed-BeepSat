Writing a Task on PyCubed
=========================

All the operations performed by the cubesat via the PyCubed board, are in the form of tasks. A ``task`` file is written, and pasted in the **Tasks** directory on the PYCUBED drive.

.. _reference_name:

Understanding the Task File Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``task`` file consists of the ``Task`` object that encapsulates the function to be performed. 

.. autoclass:: task.Task
   :members:
   :special-members:
   :exclude-members: __weakref__

.. note ::

   The method ``main_task`` is NOT a regular function. It is a coroutine. Execution of coroutines does not take place in the same manner as execution of regular functions. While the scheduler in ``code.py`` abstracts the complexities of coroutines from the user, it may be a good idea to explore the basics of the same, through `this`_ link.

.. warning ::

   The class in the ``task`` files **MUST** be named ``Task`` while the main async method/coroutine to be scheduled **MUST** be named ``main_task``. This is due to the way the files are imported and scheduled in ``code.py``. Not adhering to the template will result in errors.

.. _this: https://docs.python.org/3/library/asyncio-task.html

On boot-up, the ``code.py`` script imports all these tasks and schedules them based on the specifications provided in the tasks. 

.. _ref:

Steps to execute Tasks on PyCubed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1) Follow the template mentioned in :ref:`reference_name` to write the ``task`` file.
2) Paste the ``task`` file in the **Tasks** folder.
3) Reset or reboot the board. 

The ``task`` file is automatically imported upon boot, leading to its execution at the specified frequency, with the specified priority level.

A Simple Example 
~~~~~~~~~~~~~~~~~

The example below demonstrates the simple task of sending the message "Hello World!" through the radio at a frequency of 1 Hz. ::

	# Task to send "Hello World" on the radio at a frequency of 1Hz

	class Task:
    		def __init__(self, satellite):
        		self.cubesat = satellite

    		async def main_task(self):
        		print("Sending message from PyCubed....")
        		self.cubesat.radio2.send("Hello World!", keep_listening=True)
        		print("Message sent from PyCubed")

    		priority = 1
    		frequency = 1
    		task_id = 4
                schedule_later = False

The above example sets the priority of the task to 1, sets the task ID to 4, and sets the execution rate of the task to 1 Hz. 

To run this example, create a ``task`` file (can be named anything, for example: ``radio_send_task.py``), and copy the code onto that file.
Paste this file in the **Tasks** folder on PYCUBED, and then reset the board using Ctrl+D. 
The task will automatically be executed, at the specified frequency.

Stopping Tasks on PyCubed
~~~~~~~~~~~~~~~~~~~~~~~~~~

In certain situations, some tasks may have to be stopped from within another task.

For example: If we want to end all tasks upon receiving a "killswitch" command on the radio.

For this purpose a ``StopTask`` object is used, which resides in the ``stop_tasks.py`` script. 

.. autoclass:: stop_tasks.StopTask
   :members:
   :special-members:
   :exclude-members: __weakref__

An example is provided here- :ref:`ref_name`. 

.. warning ::

   Do not forget to import the ``StopTask`` object from the ``stop_tasks.py`` module when using this functionality.