#!/usr/bin/env python3

import signal

from gpiozero import Button
from lms import Server

class ButtonHandler:
  def __init__(self, host, port, player_id):
    self._host = host
    self._port = port
    self._player_id = player_id

  def play_pause(self, button):
    if button.is_held:
      return
    print("play/pause")
    self._player.query('pause')

  def seek_forward(self):
    print("seeking+20")
    self._player.seek('+20')

  def loop(self):
    server = Server(self._host, self._port)
    server.update()
    print(server)
    self._player=server.player(self._player_id)

    button = Button(15, hold_repeat=True, hold_time=3)
    button.when_released = self.play_pause
    button.when_held = self.seek_forward
  #  p.seek('-10')

  #  p.query('playlistcontrol', 'cmd:load', 'playlist_name:44-21-65-188-196')
  #  p.query('playlist', 'name', '?')
  #  p.query('playlist', 'playlistsinfo')
    signal.pause()

def main():
  import sys
  if len(sys.argv) != 4:
    print("Usage: button-squeezectl lms_host port player_id", file=sys.stderr)
    print("Example: button-squeezectl music 9000 b8:27:eb:d0:cc:13", file=sys.stderr)
    sys.exit(1)
  else:
    handler = ButtonHandler(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    handler.loop()

if __name__ == "__main__":
  main()