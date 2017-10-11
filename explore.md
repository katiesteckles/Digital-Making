# Things to explore

## Micro:Bit and NeoPixels

A Micro:Bit running [this code](https://www.proto-pic.co.uk/user/SpookyColours.hex).

To play with this, you'll need to unfold the `Advanced` blocks in the Micro:Bit editor, then `Add Package` to add the NeoPixel library. `NeoPixel` blocks will now appear.

Google the board and you'll find [this page](https://www.proto-pic.co.uk/micropixel-4x8-ws2812b-board-for-bbc-microbit.html), which links to some resources. Most of the good stuff uses MicroPython, which is an alternative approach to writing code for Micro:Bit. You can get to the MicroPython editor by scrolling down the usual Micro:Bit page below the blocks editor you've used so far.

There are some really neat Python features to explore in here.

## Raspberry Pi & Explorer HAT Pro

The [Explorer HAT](https://shop.pimoroni.com/products/explorer-hat) is a great piece of kit, but [the documentation]() is pretty terrible. We hacked this together as a bit of a test. Turn the dial and some LEDs will light up or go out.

The code is [here](code/analogue_pi.py).

Things to note:

* Take a close look at the circuit: the Explorer HAT outputs are *weird*. That's buried in the documentation with the blurb:
> When you turn Explorer HAT/pHAT outputs on ( logic HIGH ) it will sink current to ground.
Pardon? We worked it out by replugging things more-or-less at random, and we now think we understand what they mean. Sort-of.

* The potentiometer (which is the twisty-turny dial thing) doesn't always respond in the way you might expect. Can you see what we mean?

It's worth searching for 'Explorer HAT' to find the other documentation on this board.

## Picamera and GPIOZero

Two scripts:
* [This one](code/camera_gpiozero.py) waits for a button press, then takes a picture.
* [This one](code/camera_simple.py) shows you a preview, then takes a picture.

Can you glue these two bits of code together so you get a preview, then on a button press a picture is taken?

Next step: Give me a five-second countdown using LEDs. You may want to refer back to the traffic lights example we started with.

Useful documentation:
* [GPIOZero docs](http://gpiozero.readthedocs.io/en/stable/) for all your button-handling and LED-lighting needs.
* [Picamera docs](http://picamera.readthedocs.io/en/latest/) for things camera-related.
* The [Pi Foundation GPIOZero tutorial](https://projects.raspberrypi.org/en/projects/physical-computing), though it doesn't appear to be finished.

## Picamera effects

[Start here](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera). But it's probably a good idea to use the Thonny editor you started with rather than IDLE, as suggested in the tutorial.

The 'final' code (which you might like to explore) is [something like this](code/camera_effects.py). You could try controlling it with some buttons (from the previous example) to set the desired effect?
