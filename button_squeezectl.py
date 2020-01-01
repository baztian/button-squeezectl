#!/usr/bin/env python3

from signal import pause

from gpiozero import Button
from lms import Server

def loop(host, port, player_id):
  Button(15).wait_for_press()

  server = Server(host, port)
  print(server)
  p=server.player(player_id)
  p.play()
  p.pause()
  p.seek('-10')

  p.query('playlistcontrol', 'cmd:load', 'playlist_name:44-21-65-188-196')
  p.query('playlist', 'name', '?')
  p.query('playlist', 'playlistsinfo')

def main():
  import sys
  print(len(sys.argv))
  if len(sys.argv) != 4:
    print("Usage: button-squeezectl lms_host port player_id", file=sys.stderr)
    print("Example: button-squeezectl music 9000 b8:27:eb:d0:cc:13", file=sys.stderr)
    sys.exit(1)
  else:
    loop(sys.argv[1], int(sys.argv[2]), sys.argv[3])

if __name__ == "__main__":
  main()