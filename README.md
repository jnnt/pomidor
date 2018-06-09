## Do not disturb, I'm in the middle of a pommodoro!

I think I need a visual cue for my coworkers to see if I am busy and need some quiet time.

I sometimes use the [Pomodoro technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) when I am trying to get some work done.
* to track Pomodoros I use [Toggl](https://toggl.com) + Chrome plugin. The plugin starts timer for a Toggl task and automatically stops after 25 minutes.
* this setup polls Toggl API to see if I have an active time entry (i.e. I'm working on something)
* depending on the API query result, a physicl 'pomodoro' flag is raised or lowered. I am using a MicroPython board connected through USB (serial) and a servo motor (pics and description coming soon)

