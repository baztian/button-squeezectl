# Control Logitech Squeezebox using GPIO buttons

Control Logitech Squeezebox using GPIO momentary buttons.

## Setup

    sudo apt install python3-venv
    python3 -m venv --system-site-packages ~/button-squeezectl
    . ~/button-squeezectl/bin/activate
    pip install rpi.gpio button-squeezectl
    button-squeezectl host port player_id

## Usage

Currently it is hard coded to GPIO 18. A single press of the button will switch between play and pause. Holding the button will do a progressive fast forward: Holding it for at least 3 seconds will do a relative seek (fast forward) plus 15 seconds. Holding the button for another 3 seconds will skip again but double the seconds getting skipped. Holding it further will continue skipping and double until it has reached a skip amount of 60 seconds.

## Develop

    pip install bump2version
    bumpversion patch
    git push && git push --tags
