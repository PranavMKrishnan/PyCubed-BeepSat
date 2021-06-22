Implementing a simple "BeepSat"
===============================

A simple method to understand the framework of the PyCubed software, is to implement a "BeepSat". The "BeepSat" beacons "Hello World!" once every second, transmits IMU sensor data (Gyro Readings) once every 10 seconds, and listens for a "killswitch" command, every second. 

Once the "killswitch" command is received, execution of all tasks is ended.

The ``task`` files required for the implementation of the "BeepSat" are below.

.. _ref_name:

``task`` file to listen for messages  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

	# Task to listen for "killswitch" command on Radio
	import Tasks.stop_tasks as stop_tasks

	class Task:
    		def __init__(self, satellite):
        		self.cubesat = satellite
        		self.include = True
        		self.cubesat.radio2.listen()

    		def __await__(self):

        		while self.cubesat.radio2.rx_done() == 0:
            		yield
        		message = self.cubesat.radio2.receive()
        		msg_text = str(message, "ascii")
        		if msg_text == "killswitch":
            		print("Sending message.....")
            		self.cubesat.radio2.send(
                		"Killswitch received, Bye World......", keep_listening=True
            		)

            		#Stop desired tasks
            		stop_tasks.StopTask(self.cubesat, 3, [1,2,3]).stop()

    		async def main_task(self):
        		print("Awaiting message")
        		await self
        		print("Done awaiting message")

    		priority = 1
    		frequency = 1
    		task_id = 1


``task`` file to transmit IMU Readings  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

	# Task to obtain IMU sensor readings

	class Task:
    		def __init__(self, satellite):
        		self.cubesat = satellite

    		async def main_task(self):
        		reading = self.cubesat.IMU.gyro
        		print("Sending Gyro Readings....")
        		self.cubesat.radio2.send(','.join(map(str,reading)), keep_listening=True)
        		print("Done Sending Gyro Readings")

    		priority = 2
    		frequency = 1/10
    		task_id = 2


``task`` file to transmit "Hello World!"  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

	# Task to send "Hello World" on the radio

	class Task:
    		def __init__(self, satellite):
        		self.cubesat = satellite

    		async def main_task(self):
        		print("Sending message from PyCubed....")
        		self.cubesat.radio2.send("Hello World!", keep_listening=True)
        		print("Message sent from PyCubed")

    		priority = 3
    		frequency = 1
    		task_id = 3


.. note ::

   To run the tasks on PyCubed refer to this link- :ref:`ref`.
