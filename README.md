# Hiring Challenge
Challenge!

## Objectives.
Your goal is to make a task scheduler using the stub code. Please don't fret
about this challenge too much; enjoy it if possible 🤓
We're not looking for a perfect solution or even a complete solution; we just
need something that you've worked on to discuss, that we also understand! So:

- We don't expect you to spend more than 1 hour on it (unless you want to!)
- If you *do* spend more than 1 hour on it - please log how long you spend
- Please **fork this repository** to your own GitHub account
- Please try to make **regular, atomic commits** to a **branch** (even if they are WIP (Work In Progress) commits).
- Make a **Pull Request**, which we will use to review your changes.
- We'll talk over what you did in the interview
- We may go into a pairing exercise on this code in the interview

### Purpose of Tasks and Scheduler

Tasks are run hourly. They will operate on an hour's worth of data (i.e. an hour
"period"), with the start of that period being given as a parameter (`when`).
Ordinarily, this `when` parameter would be set to the **previous complete hour**.


For example, a task running at 08:01 would be given the time 07:00 as
its `when` parameter, which would cover teh period of 07:00 to 08:00.


Tasks should be kept up to date so that the latest period they have completed is
for the last fully complete hour, and this time (e.g. 07:00 in the example) is
stored as `latest_done`.


Additionally, Tasks can '**back fill**' to a certain point in the past
(`start_from`), and their progress back in time toward that is stored as
`earliest_done`.

For example, a task that has completed its latest period
should move to back fill an older period until `earliest_done` is the same as
`start_from`.


Tasks may be stopped at a known point in the future by setting `repeat_until`.


The Scheduler is in charge of scheduling the tasks so that they are all kept up
to date, and back filled when there is time to do so. The Scheduler should:
- [x] Store tasks
- [x] Register new tasks
- [ ] Filter tasks to find what needs doing
- [ ] Schedule filtered tasks to prioritise those that have the nearest (i.e. most recent) to-do period right now
- [ ] Schedule filtered tasks to back fill periods when there are no recent to-do periods
- [ ] Scheduled tasks should keep track of their progress (forward and backward in time)

The checked tasks above are "done", but you may wish to reimplement them.

### Your goals
In order of importance (first is most important):

- Most important - keep 100% test coverage!
- Get all existing tests passing
- Complete the incomplete methods in `challenge.py` according to the above description of the purpose.
- Ensure you keep 100% test coverage!

## Don't forget

- Fork it
- Commit regularly
- Make a Pull Request
- Enjoy!
