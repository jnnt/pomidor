## Do not disturb, I'm in the middle of a pomodoro!

`pomidor` == tomato in Polish

I think I need a visual cue for my coworkers to see if I am busy and would prefer to avoid interruptions. They may get a little distracted every time I start/stop my [Pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) timer but that's a sacrifice I am willing to make ;>

* to track Pomodoros I use [Toggl](https://toggl.com) + Chrome plugin. The plugin starts timer for a Toggl task and automatically stops after 25 minutes.
* this setup polls Toggl API to see if I have an active time entry (i.e. I'm working on something)
* depending on the API query result, a physical 'pomodoro' flag is raised or lowered. I am using a MicroPython board connected through USB (serial) and a servo motor (HXT500). My ultra-professional flag is made from a drinking straw and a piece of paper colored with red isolation tape.
* if you do your own Pomodoro flag you should totally use googly eyes

Here it is in action: https://photos.app.goo.gl/NbSyeTXG1vy9MM5KA 

![hardware img](https://lh3.googleusercontent.com/JyYk-AufSYQD7SBq7ILhtbM-SrZ3e_sMbshcCB6PgVDzM4EM-sdc4r4ARyn_LFobwAf5X9ynhN54FWXU70frG1R9KZC5Txb-RyyHH_z2v8OskbleVvN_J64w3PyC1L7ZqwgAOhKM-6M=w720-h959-no)

TODO (maybe, someday):
* refactor
* CLI for raising/lowering the flag 'manually'
* Ansible plugin to activate the flag for playbooks which require more attention
