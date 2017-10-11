# Node-RED and the Information Superhighway
## What is Node-Red??
Node-RED is a visual tool for gluing together the Internet of Things (IoT). It provides _some_ simplicity when wiring up different web-enabled technologies and software.

Want your Twitter feed to control your bedroom lamp? Or you FitBit to switch off the power to your fridge when you've not done enough steps? Or to enable audience members to particpate in live data collection in one of your activities? Node-RED is a tool (not the only tool) that can hep you achieve your wildest IoT dreams.

## Accessing Node-Red
General Node-RED guidance is to fresh install the latest version onto your Pi, rather than just using the version included with Raspbian. Head to your terminal and enter:
`bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)`  

You can make Node-RED start at boot (when you switch the Pi on) by typing:  
`sudo systemctl enable nodered.service`  

Now head to your Pi's web browser and navigate to localhost:1880 and marvel at the beauty of the graphical interface.  

## Creating your first flow
Node-RED uses the term __flows__ to describe a set of inputs and output linked by wires. Usually you'll get a flow to perform a series of functions that make up your project (your web-enable rainbow machine for example).  

On the left of the screen you'll see your __palette__ which contains all your input, output and function Nodes organised by type. Your __workspace__ is in the centre of the screen, you'll drags nodes here to create flows. And finally on the right, you'll find your __info panel__, from here you can __deploy__ new flows, find out __info__ about the nodes you are using and __debug__ your flows to check where they are going wrong (that won't happen - promise).  

### Inputs, Outputs and Debugging  
Enough talk! Let's make our first flow.  

Two really useful nodes are __inject__ and __debug__, you can find them in your __palette__ (on the left). inject can be found under inputs and debug under outputs.  Drag them onto the __workspace__.  

Connect the two nodes by clicking and dragging a wire from the dot on the __inject node__ to the dot on the __debug node__. You'll notice the nodes have a little blue dot on them, this means they have yet to be __deployed__. Press the __deplo__ button above the info panel and _voila!_ - nothing happens.  

Your flow hasbeen deployed, but it doesn't do very much. In the info area, make sure that the __debug__ tab is selected. Now press the little button to the left of your inject node and _voila!_ - something happens. A number appears, to be more specific the number of milliseconds that have passed since January 1st 1970 is displayed.  

Your inject node can be used to send other things through your flow, if you double click the node you can choose a variety of different __payloads__. Try doing the same thing but send a string (some text) instead. Remember to press deploy before you try to inject your new string.  

## Activity 1: Controlling NeoPixels
Time for an upgrade - inject and debug nodes will be really useful when designing your flows, but alone they aren't overly exciting. In this activity, we'll create a simple user interafce that controls the colour of a LED.  

To run this flow you'll need a few nodes that don't come with the basic install. We've installed them for you, but if your doing this tutorial after the event. You can install them easliy through the hamburger menu in Node-RED, click it and then click __Manage Palettes__. Click the __install__ tab and search for `node-red-node-pi-neopixel` and for `node-red-dashboard` then install. New Nodes will show up in the palette - if they don't a restart might be needed. To get the NeoPixels working you'll also need to install some drivers outside of Node-RED. Head to a terminal window and type `curl -sS get.pimoroni.com/unicornhat | bash`.  

Brill - we're ready. Three steps and you'll have a beautiful little light you can control with a colour picker.
1. Wire up a neopixel  
Connect the -VE wire to a GND pin on the Pi, connect the DATA wire to GPIO 18 and finally the +VE wire to a 5V output.  
2. Set up your input
Drag the __color picker__ node from the palette, it's under the heading __dashboard__ and place it on your workspace. The node needs a little setup before it will dance in the way we want it to. Double click the node to open its properties.  
We need to create a place for the color picker to sit, so cick the pencil to the right of the __group__ section, then do the same for the __tab__ section. This will populate boxes with __default__ settings. Click __update__ and then __update__ again. Back in the __color picker__ isettings box, change the size to 6x6, and check the box for __always show picker__. Click __done__ then __deploy__ the flow.  
Open a new browser windown and navigate to the User Interface (UI) __localhost:1880/ui__ you'll see your colour picker - woop! 
3. Add the beautiful colour
Drag a __neopixel__ node onto the workspace. It needs minimal setup, just double click and set the number of pixels to the number of LEDs you have (1). Now connect the two nodes and __deploy__. Head to the UI and move the colour picker and marvel at the pretty colours. 

## Activity 2: A better use for Twitter  
So far so good. Now lets connect to the world via the wonder that is the Internet. Node-RED offer multiple ways to connect to online data soucres, we're going to use Twitter, but you could set it up with your email, or a weather app, your FitBit, Alexa or a news feed.

Drag the __twitter__ input node from the __social__ area of the __palette__ (sounds like there's a fight about to start in a digital nightclub). The input node has the connecting dot on the right hand side (the other twitter node is an output).  We're going to make this node search for the #colourchange and then extract the name of a colour from the tweet to send to the neopixel. The tweet will be in this format: _#colourchange blue_.

Double click the __twitter__ node on your workspace. Click the pencil to the right of the __TwitterID__ section and then click to authenticate. This will take you to twitter where you can input some details to allow node-RED to search and post on your behalf. Back in Node-RED, click add. Now you need to add a term which Node-RED will search for - we'll use #changecolour.

Connect the __debug__ node to the __twitter__ node and then __deploy__ - we want to see what the output from twitter is so that we can make it a successful input to the __neopixel__. Send a tweet in this format: #changecolour blue and watch the debug output.

The __neopixel__ node can take inputs of colour names (if they are on [this list](https://html-color-codes.info/color-names/)), RGB values separated by commas or HEX values (that's what it's getting from the colour picker). The output from the __twitter__ node currently looks like this _#colourchange red_ - we'll need to remove the hastag and the trailing space to make it work.

Time for a new node, one that changes the content of the message payload sent between nodes. Grab the __change__ node from the **palette**. Hook it up between the **twitter** node and the **debug**. Double click the **change** node and set the **Rules**  to **change** we're going to remove *"#changecolour "* (including the trailing space) and put nothing in its place. **Deploy** and test this new code by sending another tweet. With any luck, your debug output will now show just a colour name.

Finally, hook the **change** node to the 
 


