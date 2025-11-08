# GoTheFuckToSleep

A small Python program that reminds you of your bedtime by turning off your computer after a countdown.  

I tend to get stuck in social VR games way past my bedtime, so I created this program to solve that problem.  
Since I imagine I'm not the only one with this problem, I decided to share it here — maybe it can help someone. :)

## Features

- Simple Tkinter GUI (i know it's ugly) with a countdown.
- Buttons to select a time from the following options:  
  `4 hours`, `3 hours`, `2 hours`, `1 hour`, `45 minutes`, or `30 minutes`.
- Audio reminders that can be muted/unmuted at:  
  - 30 minutes  
  - 15 minutes  
  - 5 minutes  
  - Countdown at 10 seconds  

## Installation

1. Clone this repo

    ``` shell
    git clone https://github.com/EvelineFlowercrown/GoTheFToSleep
    cd GoTheFToSleep
    
    ```

2. Make sure you have **Python 3.11** and **pip3** installed:  

    ``` shell
    winget install python.python.3.13
    ```

3. Install Python dependencies

    ``` shell
    pip install -r requirements.txt
    ```

## Usage

1. Execute the program

    ``` shell
    python GoTheFuckToSleep.py

    ```

2. Click on the desired countdown time and choose whether you want audio reminders.  

3. Enjoy whatever usually keeps you up late. :)
