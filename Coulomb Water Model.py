from __future__ import division

from visual import *
from visual.graph import * # import graphing features

O=Oxygen=sphere(pos=vector(0,0,0),radius=10*.66e-11, color=color.red)
H1=Hydrogen1=sphere(pos=vector(95.564e-12,7.2661e-12,0),radius=10*.31e-11)
H2=Hydrogen2=sphere(pos=vector(-95.564e-12,7.2661e-12,0),radius=10*.31e-11)

#With a Kick
#H1=Hydrogen1=sphere(pos=vector(90e-12,7e-12,0),radius=10*.31e-11)   
#H2=Hydrogen2=sphere(pos=vector(-90e-12,7e-12,0),radius=10*.31e-11)

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

#Force modeled electrostatically
#Fe=K*qO*qH/(H.pos-O.pos)^2
ke=8.987551e+9				#Coulomb's Constant
t=0
dt=1.15e-38

while t<5e-12:
    t=t+dt    
    FOH1=((ke*qO*qH)/(mag(H1.pos-O.pos))**2)*-norm(H1.pos-O.pos)	#Force of Oxygen on Hydrogen1
    FOH2=((ke*qO*qH)/(mag(H1.pos-O.pos))**2)*-norm(H2.pos-O.pos)
    FH1O=((ke*qO*qH)/(mag(O.pos-H1.pos))**2)*-norm(O.pos-H1.pos) #=-FOH1
    FH2O=-((ke*qO*qH)/(mag(O.pos-H2.pos))**2)*norm(O.pos-H2.pos)
    FH1H2=-((ke*qH*qH)/(mag(H2.pos-H1.pos))**2)*norm(H2.pos-H1.pos)
    FH2H1=-((ke*qH*qH)/(mag(H1.pos-H2.pos))**2)*norm(H1.pos-H2.pos)
	 
    H1.pos=H1.pos+((pH1)/mH)*dt
    H2.pos=H2.pos+((pH2)/mH)*dt
    O.pos=O.pos+((pO)/mO)*dt
    pH1=pH1+(FOH1+FH2H1)*dt
    pH2=pH2+(FOH2+FH1H2)*dt
    pO=pO+(FH1O+FH2O)*dt

    graph1.plot(pos=(t,mag(H1.pos-O.pos)-95.84e-12))
