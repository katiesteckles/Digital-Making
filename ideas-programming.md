# Ideas – Programming

If we've demonstrated one thing in the last few years, it's that you don't need to be a great programmer to develop and deliver some terrific digital making activities and installations. For the most part, you can learn as you go along and pick up ideas when you need them. Purists will wince at some of what you do, but if what you do works... are they right to worry?

Sometimes, yes they are. And we continually revisit old projects to improve them, and laugh at some of the things we thought were smart a few months ago.

The following is -- for the moment -- a bare list of programming concepts and keywords which we think are useful. They're in no particular order, and we're not referring to specific languages here. The concepts are shared across most of the languages and platforms you're likely to encounter, even if the way of expressing them varies tremendously. One of the most useful things to learn is that once you know what a particular concept is *called*, you can usually google it and find out how to use it.

We'll fill in notes and particularly useful links as we come across them (or you're welcome to add your own!), but the real lesson here is to use the headings as key words in a web search.

## Loops
In the skills day, the first loop you encountered was in the initial Python:

    while True:

...and the code within that block executed over and over and over, because the `True` test never failed.

In the Micro:Bit section, the `forever` block does much the same thing.

You might also have come across situations where you wrote some logical test on every pass through the loop, letting your code assess whether to go around one more time or skip on to the next block.

One thing to watch for: when does the loop test run? Before the code within the loop executes, or after it? Some loop structures always run at least once, while some can exit before they ever run. Not quite wrapping your head around this is a common source of bugs early on.

### Iterators
We probably didn't get to these in the Skills Day, but they're a key concept in Python (and several other languages). Worth googling.

## Variables

### Variable types

## Conditionals: `if... then... else`

## Function calls & object methods
Computer scientists will probably wince at grouping these two together, but if you're writing little bits of code to glue a few things together the deep distinction doesn't really matter that much. At some point, as you continue your explorations, you'll start to notice that the code you're borrowing from other people looks a lot neater than yours, and it's extending the language you're using in neat ways that don't seem accessible to you.

At that point, start reading up on *object orientation* in whichever programming language you've settled on. It'll blow your mind, but also simplify a lot of the stuff you've been doing for ages already.

## Data structures
We won't have got into this much in the skills day, but as you get more advanced a key concept becomes: how do the variables you're setting up group together and model the problem your code is trying to address? So, and LED might have a brightness and a colour, and keeping track of those two things is straightforward enough. But what sort of variable is 'colour'? Is it a triplet of red, green and blue values? Or maybe a hue, saturation, lightness trio?

Now what if you're working with a grid of hundreds of LEDs, each of which could have a brightness and a colour value? You *could* set up individual variables for each quantity, but that's going to be massively tedious. 'This is tedious' is the sort of phrase that should transform in your head into 'There has to be a better way of doing this'. That's when you start googling.

### Arrays, lists, tuples, and all that jazz

### Key:Value pairs, dictionaries

### Complex structures
