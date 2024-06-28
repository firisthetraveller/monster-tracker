# Monster Tracker

Programmed for Honkai: Star Rail (v2.2) daily farmers using this [route](https://www.prydwen.gg/star-rail/guides/daily-farming-route) or something similar.
It serves as a counter and tracker for monster kill timestamps and map switch timestamps for **analytic purposes**, aiming at finding a better route than the one proposed. Don't get me wrong, the current one is very good to save on Trick Snacks. The only problem is that it takes too much time, even using Acheron.

This program is not aimed at the daily Honkai user, just for data nerds.

## Requirements
This program uses [Python](https://www.python.org), a language that allows fast programming, and the `pynput` library to read keyboard presses. Code is available to read and commented so you know what the program reads and does with it.

### macOS X
From the `pynput` [documentation](https://pythonhosted.org/pynput/keyboard.html#monitoring-the-keyboard):
> One of the following must be true:
> - The process must run as root.
> - Your application must be white listed under Enable access for assistive devices. Note that this might require that you package your application, since otherwise the entire Python installation must be white listed.

### Windows
Also from the same [documentation](https://pythonhosted.org/pynput/keyboard.html#monitoring-the-keyboard):
> On Windows, virtual events sent by other processes may not be received. This library takes precautions, however, to dispatch any virtual events generated to all currently running listeners of the current process.

## Usage
### Installing and launch
Using a terminal:
```sh
pip3 install -r requirements.txt
python3 counter.py
```

### While in the program
Press:
- `x` to count monsters.
- `c` to mark map change.
- `r` to restart recording.
- `Escape` to exit and save file.

The recording is saved in the `output` directory.

### What to do with the output?
- Analyze it!
- Here's my result for example:
![Monster Density Plot](https://raw.githubusercontent.com/firisthetraveller/monster-tracker/main/images/Figure_2.png)

## What next?
Routing!

## Any suggestions?
I also take suggestions to help the Honkai: Star Rail community!

## Contacts
Discord: .firis, also find me on the [Prydwen Discord](https://discord.gg/prydwen)!