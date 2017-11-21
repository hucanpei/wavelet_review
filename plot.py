import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

''' 
X = np.arange(0, 5, 0.1) 
Y= [1*x+1 for x in X]
Y_rand=[np.random.normal(y, 0.6) for y in Y]
Z= [-1*x+4 for x in X] 

plt.plot(X, Y_rand, 'ro')
plt.plot(X,Y,'b',linewidth=2)
plt.plot(X,Z,'g',linewidth=2)
plt.xlim(0,5)
plt.ylim(0,5)
plt.axis('off')

fig6=plt.gcf()
fig6.savefig('fig6.eps', format='eps',dpi=1000)
plt.show()
'''

'''
fig,ax=plt.subplots(nrows=2,ncols=2)

ax[0,0].broken_barh([(0,4),(4,4),(8,4),(12,4)],(0,4),facecolors=('#000000','#404040','#808080','#FFFFFF'))
ax[0,0].set_xlim(0,16)
ax[0,0].set_ylim(0,4)
ax[0,0].set_ylabel('frequency')
ax[0,0].set_title('Time Analysis')

ax[0,1].broken_barh([(0,16)],(0,1),facecolors='#000000')
ax[0,1].broken_barh([(0,16)],(1,1),facecolors='#404040')
ax[0,1].broken_barh([(0,16)],(2,1),facecolors='#808080')
ax[0,1].broken_barh([(0,16)],(3,1),facecolors='#FFFFFF')
ax[0,1].set_xlim(0,16)
ax[0,1].set_ylim(0,4)
ax[0,1].set_title('FT')

ax[1,0].broken_barh([(0,4),(4,4),(8,4),(12,4)],(0,1),facecolors=('#000000','#2b2b2b','#555555','#808080'))
ax[1,0].broken_barh([(0,4),(4,4),(8,4),(12,4)],(1,1),facecolors=('#2b2b2b','#555555','#808080','#ABABAB'))
ax[1,0].broken_barh([(0,4),(4,4),(8,4),(12,4)],(2,1),facecolors=('#555555','#808080','#ABABAB','#D5D5D5'))
ax[1,0].broken_barh([(0,4),(4,4),(8,4),(12,4)],(3,1),facecolors=('#808080','#ABABAB','#D5D5D5','#FFFFFF'))
ax[1,0].set_xlim(0,16)
ax[1,0].set_ylim(0,4)
ax[1,0].set_xlabel('time')
ax[1,0].set_ylabel('frequency')
ax[1,0].set_title('STFT')

ax[1,1].broken_barh([(0,8),(8,8)],(0,1),facecolors=('#303030','#707070'))
ax[1,1].broken_barh([(0,4),(4,4),(8,4),(12,4)],(1,1),facecolors=('#404040','#606060','#808080','#9F9F9F'))
ax[1,1].broken_barh([(0,2),(2,2),(4,2),(6,2),(8,2),(10,2),(12,2),(14,2)],(2,1),facecolors=('#585858','#686868','#787878','#878787','#979797','#A7A7A7','#B7B7B7','#C7C7C7'))
ax[1,1].broken_barh([(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1),(12,1),(13,1),(14,1),(15,1)],(3,1),facecolors=('#747474','#7C7C7C','#838383','#8B8B8B','#939393','#9B9B9B','#A3A3A3','#ABABAB','#B3B3B3','#BBBBBB','#C3C3C3','#CBCBCB','#D3D3D3','#DBDBDB','#E3E3E3','#EBEBEB'))
ax[1,1].set_xlim(0,16)
ax[1,1].set_ylim(0,4)
ax[1,1].set_xlabel('time')
ax[1,1].set_title('WT')

plt.subplots_adjust(left=0.1,right=0.95,bottom=0.1,top=0.95,wspace=0.2,hspace=0.2)

fig5=plt.gcf()
fig5.savefig('fig5.eps', format='eps', dpi=1000)
plt.show()
'''

'''
def u1(x):
	if x<2:
		return 1/math.sqrt(2)
	else:
		return 0
def v1(x):
	if x<1:
		return 1/math.sqrt(2)
	elif x<2:
		return -1/math.sqrt(2)
	else:
		return 0
def u2(x):
	if x<4:
		return 0.5
	else:
		return 0
def v2(x):
	if x<2:
		return 0.5
	elif x<4:
		return -0.5
	else:
		return 0
def u3(x):
    if x<8:
        return 1/math.sqrt(8)
    else:
        return 0
def v3(x):
    if x<4:
        return 1/math.sqrt(8)
    elif x<8:
        return -1/math.sqrt(8)
    else:
        return 0
t=np.arange(0,10,0.01)
y0=[]
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
y6=[]

for i in t:
	y_0=0
	y0.append(y_0)

plt.figure()

for i in t:
	y_1=u1(i)
	y1.append(y_1)
plt.subplot(321)
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.9, top=0.9,hspace=0.2, wspace=0.4)
plt.plot(t,y1,'b-')
plt.plot(t,y0,'k-')
plt.xlim(0,10)
plt.ylim(-1,1)
plt.ylabel('$u^1_1$',size=18)

for i in t:
    y_2=v1(i)
    y2.append(y_2)
plt.subplot(322)
plt.plot(t,y2,'b-')
plt.plot(t,y0,'k-')
plt.xlim(0,10)
plt.ylim(-1,1)
plt.ylabel('$v^1_1$',size=18)

for i in t:
    y_3=u2(i)
    y3.append(y_3)
plt.subplot(323)
plt.plot(t,y3,'b-')
plt.plot(t,y0,'k-')
plt.xlim(0,10)
plt.ylim(-1,1)
plt.ylabel('$u^2_1$',size=18)

for i in t:
    y_4=v2(i)
    y4.append(y_4)
plt.subplot(324)
plt.plot(t,y4,'b-')
plt.plot(t,y0,'k-')
plt.xlim(0,10)
plt.ylim(-1,1)
plt.ylabel('$v^2_1$',size=18)

for i in t:
    y_5=u3(i)
    y5.append(y_5)
plt.subplot(325)
plt.plot(t,y5,'b-')
plt.plot(t,y0,'k-')
plt.xlim(0,10)
plt.ylim(-1,1)
plt.xlabel('$t$',size=18)
plt.ylabel('$u^3_1$',size=18)

for i in t:
    y_6=v3(i)
    y6.append(y_6)
plt.subplot(326)
plt.plot(t,y6,'b-')
plt.plot(t,y0,'k-')
plt.xlim(0,10)
plt.ylim(-1,1)
plt.xlabel('$t$',size=18)
plt.ylabel('$v^3_1$',size=18)

fig4=plt.gcf()
fig4.savefig('fig4.eps', format='eps', dpi=1000)

plt.show()
'''

'''
fig=plt.figure()
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = 2*X+2*Y
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, color=(1,1,1))
ax.plot([2,0],[2,0],[30,0])
ax.plot([3,2],[3,2],[12,30])
ax.plot([0,3],[0,3],[0,12])
ax.axis('off')
fig2=plt.gcf()
fig2.savefig('fig2.eps', format='eps', dpi=1000)
plt.show()
'''

'''
plt.figure()
plt.arrow(0,0,2,1.2,linestyle=':',length_includes_head=True,head_length=0.05)
plt.text(0.9,0.47,r'$\mathbb{V}_0$',fontsize=18)

plt.arrow(0,0,0.8,0.48,length_includes_head=True,head_length=0.05)
plt.text(0.75,0.4,r'$\mathrm{v_0}$',fontsize=18)

plt.arrow(0.8,0.48,-0.12,0.2,length_includes_head=True,head_length=0.05)
plt.text(0.73,0.65,r'$\mathrm{v-v_0}$',fontsize=18)

plt.arrow(0,0,0.68,0.68,length_includes_head=True,head_length=0.05)
plt.text(0.6,0.65,r'$\mathrm{v}$',fontsize=18)
plt.axis('off')

fig1=plt.gcf()
fig1.savefig('fig1.eps', format='eps', dpi=1000)
plt.show()
'''



