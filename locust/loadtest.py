from random import random

from . import TaskSet, runners


class LoadtestTaskSet(TaskSet):

    repeat_threshold = 0.3
    """Defines how often a given task should be repeated. Default 30%"""

    def __init__(self, *args, **kwargs):
        super(LoadtestTaskSet, self).__init__(*args, **kwargs)
        self.current_task_idx = 0

    def get_next_task(self):
        if self.current_task_idx < len(self.tasks):
            next_task = self.tasks[self.current_task_idx]
            self.current_task_idx += 1
            if random() < self.repeat_threshold:
                self.current_task_idx -= 1
            return next_task
        runners.locust_runner.stop()
