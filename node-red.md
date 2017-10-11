# Node-RED and the Information Superhighway
## What is Node-Red?
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
On the lef tof the screen you'll see your __palette__ which contains all your input, output and function Nodes organised by type. Your __workspace__ is in the centre of the screen, you'll drags nodes here to create flows. And finally on the right, you'll find you __Info panel__, from here you can __deploy__ new flows, find out __info__ about the nodes you are using and __debug__ your flows to check where they are going wrong (that won't happen - promise).  
### Inputs, Outputs and Debugging  
Enough talk! Let's make our first flow.  

Two really useful nodes are __inject__ and __debug__, you can find them in your __palette__ (on the left). inject can be found under inputs and debug under outputs.  Drag them onto the __workspace__.  

Connect the two nodes by clicking and dragging a wire from the dot on the __inject node__ to the dot on the __debug node__. You'll notice the nodes have a little blue dot on them, this means they have yet to be __deployed__. Press the __deplo__ button above the info panel and _voila!_ - nothing happens.  

Your flow hasbeen deployed, but it doesn't do very much. In the info area, make sure that the __debug__ tab is selected. Now press the little button to the left of your inject node and _voila!_ - something happens. A number appears, to be more specific the number of milliseconds that have passed since January 1st 1970 is displayed.  

Your inject node can be used to send other things through your flow, if you double click the node you can choose a variety of different __payloads__. Try doing the same thing but send a string (some text) instead. Remember to press deploy before you try to inject your new string.  

## Activity 1: Controlling NeoPixels
## Actviity 2: A better use for Twitter
