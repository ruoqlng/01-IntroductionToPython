"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and ruoqing.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

will = rg.SimpleTurtle('turtle')
will.pen = rg.Pen('aqua', 1)
will.speed = 50


size = 200
becca = rg.SimpleTurtle('turtle')
becca.pen = rg.Pen('pink', 1 )
becca.speed = 50

for k in range(9):

    size = size - 12
    will.draw_square(size)
    will.pen_up()
    will.forward(10)
    will.pen_down()
    size = size - 10

    size = size - 12
    becca.draw_square(size)
    becca.pen_up()

    becca.forward(10)
    becca.pen_down()
    size = size - 10

window.close_on_mouse_click()