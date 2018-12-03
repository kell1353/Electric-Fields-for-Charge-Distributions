
"""import sys"""
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

c = input("Charges multiplier?: ")
#d= input("Charges multiplier?: ")
#k =  4*np.pi*(8.854**(-12))

Modulo = input("\nWhich modulo do you want to run? (1, 2, 3, or 4):  ")

def E(q, r0, x, y):
    """Return the electric field vector E=(Ex,Ey) due to charge q at r0."""
    den = np.hypot(x-r0[0], y-r0[1])**3
    return q * (x - r0[0]) / den, q * (y - r0[1]) / den


"""Grid of x, y points"""
nx, ny = 64, 64
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)


"""Grid of x, y points for less detailed wider view"""
##nx, ny = 256, 256
##x = np.linspace(-4, 4, nx)
##y = np.linspace(-4, 4, ny)
##X, Y = np.meshgrid(x, y)


"""Create a multipole with nq charges of alternating signs, positive signs ,or negative signs, equally spaced"""
# nq = 2**int(sys.argv[2])
nQ = 2**int(0)
nq = 2**int(c)
charges = []
for i in range(nq):
    Aq = i%2 * 2 - 1                                                                                                                                    # atlernating charges
    #Pq =  i % 2 * 2 + 1                                                                                                                            # only positive charges
    Pq =  1  
    #Nq = -(i % 2 * 2  + 1)                                                                                                                     # only negative charges
    Nq = -1
    
    """ Create a multipole with nq charges of alternating sign, equally spaced"""       """Modulo 1"""
    """ on the unit circle. ORIGINAL"""

    """ A  small ring of charges above a line of charges"""       """Modulo 2"""

    """ Two vertical parallel lines with opposite charges"""       """Modulo 3"""

    """ Creates a horizontal plate and a single point charge above it"""        """Modulo 4"""
    
    if Modulo == '1':
        charges.append((Aq, (np.cos(2*np.pi*i/nq), np.sin(2*np.pi*i/nq))))                          # on the unit circle
    
    #charges.append((q, (np.cos(2*np.pi*i/nq), 2*np.sin(2*np.pi*i/nq))))                          # on an ellipse 

    elif Modulo == '2':
        charges.append((Nq, (np.cos(2*np.pi*i/nq), np.sin(0*np.pi*i/nq)-1.6)))                      # on a line on the x-axis
        charges.append((Pq, (.6*np.cos(2*np.pi*i/nq), .6*np.sin(2*np.pi*i/nq)+1)))              # .6* a unit circle  center at (0,1)


    elif Modulo == '3':
        charges.append((Nq, (np.cos(0*np.pi*i/nq)-2, np.sin(2*np.pi*i/nq))))                        #  vertical line on x = -1
        charges.append((Pq, (np.cos(0*np.pi*i/nq), np.sin(2*np.pi*i/nq))))                             # vertical line on x = 1


    elif Modulo == '4':
        charges.append((Nq, (np.cos(2*np.pi*i/nQ)-1, np.sin(2*np.pi*i/nQ)+.6)))                 # a single point charge at (0, .6)
        charges.append((Pq, (np.cos(2*np.pi*i/nq), np.sin(0*np.pi*i/nq-1))))                         # a horizontal line at y = -2


    elif Modulo == '5':
        charges.append((Pq, 1/nq, 2/nq))

    else:
        print("\nThis modulo doesn't exist")


"""Use below  if you want to add a new set of points with a different charge  multiplier"""
"""If you just want a single point set d = 0"""

##nQ = 2**int(d)                                                                                                                                
##for i in range(nQ):
##    q= (i%2*2+1)
##    charges.append((q, (np.cos(2*np.pi*i/nQ), np.sin(2*np.pi*i/nQ)+1.5)))

                   
"""Electric field vector, E=(Ex, Ey), as separate components"""
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
for charge in charges:
    ex, ey = E(*charge, x=X, y=Y)
    Ex += ex
    Ey += ey

fig = plt.figure()
ax = fig.add_subplot(111)

"""Plot the streamlines with an appropriate colormap and arrow style"""
color = 2 * np.log(np.hypot(Ex, Ey))
ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2.5, arrowstyle='->', arrowsize=1.0)

"""Add filled circles for the charges themselves"""
charge_colors = {True: '#aa0000', False: '#0000aa'}
for q, pos in charges:
    ax.add_artist(Circle(pos, 0.035, color=charge_colors[q>0]))

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_aspect('equal')
plt.show()




