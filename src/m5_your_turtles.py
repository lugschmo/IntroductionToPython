"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Mitch Lugsch.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

pink_turtle = rg.SimpleTurtle('turtle')
pink_turtle.pen = rg.Pen('pink', 3)
pink_turtle.speed = 16  # Fast

length = 100

for k in range(19):

    # moving with the pen down
    pink_turtle.forward(length)
    pink_turtle.left(45)
    pink_turtle.forward(length)
    pink_turtle.left(45)
    pink_turtle.forward(length)
    pink_turtle.left(45)

    length = length - 5

orange_turtle = rg.SimpleTurtle('turtle')
orange_turtle.pen = rg.Pen('orange', 5)
orange_turtle.speed = 15  # Fast
orange_turtle.pen_up()
orange_turtle.backward(200)
orange_turtle.left(90)

distance = 235
distance2 = 10

for k in range(20):

    orange_turtle.forward(distance)
    orange_turtle.pen_up()
    orange_turtle.left(90)
    orange_turtle.forward(distance2)
    orange_turtle.left(90)
    orange_turtle.pen_down()

    distance2 = distance2 + 10

window.close_on_mouse_click()