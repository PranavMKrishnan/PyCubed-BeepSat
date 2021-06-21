class StopTask:
    def __init__(self, satellite, num_of_tasks, task_ids):
        self.cubesat = satellite
        self.num = num_of_tasks
        self.task_id_list = task_ids
        self.count = 0

    def stop(self):
        for task in self.cubesat.scheduled_objects:
            if task.get_task_id() in self.task_id_list:
                task.stop()
                self.count = self.count + 1
        assert self.count == self.num, "Multiple tasks have the same task_id!"
