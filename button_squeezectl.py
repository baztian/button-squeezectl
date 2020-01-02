#!/usr/bin/env python3

import signal
from sys import stderr

from gpiozero import Button
from lms import Server

INITIAL_SEEK_OFFSET = 15
MAX_SEEK_OFFSET = INITIAL_SEEK_OFFSET * 4

class ButtonHandler:
  def __init__(self, host, port, player_id):
    self._host = host
    self._port = port
    self._player_id = player_id
    self._button_is_held = False
    self._seek_offset = INITIAL_SEEK_OFFSET

  def play_pause(self, button):
    print("Button held: {}".format(self._button_is_held))
    if self._button_is_held:
      self._button_is_held = False
      self._seek_offset = INITIAL_SEEK_OFFSET
      return
    print("play/pause")
    self._player.query('pause')

  def seek_forward(self):
    self._button_is_held = True
    seek = '+{}'.format(min(self._seek_offset, MAX_SEEK_OFFSET))
    print("seeking", seek)
    self._player.seek(seek)
    self._seek_offset *= 2

  def loop(self):
    server = Server(self._host, self._port)
    server.update()
    try:
      self._player=server.player(self._player_id)
    except (KeyError) as e:
      print(server, file=stderr)
      raise Exception("Player {} not found".format(self._player_id)) from e

    button = Button(23, hold_repeat=True, hold_time=3)
    button.when_released = self.play_pause
    button.when_held = self.seek_forward

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