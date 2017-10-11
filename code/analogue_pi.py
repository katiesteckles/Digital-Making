#!/usr/bin/env python

import signal

import explorerhat


print("""
This example shows how you can monitor an analog input by attaching a function to its changed event.

You should see the analog value being printed out as it changes.

Try connecting up a rotary potentiometer or analog sensor to input one.

Press CTRL+C to exit.
""")

def handle_analog(pin, value):
    print(pin.name, value)
    # Set all outputs off every time.
    # This is clunky, but fast enough not to make things flash.
    explorerhat.output.one.off()
    explorerhat.output.two.off()
    explorerhat.output.three.off()
    # Now check the value, and turn on a corresponding number of LEDs
    if value > 1.0:
        print("Made it to 1")
        explorerhat.output.one.on()
    if value > 2.0:
        print("Made it to 2")
        explorerhat.output.two.on()
    if value > 4.0: # Why 4? Test variations and see
        print("Made it to 3")
        explorerhat.output.three.on()

# Attach an event handler.
# This is a different way of making stuff happen in Python to what you've done before.
# Can you describe the difference?
explorerhat.analog.one.changed(handle_analog)

# Can you work out what this does?
# (Hint: we don't know ourselves, but it's in the example code)
signal.pause()
