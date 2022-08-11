# hire-challenge
Challenge!

## Objectives.
Your goal is to make a task scheduler using the stub code.

### Purpose of Tasks and Scheduler

Tasks are run hourly with a parameter (`when`) set to the previous hour. For
example, a task running at 08:01 would be given the time 07:00 as its `when`
parameter. Tasks should be kept up to date so that the last time they were run
is always the last fully complete hour, and this is stored as `latest_done`.
Additionally, Tasks can 'back fill' back to a certain point in time
(`start_from`), and their progress toward that is stored as `earliest_done`.
Tasks may be stopped at a known point in the future by setting `repeat_until`.

The Scheduler is in charge of scheduling the tasks so that they are all kept up
to date, and back filled when there is time to do so. The Scheduler should:
- [x] Store tasks
- [x] Register new tasks
- [ ] Filter tasks to find what needs doing
- [ ] Schedule filtered tasks to prioritise those that have the nearest (i.e. most recent) to-do to right now
- [ ] Schedule filtered tasks to back fill tasks when there are no recent to-dos

### Your goals
In order of importance (first is most important):

- Most important - get 100% test coverage!
- Get all tests passing...
- Complete the incomplete methods in `challenge.py` (and cover with passing tests)
