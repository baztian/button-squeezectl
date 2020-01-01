# Control Logitech Squeezebox using GPIO buttons

Control Logitech Squeezebox using GPIO buttons.

## Setup

    sudo apt install python3-venv
    python3 -m venv --system-site-packages ~/button-squeezectl
    . ~/button-squeezectl/bin/activate
    pip install button-squeezectl
    button-squeezectl host:port player_id

## Develop

    pip install bump2version
    bumpversion patch
    git push && git push --tags
