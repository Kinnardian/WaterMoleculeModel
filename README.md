WaterMoleculeModel
==================

This is a collection of three different models of a water molecule in Python.

Models of Molecular Motions
=====
Of all the fundamental forces governing our world, those that govern intramolecular and intermolecular interaction are perhaps the most pervasive. They appear as the force of magnets, and the electronics which depend on them, but also as the magnetosphere of the Earth and the beautiful aurora it produces. They apars as the forces that governs chemical interactions. All of these forces are actually all incarnations of the electrostatic force. Curiously, it is the force which governs springs on the macroscopic level and chemical bonds on the nanoscopic level. This curious coincidence of physical phenomena is one of great consequence for it allows us to simply yet elegantly describe the mechanics of molecules and glean much other understanding from the Universe. In this paper I will model interparticle interactions using three different but related vPython set-ups. 

Models
====
In the interest of computational parsimony, the elegance of the model, and my own sanity several assumptions have been made. Some will be shed as we progress through the models. Atoms are treated as massive, sometimes charged point particles represented by spheres. This contrasts with the currently understood reality explained by quantum physics, not only in complexity but also in computability. Bonds are modeled variously using springs, the coulumb force, and the Lennard-Jones Potential.
I chose to model water because of its simplicity, its pervasiveness, and it centrality to human experience and also because of its role as a solvent in easily(or so I thought) modeled ionic interactions. 
Hooke Model
===
My water model is composed of three particles, one oxygen and two hydrogens and three springs. The hydrogens are attached to the oxygens by springs with 95.84pm as the equilibrium length, as this is the equilibrium length of the O-H bond in water.  There is a third imaginary spring, which does not represent a bond running from Hydrogen to Hydrogen. This spring, I believe, accounts for the lone pairs on oxygen which give water its bond angle, but which would not appear in a model treating atoms as point particles. 
The force of each spring is given by a Hook’s Law: . The spring constants of the springs were derived from their respective angular frequencies of oscillation, which were available from experimentation and from this semesters lecture notes, using the relation .  This model allows for intramolecular behavior such as bond length and angle oscillation to be understood but it does not account for intermolecular interactions.

Coulumb Model
==
In order to model interatomic interactions, the particles of water were given partial charges which sum to 0 (arbitrarily, δO=-.8, δH=+.4) and the force due to these charges was modeled using Coulumb’s Law:  rather than springs. This model accounts for attractive forces between differently charged particles, and repulsive forces between similarly charged particles but it does not account for restoring forces in each case.
In order to account for both the attractive and repulsive forces between particles, I extended my model to include forces of temporary intratomic shifts in charge distribution know as dipole moments known as Van der Waals forces using the Lennard Jones Potential:. This model was developed by John Lennard-Jones in the 1920’s at Cambridge. It is widely used because of its analytical and computational simplicity. 


Results
===
The spring model starts off fine except that if run long enough, the oscillations of the O-H bond length grow and do so in such a way that indicates my spring water model is inaccurate as a model for nature. This may be a product of cumulative rounding error rather than modeling error and can be corrected for by using a smaller time step.
Graph of O-H bond length in Hook Model oscillating out of control.
The Coulomb model seems to pull in the hydrogens, as if in a pinball machine only for them to be shot away. This makes sense because of the absence of a restorative force. 

Falling in . . .
  Flying away!
===

The final model, using the Lennard-Jones Potential seems to be the best, as it displays neither the instability of the Coulumb model or the eventual decay of the spring model. I had hoped to also include a model involving an ionic interaction but this hope was snuffed out by the pernicious n-body problem.
