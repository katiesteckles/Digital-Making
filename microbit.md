# Micro:Bit

Ah, the Micro:Bit. Late to the party, troubled launch, major shifts... but nevertheless emerging as a really neat platform for doing our kind of thing. Try some of these activities and let's discuss why we think that's the case:

## Dice Rolling

Unbelievably, I couldn't find an existing worksheet which did what I wanted here -- all the existing ones are either too complex, are designed as full lesson plans for a 60-minute session, or were built using the coding environments which were first used by the Micro:Bit but have now (mostly) been ditched in favour of the JavaScript Blocks Editor.

> Key lesson: if you find resources for 'Touch Develop' -- those are old and not really usable any more.

### Roll ’em

The challenge: turn state-of-the-art microcontroller-based electronic doohickie into something marginally less functional than a set of sheep knuckle bones dating from a few thousand years ago.

That is: make dice.

There are lots of different ways of achieving this.

#### Useful hints (ie. do this first)
* Check the `Input` blocks for an `on shake` block.
* The `Math` section has a `pick random` block, but you'll need to work out what you can snap it to. Which leads to:
* `Variables`. Try `set item to to 0`, then snap the random assignment to that block.
* If you rename `item` to something like `roll`, you'll find `roll` appear as a block under `Variables`. This way you can store and retrieve bits of data your code is working with.
* The simplest thing here is to add a `show number` block. See if you can work out how to get the random number to show on the Micro:Bit.

#### After that...
* How could your die show a traditional dice face rather than a number?
* Can you extend the code to mimic a pair of dice rather than a single die? How about being able to select the number of dice using the buttons?

## Hide & Seek

Micro:Bits have radio modules embedded in them: you can find the blocks by `Add Package` then choosing 'Radio'. The Micro:Bit foundation have a fun-looking activity for turning the little dears into a radio-driven hide-and-seek game

Visit [this Micro:Bit page](https://makecode.microbit.org/projects/hot-or-cold) and see how you get on.

Note that the later stages of this worksheet get into quite clever data storage ideas.

## Knuckle whacker

One of the things Micro:Bit can do that Raspberry Pi can't is analogue inputs. That is: the Micro:Bit can measure a voltage on its inputs, rather than merely detect whether a voltage is there or not (a *digital* input).

In this example, you're going to read the value from a sensor and use that to change the angle of a small servo motor. You'll also find out what all these words mean.

* You'll be working in the `forever` block, since we want our code to keep running.
* We've pre-built the circuits to save you some time, on the handy little Micro:Bit plug-in prototyping boards. See if you can work out what all the bits do, and ask us!
* Everything you need is in the `Pins` and `Variables` section.
* Start by taking a reading from Pin 1: `analog read pin 1`. You'll need to snap that to a variable assignment block: `set item to`; change the variable name from `item` to something like `reading`.
* The analogue input gives you a value between 0 (0 Volts) and 1023 (3.3 Volts). The servo, however, needs a deflection angle in degrees, so:
* Make yourself a new variable, `set angle to`, then from `Pins` pull in a `map` block. See if you can work out how to make that do what you need.
* Finally, from `Pins` pull in a `servo write` block. The servo is on Pin 2.

When this is working, you should have a thing where the servo changes angle depending on how hard you push or how far you bend the sensor. See if you can arrange things so when you push the sensor, the servo gently nudges your hand out of the way.

We might have over-sold this as a 'knuckle whacker', though you could think about how you'd achieve that.
