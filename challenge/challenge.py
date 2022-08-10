from dataclasses import dataclass
from datetime import datetime
from typing import Union, List


@dataclass
class HourlyTask:
    """A task to be done every hour, and backfilled if not up to date."""

    #: From when should this task start occurring?
    start_from: datetime

    #: Until when should this task occur?
    repeat_until: Union[datetime, None] = None

    #: What, if any, is the first time that has been done for this task?
    earliest_done: Union[datetime, None] = None

    #: What if any is the last (most recent) time that has been done for this
    #: task?
    latest_done: Union[datetime, None] = None

    @property
    def next_to_do(self) -> Union[datetime, None]:
        """Return the next datetime that needs doing."""


class Scheduler:
    """Schedule some work."""

    def __init__(self):
        """Initialise Scheduler."""
        self.task_store = []

    def register_task(self, task: HourlyTask) -> None:
        """Add a task to the local store of tasks known about."""
        self.task_store.append(task)

    def register_tasks(self, task_list: List[HourlyTask]) -> None:
        """Add several tasks to the local store of tasks."""
        [self.register_task(task) for task in task_list]

    def get_tasks_to_do(self) -> List[HourlyTask]:
        """Get the list of tasks that need doing."""

    def schedule_tasks(self, task_list: List[HourlyTask]) -> None:
        """Schedule the tasks in the list.

        Tasks should be prioritised so that tasks with a recent "to do" date
        are done before any that need backfilling.
        """
