"""
Demonstrates:
  -- LOOPS (doing something repeatedly) and
  -- using OBJECTS
via Turtle Graphics.

Concepts include:
 * Using OBJECTS:
   -- CONSTRUCT an INSTANCE of a CLASS (we call such instances OBJECTS).
   -- Make an object  ** DO **  something by using a METHOD.
   -- Reference an object's  ** DATA **  by using an INSTANCE VARIABLE.

 * LOOPS:
   -- Using a FOR expresssion like this:
         for k in range(41):
             blah
             blah
             blah

     The above repeats the body of the FOR expression 41 times.
     The name  k  is:
            0 the first time the body runs,
       then 1 the next time the body runs,
       then 2 the next time the body runs,
         etc
       then 40 the last time the body runs.

 * ASSIGNMENT and NAMES
  -- ASSIGNING a VALUE to a NAME (aka VARIABLE), as in these examples:
        jack = 45
        jill = 'ran down the hill'
        size = size - 12

 * The DOT trick: Type expressions like the following,
     pausing after typing the DOT (period, full stop).
     The window that pops up give lots of clues for what you can do!
        rg.
        rg.SimpleTurtle().
        rg.Pen().
        rg.PaintBucket().

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         and their colleagues.
"""
import rosegraphics as rg

window = rg.TurtleWindow()

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('midnight blue', 3)
blue_turtle.speed = 20  # Fast

# The first square will be 300 x 300 pixels:
size = 200
red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red', 3)

red_turtle.speed = 20
size = 200
red_turtle.left(180)
# Do the indented code 13 times.  Each time draws a square.
for k in range(13):

    # Put the pen down, then draw a square of the given size:
    size = size - 12
    blue_turtle.draw_circle(size)
    blue_turtle.pen_up()
    blue_turtle.forward(10)
    blue_turtle.pen_down()
    size = size - 10


    size = size - 12
    red_turtle.draw_circle(size)
    red_turtle.pen_up()

    red_turtle.forward(10)
    red_turtle.pen_down()
    size = size - 10

window.close_on_mouse_click()
