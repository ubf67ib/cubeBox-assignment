import rhinoscriptsynax as rs
from boxmaker import *

#TODO: Make this user inputted
lines = [[0.3, 0.6], [0.4, 0.8], [0.2, 0.7]]
x, y, z = 0, 0, 0

for i in lines[0]:
    makebox(x+i*9-3/32, y, z, 3/16, 9, 9)
for i in lines[1]:
    makebox(x, y+i*9-3/32, z, 9, 3/16, 9)
for i in lines[2]:
    makebox(x, y, z+i*9-3/32, 9, 9, 3/16)