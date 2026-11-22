NHL Video Agent

A Python-based project exploring how NHL player shift data can be used to automate the creation of player-specific video clips from full game recordings.

Project Overview

The goal is to build a tool that identifies when a selected NHL player is on the ice and uses that information to extract the corresponding segments from a game recording.

The project also serves as a practical learning environment for Python development, API integration, video processing, and AI-assisted software engineering.

Current Features

Retrieve player shift data from the NHL Stats API.

Parse JSON responses and filter shifts by player.

Extract shift information, including period, start time, and end time.

Convert time values into seconds for further processing.

Planned Features

Convert player shifts into game-wide timestamps.

Synchronize official game timestamps with local video recordings.

Automatically extract player-specific clips using FFmpeg.

Explore AI agents and computer vision to improve video processing and automation.

Technologies

Python 3.12

NHL Stats API

Requests

Git and GitHub

Planned tools include FFmpeg, OpenCV, and AI-assisted development tools.

Project Status

Work in progress

The project currently focuses on retrieving and processing NHL shift data. Video synchronization and automated clip extraction are planned for future development.

Example Use Case

Given an NHL game and a selected player, such as Aleksander Barkov:

Retrieve the official shift data for the game.

Identify the player's shifts.

Convert shift times into a format suitable for video processing.

Match the shifts to the game recording.

Generate video clips containing the player's ice time.

Steps 4–5 are not yet implemented.
