"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Aaryan Khatri
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
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
#
########################################################################
import rosegraphics as rg
window=rg.TurtleWindow()

aaryan = rg.SimpleTurtle('arrow')
aaryan.pen = rg.Pen('red', 10)
aaryan.speed=30

size=200

for k in range(10):
    aaryan.draw_regular_polygon(8,15)
    aaryan.backward(50)
    aaryan.forward(77)
    aaryan.left(69)
    aaryan.right(22)

alec = rg.SimpleTurtle('turtle')
alec.Pen = rg.Pen('blue', 30)
alec.speed=100

size=1000

for k in range(30):
     alec.draw_square(3)
     alec.left(33)
     alec.right(44)
     alec.forward(35)
     alec.backward(30)