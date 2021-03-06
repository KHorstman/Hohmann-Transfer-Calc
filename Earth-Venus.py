import math
import time
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.widgets

#Parameters (Constants)
re = 1.496E8                                    #Earth Orbit Radius
rm = 108.2E6                                    #Mars Orbit Raduis
Tm = 19414080
Te = 31558118.4

#Parameters (Calculated)
M = rm +re                                     #Major Axis
a = M/2                                        #Semi-Major Axis 
mus = 132712000000                             #Mu Sun
eplison = -(mus/(M))                           #Energy of ellipse

e = abs(((re-rm)/M))                           #Orbit eccentricity

h = math.sqrt((rm * mus) * (1 + e))            #Angular Momentum

vp = h/re
va = h/rm

#Transfer Orbit Time
T = ((2*math.pi)/math.sqrt(mus) * a ** (3/2))
Tt = T / 60 / 60 /24 / 2
alpha = 180 * (-1 + T/Tm)
print(Tt)

fig = plt.figure()
#Plot 1
plt.subplot(1,2,1)
EarthOrbit = plt.Circle((0,0), re, color = 'b', fill = False, linestyle = '--')
MarsOrbit = plt.Circle((0,0), rm, color = 'g', fill = False, linestyle = '--')

ax1 = plt.gca()
ax1.cla()
ax1.axis("equal")
ax1.set_xlim((-5E8, 5E8))
ax1.set_ylim((-5E8, 5E8))

ax1.add_artist(EarthOrbit)
ax1.add_artist(MarsOrbit)
ax1.plot((-re),(0), 'ro', color = 'blue')

marsx = rm * math.cos(alpha)
marsy = rm * math.sin(alpha)

ax1.plot((marsx), (marsy), 'ro', color = 'g')

exv = [0,-re]
eyv = [0,0]

mxv = [0, marsx]
myv = [0, marsy]
ax1.plot(exv,eyv,linewidth=1, color = 'blue')
ax1.plot(mxv,myv,linewidth=1, color = 'green')
ax1.plot((0),(0), 'ro', color = 'orange')
plt.title("Departure Seperation Angle (~%(alpha)d degrees)" %{'alpha':alpha}, fontsize = 14)
plt.xlabel("Distance (km)")
plt.ylabel("Distance (km)")
plt.legend([EarthOrbit, MarsOrbit], ["Earth Orbit", "Venus Orbit"], loc = 2)


##Plot 2##
plt.subplot(1,2,2)
EarthOrbit = plt.Circle((0,0), re, color = 'b', fill = False, linestyle = '--')
MarsOrbit = plt.Circle((0,0), rm, color = 'g', fill = False, linestyle = '--')

ax2 = plt.gca()
ax2.cla()
ax2.axis("equal")
ax2.set_xlim((-5E8, 5E8))
ax2.set_ylim((-5E8, 5E8))

ax2.add_artist(EarthOrbit)
ax2.add_artist(MarsOrbit)
ax2.plot((-re),(0), 'ro', color = 'blue')

ax2.plot((rm), (0), 'ro', color = 'g')

exv = [0,-re]
eyv = [0,0]

mxv = [0, rm]
myv = [0, 0]
ax2.plot(exv,eyv,linewidth=1, color = 'blue')
ax2.plot(mxv,myv,linewidth=1, color = 'g')
ax2.plot((0),(0), 'ro', color = 'orange')
plt.title("Hohmann transfer Orbit", fontsize = 14)
plt.xlabel("Distance (km)")
plt.ylabel("Distance (km)")

#Ellipese for Plot 2
b = h**2 /mus

c = math.sqrt(((M/2)**2) - (b**2))

TransferOrbit = matplotlib.patches.Arc((-c+10000000,0),M,2*b, theta1 = 0, theta2 = 180, fill = False)
plt.legend([EarthOrbit, MarsOrbit, TransferOrbit], ["Earth Orbit", "Venus Orbit","Transfer Orbit"], loc = 2)
ax2.add_patch(TransferOrbit)
#Stuff at the bottom of the plot
def signaturebar(fig,text,fontsize=10,pad=5,xpos=20,ypos=5,
                 rect_kw = {"facecolor":"grey", "edgecolor":None},
                 text_kw = {"color":"w"}):
    w,h = fig.get_size_inches()
    height = ((fontsize+4*pad)/72.)/h
    rect = plt.Rectangle((0,0),1,height, transform=fig.transFigure, clip_on=False,**rect_kw)
    fig.axes[0].add_patch(rect)
    fig.text(xpos/72./h, ypos/72./h, text,fontsize=fontsize,**text_kw)
    fig.subplots_adjust(bottom=fig.subplotpars.bottom+height)

signaturebar(fig,"The transfer velocity required at Earth is %(vp)d km/s. \n" %{"vp" : vp} + "The transfer velocity required at Venus is %(va)d km/s. \n" %{"va" : va} + "The time required to intercept Venus is %(Tt)d days." %{"Tt": Tt})
#plt.savefig('foo.png', bbox_inches='tight')
plt.show()