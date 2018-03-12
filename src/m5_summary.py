"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and ruoqing.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   Write code that constructs a SimpleTurtle with a red Pen
#   and makes it move around a bit.  Don't forget to:
#     -- import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     -- ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#      ** Nothing fancy is required. **
#      ** The NEXT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
#   As always, COMMIT-and-PUSH when you are done with this module.
#
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

size = 20
becca = rg.SimpleTurtle('turtle')
becca.pen = rg.Pen('pink', 5)


becca.speed = 200
for k in range(7):
    becca.draw_square(size)
    becca.pen_up()
    becca.right(90)
    becca.forward(50)
    becca.left(90)
    becca.pen_down()

window.close_on_mouse_click()