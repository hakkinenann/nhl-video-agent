NHL Video Agent 🏒

A Python-based project for automatically generating NHL player shift video clips using official NHL shift data and recorded game footage.

The goal is to build a tool that can identify when a selected player is on the ice, synchronize those shifts with a game recording, and automatically extract the corresponding video clips.


Project Status

🚧 Work in progress — early prototype

The project currently supports:

Retrieving player shift data from the NHL Stats API.

Filtering shifts by player and period.

Converting shift timestamps into seconds.

Mapping game time to video timestamps using manually defined synchronization points and linear interpolation.

Extracting video clips programmatically using Python and FFmpeg.


The first successful prototype has been tested using Aleksander Barkov's shifts from Game 6 of the 2025 Stanley Cup Final.

Current testing focuses on the third period of the game.


Technologies

Python — Data processing and automation

Requests — NHL API integration

FFmpeg — Video processing and clip extraction

Subprocess — Executing FFmpeg commands from Python

Git & GitHub — Version control


How It Works

1. Fetch shift data from the NHL Stats API.

2. Filter shifts for the selected player and period.

3. Convert shift start and end times into seconds.

4. Estimate video timestamps using manually identified synchronization points.

5. Calculate clip durations from the shift data.

6. Execute FFmpeg commands to extract video clips.


Video Synchronization

One of the main challenges is that NHL game time and video recording time do not progress at the same rate.

Game stoppages, commercial breaks, and intermissions introduce differences between the two timelines.

The current prototype uses linear interpolation between manually identified synchronization points to estimate where a shift occurs in the recording.