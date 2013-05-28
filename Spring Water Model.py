#Tweaked for visuals
from __future__ import division

from visual import *
from visual.graph import * # import graphing features

O=Oxygen=sphere(pos=vector(0,0,0),radius=10*.66e-11, color=color.red)
#H1=Hydrogen1=sphere(pos=vector(95.564e-12,7.2661e-12,0),radius=10*.31e-11)
#H2=Hydrogen2=sphere(pos=vector(-95.564e-12,7.2661e-12,0),radius=10*.31e-11)

#With a Kick
H1=Hydrogen1=sphere(pos=vector(90e-12,7e-12,0),radius=10*.31e-11)   
H2=Hydrogen2=sphere(pos=vector(-90e-12,7e-12,0),radius=10*.31e-11) 

mO=15.99/(6.022e26)
mH=1.0079/(6.022e26)


#Given from experimentation
k=50
upp=5e-5

pO=mO*vector(0, 0, 0)
pH1=mH*vector(0, 0, 0)
pH2=mH*vector(0, 0, 0)

graph1 = gcurve(color=color.white)


#Force Modeled by a spring

t=0
dt=15e-18

while t<5e-11:
    t=t+dt
    Fl1=-k*(mag(H1.pos-O.pos)-95.84e-12)*norm(H1.pos-O.pos)
    Fl2=-k*(mag(H2.pos-O.pos)-95.84e-12)*norm(H2.pos-O.pos)
    Fa=upp*(mag(H1.pos-H2.pos)-191.128e-12)*norm(H1.pos-H2.pos)

    H1.pos=H1.pos+((pH1)/mH)*dt
    H2.pos=H2.pos+((pH2)/mH)*dt

    pH1=pH1+(Fl1-Fa)*dt
    pH2=pH2+(Fl2+Fa)*dt

    graph1.plot(pos=(t,mag(H1.pos-O.pos)-95.84e-12))
