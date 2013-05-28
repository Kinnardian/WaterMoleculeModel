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
qO=.8
qH=.4
qNa=1
qCl=-1

pO=mO*vector(0, 0, 0)
pH1=mH*vector(0, 0, 0)
pH2=mH*vector(0, 0, 0)

graph1 = gcurve(color=color.white)

#Force modeled using Lennard-Jones potential
#F=-12Ar^-13+6Br^-7
A=1
B=2
t=0
dt=1e-18

while t<5e-12:
    t=t+dt    
    FOH1=(-1)*(-12*A*(mag(H1.pos-O.pos)**13)+6*B*(mag(H1.pos-O.pos))**(-7))*norm(H1.pos-O.pos)	#Force of Oxygen on Hydrogen1
    FOH2=-1*(-12*A*(mag(H2.pos-O.pos)**13)+6*B*(mag(H2.pos-O.pos))**(-7))*norm(H2.pos-O.pos)
    FH1O=-1*(-12*A*(mag(O.pos-H1.pos)**13)+6*B*(mag(O.pos-H1.pos))**(-7))*norm(O.pos-H1.pos)
    FH2O=-1*(-12*A*(mag(O.pos-H2.pos)**13)+6*B*(mag(O.pos-H2.pos))**(-7))*norm(O.pos-H2.pos)
    FH1H2=-1*(-12*A*(mag(H2.pos-H1.pos)**13)+6*B*(mag(H2.pos-H1.pos))**(-7))*norm(H2.pos-H1.pos)
    FH2H1=-1*(-12*A*(mag(H1.pos-H2.pos)**13)+6*B*(mag(H1.pos-H2.pos))**(-7))*norm(H1.pos-H2.pos)
	
    H1.pos=H1.pos+((pH1)/mH)*dt
    H2.pos=H2.pos+((pH2)/mH)*dt
    pH1=pH1+(FOH1+FH2H1)*dt
    pH2=pH2+(FOH2+FH1H2)*dt
    pO=pO+(FH1O+FH2O)*dt
    graph1.plot(pos=(t,mag(H1.pos-O.pos)-95.84e-12))
