# Monster Tracker

Programmed for Honkai: Star Rail (v2.2) daily farmers using this [route](https://www.prydwen.gg/star-rail/guides/daily-farming-route) or something similar.
It serves as a counter and tracker for monster kill timestamps and map switch timestamps for **analytic purposes**, aiming at finding a better route than the one proposed. Don't get me wrong, the current one is very good to save on Trick Snacks. The only problem is that it takes too much time, even using Acheron.

This program is not aimed at the daily Honkai user, just for data nerds.

## Requirements
This program uses [Python](https://www.python.org), a language that allows fast programming, and the `pynput` library to read keyboard presses. Code is available to read and commented so you know what the program reads and does with it.

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
- `Escape` to exit and save file.

The recording is saved in the `output` directory.

### What to do with the output?
- If you happen to use the program and no better routes have been posted on [Prydwen](https://www.prydwen.gg/star-rail/), please do send it to [me](#contacts) so I can analyze it!

## What next?
I plan to make another program that uses the output of the Monster Tracker to find better routes using the Monster Density metric to get the best "bang for your bucks", a short but dense route.

## Any suggestions?
I also take suggestions to help the Honkai: Star Rail community!

## Contacts
Discord: .firis, also find me on the [Prydwen Discord](https://discord.gg/prydwen)!