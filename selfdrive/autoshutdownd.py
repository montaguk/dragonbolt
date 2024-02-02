#!/usr/bin/env python3

import os
import time
import cereal.messaging as messaging


def main():

  shutdown_at = 60
  shutdown_count = 0
  device_state_sock = messaging.sub_sock('deviceState')

  while 1:
    msg = messaging.recv_sock(device_state_sock, wait=True)
    if msg is not None:
      if not msg.deviceState.usbOnline and not msg.deviceState.started:
        shutdown_count += 5
      else:
        shutdown_count = 0
    else:
      shutdown_count = 0

    print('current', shutdown_count, 'shutdown_at', shutdown_at)

    # Don't actually shutdown since this is C2 and doesn't have a battery
    # If we are on, we have USB and we are good to go
    # if shutdown_count >= shutdown_at > 0:
    #   os.system('LD_LIBRARY_PATH="" svc power shutdown')

    time.sleep(5)


if __name__ == "__main__":
  main()
