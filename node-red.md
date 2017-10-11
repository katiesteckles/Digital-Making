# Node-RED and the Information Superhighway

## Node_RED in brief

Node-RED is a visual tool for gluing together the Internet of Things (IoT). It provides *some* simplicity when wiring up different web-enabled technologies and software.

Want your Twitter feed to control your bedroom lamp? Or your FitBit to switch off the power to your fridge when you've not done enough steps? Or to enable audience members to particpate in live data collection in one of your activities? Node-RED is a tool (not the only tool) that can hep you achieve your wildest IoT dreams.

## Accessing Node-Red

General Node-RED guidance is to fresh install the latest version onto your Pi, rather than just using the version included with Raspbian. Head to your terminal and enter:
`bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)`

You can make Node-RED start at boot (when you switch the Pi on) by typing:
`sudo systemctl enable nodered.service`

Now head to your Pi's web browser and navigate to localhost:1880 and marvel at the beauty of the graphical interface.

## Creating your first flow

Node-RED uses the term **flows** to describe a set of inputs and outputs linked by wires. Usually, you'll get a **flow** to perform a series of functions that make up your project (your web-enable rainbow machine for example).

On the left of the screen, you'll see your **palette** which contains all your input, output and function Nodes organised by type. Your **workspace** is in the centre of the screen, you'll drag nodes here to create flows. And finally, on the right, you'll find your **info panel**, from here you can **deploy** new flows, find out **info** about the nodes you are using and **debug** your flows to check where they are going wrong (that won't happen - promise).

### Inputs, outputs and debugging

Enough talk! Let's make our first flow.

Two really useful nodes are **inject** and **debug**, you can find them in your **palette** (on the left). **inject** can be found under inputs and **debug** under outputs.  Drag them onto the **workspace**.

Connect the two nodes by clicking and dragging a wire from the dot on the **inject** node to the dot on the **debug** node. You'll notice the nodes have a little blue dot on them, this means they have yet to be deployed. Press the **deploy** button above the info panel and *voila!* - nothing happens.

Your flow has been deployed, but it doesn't do very much. In the info area, make sure that the **debug** tab is selected. Now press the little button to the left of your **inject** node and *voila!* - something happens. A number appears - to be more specific, the number of milliseconds that have passed since January 1st 1970 is displayed.

Your **inject** node can be used to send other things through your flow, if you double click the node you can choose a variety of different **payloads**. Try doing the same thing but send a string or number (some text) instead. Remember to press **deploy** before you try to inject your new string.

## Activity 1: Controlling NeoPixels 

Time for an upgrade - **inject** and **debug** nodes will be really useful when designing your flows, but alone they aren't overly exciting. In this activity, we'll create a simple user interafce that controls the colour of a LED.

To run this flow you'll need a few nodes that don't come with the basic install. We've installed them for you, but if your doing this tutorial after the event, you can install them easliy through the hamburger menu in Node-RED (top right), click it and then click **Manage Palettes**. Click the **install** tab and search for `node-red-node-pi-neopixel` and for `node-red-dashboard` then install. New Nodes will show up in the **palette** - if they don't a restart might be needed. To get the NeoPixels working you'll also need to install some drivers outside of Node-RED. Head to a terminal window and type `curl -sS get.pimoroni.com/unicornhat | bash`.

Brill - we're ready. Three steps and you'll have a beautiful little light you can control with a colour picker.

1. Wire up a neopixel

Connect the -VE wire to a GND pin on the Pi, connect the DATA wire to GPIO 18 and finally the +VE wire to a 5V output - [this diagram](https://i.pinimg.com/originals/84/46/ec/8446eca5728ebbfa85882e8e16af8507.png) might help.

2. Set up your input

Drag the **color picker** node from the palette, it's under the heading **dashboard** and place it on your workspace. The node needs a little setup before it will dance in the way we want it to. Double click the node to open its properties.
We need to create a place for the color picker to sit, so cick the pencil to the right of the **group** section, then do the same for the **tab** section. This will populate boxes with **default** settings. Click **update** and then **update** again. Back in the **color picker** isettings box, change the size to 6x6, and check the box for **always show picker**. Click **done** then **deploy** the flow.
Open a new browser windown and navigate to the User Interface (UI) **localhost:1880/ui** you'll see your colour picker - woop!

3. Add the beautiful colour

Drag a **neopixel** node onto the workspace. It needs minimal setup, just double click and set the number of pixels to the number of LEDs you have (1). Now connect the two nodes and **deploy**. Head to the UI and move the colour picker and marvel at the pretty colours.

## Activity 2: A better use for Twitter

So far so good. Now lets connect to the world via the wonder that is the Internet. Node-RED offer multiple ways to connect to online data soucres, we're going to use Twitter, but you could set it up with your email, or a weather app, your FitBit, Alexa or a news feed.

Drag the **twitter** input node from the **social** area of the **palette** (sounds like there's a fight about to start in a digital nightclub). The input node has the connecting dot on the right hand side (the other twitter node is an output).  We're going to make this node search for the #colourchange and then extract the name of a colour from the tweet to send to the neopixel. The tweet will be in this format: *#colourchange blue*.

Double click the **twitter** node on your workspace. Click the pencil to the right of the **TwitterID** section and then click to authenticate. This will take you to twitter where you can input some details to allow node-RED to search and post on your behalf. Back in Node-RED, click add. Now you need to add a term which Node-RED will search for - we'll use #changecolour.

Connect the **debug** node to the **twitter** node and then **deploy** - we want to see what the output from twitter is so that we can make it a successful input to the **neopixel**. Send a tweet in this format: #changecolour blue and watch the debug output.

The **neopixel** node can take inputs of colour names (if they are on [this list](https://html-color-codes.info/color-names/)), RGB values separated by commas or HEX values (that's what it's getting from the colour picker). The output from the **twitter** node currently looks like this *#colourchange red* - we'll need to remove the hastag and the trailing space to make it work.

Time for a new node, one that changes the content of the message payload sent between nodes. Grab the **change** node from the **palette**. Hook it up between the **twitter** node and the **debug**. Double click the **change** node and set the **Rules**  to **change** we're going to remove *"#changecolour "* (including the trailing space) and put nothing in its place. **Deploy** and test this new code by sending another tweet. With any luck, your debug output will now show just a colour name.

Finally, hook the **change** node to the **neopixel** node and **deploy** - well done you have you first web-enabled multicolour LED - high fives all round.

## Going further

Rather than a Neopixel, I thought it might be fun to try wiring up a servo instead and creating something that points or moves in response to a tweet. To do this read the **info** tabe for an output node called **rpi gpio**, the servo will need hooking up to GPIO 2 and setting as Type PWM - play with some different input values from 1-20 to work our what gives you the best movement. You'll need to think about the type of input you want from Twitter (the hastag and the instructions). To make decisions based upon an input you'll also need the **switch** node.

With this kind of power, you can build an IoT device that pets your hamster whilst your on holiday in South Africa?