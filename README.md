# hire-challenge
Challenge!

## Objectives.
Your goal is to make a task scheduler using the stub code. Please don't fret
about this challenge too much; enjoy it if possible 🤓
We're not looking for a perfect solution or even a complete solution; we just
need something that you've worked on to discuss, that we also understand! So:

- Don't spend more than 1 hour on it (unless you actually want to)
- If you do spend more than 1 hour on it - just log how long you spend
- We'll talk over what you did in the interview
- We may go into a pairing exercise on this code in the interview

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
- [ ] Scheduled tasks should keep track of their progress (forward and backward in time)

### Your goals
In order of importance (first is most important):

- Most important - keep 100% test coverage!
- Get all existing tests passing
- Complete the incomplete methods in `challenge.py` according to the above description of the purpose.
- Ensure you keep 100% test coverage!
