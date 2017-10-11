# Digital Making -- key concepts and technologies

For the most part, you can plug bits of electronics together without much worry, and for most of the things you're likely to do you won't need to use very many components or worry about suppressing signals or whatever -- most of the tricky bits are taken care of by the boards we use. At NUSTEM, we go out of our way to *avoid* doing much in the way of electronics, and so far we've not found ourselves terribly limited by taking that view.

There are, however, a few basic circuits and ideas which you can combine to make other things.

## Not blowing things up

At some stage, you're going to fry something. In digital making circles this is known as 'letting the blue smoke out', for reasons that become obvious. Things that are worth knowing:

### Shorting batteries
It's *extremely* easy to let the two wires of a battery pack touch each other. Batteries will become very hot really quite quickly, the packs will start melting, there may be a bit of smoke, and so on. It's quite alarming, and should certainly go on your risk assessment.

Control measures might include:
* Solder header pins to the battery pack wires.
* Use alkaline rather than rechargeable batteries, as they're much less likely to explode if shorted. Alkaline cells are less sustainable, but inherently safer.

### 5V and 3.3V
In the good old days, electronics standardised around 5V circuits. Which was great and all, but then people found they could make smaller and more efficient microprocessors based around a 3.3V standard instead.

Arduinos tend to use 5V; Micro:Bit and Raspberry Pi are 3.3V devices. Most of the time this doesn't matter too much, but:

* Try not to push 5V into 3.3V device. It may not like it (see above re: letting the blue smoke out)
* For situations where it actually does matter, you can get *logic level convertors* which will translate your signals between 5 and 3.3V. Google them.

### Protected vs. unprotected inputs
One of the reasons Arduinos were (and are) popular in installation art and maker circules is that the standard boards have massive resistors on their inputs. Which makes it really hard to accidentally fry the board by shoving 5V where it doesn't belong. That's called a *protected input*.

Unfortunately, protected inputs are expensive to make, which is why part of why an Arduino has a tiny fraction of the processing power of a Raspberry Pi but costs about the same. Neither Pis nor Micro:Bits have protected inputs.

The [Explorer HAT Pro](https://shop.pimoroni.com/products/explorer-hat) boards we use with our Pis *do* offer protected inputs.

## LEDs

### NeoPixels and other RGB LEDs

## Servo motors

## Motors

### Stepper motors

## Analogue vs Digital inputs

### Buttons

### Sensors

#### Measuring voltage to measure everything else

Boards which have anlogue inputs (Arduinos, which we've not talked about much in this course; Micro:Bit; the [Exporer HAT](https://shop.pimoroni.com/products/explorer-hat) for Raspberry Pi) measure *voltage*. Which is fine and all, but you're more likely to want to detect rotation angle, or force, or whatever.

In practice, you use a voltage divider circuit: your sensor (whatever it may be) behaves like a variable resistor, and you wire it between 3.3V and ground rails in series with another resistor of known value. You then connect the mid-point of the two resistors to the analogue input of your board, and measure the voltage at that input.

That's a terrible explanation which badly needs a diagram.

#### Resistors

At some point, you're going to need to know the resistance value of a tiny thing with coloured stripes on it. Here's the best way:

* [Resistor colour code](http://resistor.cherryjourney.pt)

## Sound

## Displays
