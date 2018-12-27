#coding:utf-8
import numpy as np
import matplotlib.pyplot as pl

def f1(x,QL):
    return 1/np.sqrt((1 - x**2)**2+(x/QL)**2)

def f2(x,QH):
    return 1/np.sqrt(((1/x)**2 - 1)**2+(1/x/QH)**2)

def f3(x,QP):
    return 1/np.sqrt(1+QP**2*(1/x - x)**2)

def f4(x,Qn):
    return np.abs(x**2 - 1)/np.sqrt((x**2 - 1)**2 + (x/Qn)**2)

x = np.logspace(-1,1,1000)
y0707 = 20*np.log(f1(x,np.sqrt(2)/2))
y1 = 20*np.log(f1(x,1))
y2 = 20*np.log(f1(x,2))
y10 = 20*np.log(f1(x,10))
pl.semilogx(x,y0707,'-',x,y1,'-',x,y2,'-',x,y10,'-')
pl.text(1*10**(0.05),40,'Q=10')
pl.text(1*10**(-0.08),17,'Q=2')
pl.text(1*10**(-0.08),2,'Q=1')
pl.text(1*10**(-0.15),-20,'Q=0.707')
pl.xlabel(r'$\frac{\omega}{\omega_L}$')
pl.ylabel(r'20lg|$\frac{A(j\omega)}{A_o}$|')
pl.grid()
pl.savefig('fig2.pdf')
pl.close()

y0707 = 20*np.log(f2(x,np.sqrt(2)/2))
y1 = 20*np.log(f2(x,1))
y2 = 20*np.log(f2(x,2))
y10 = 20*np.log(f2(x,10))
pl.semilogx(x,y0707,'-',x,y1,'-',x,y2,'-',x,y10,'-')
pl.text(1*10**(0.05),40,'Q=10')
pl.text(1*10**(-0.05),17,'Q=2')
pl.text(1*10**(-0.07),2,'Q=1')
pl.text(1*10**(-0.15),-20,'Q=0.707')
pl.xlabel(r'$\frac{\omega}{\omega_H}$')
pl.ylabel(r'20lg|$\frac{A(j\omega)}{A_o}$|')
pl.grid()
pl.savefig('fig4.pdf')
pl.close()

y0707 = 20*np.log(f3(x,np.sqrt(2)/2))
y1 = 20*np.log(f3(x,1))
y2 = 20*np.log(f3(x,2))
y10 = 20*np.log(f3(x,10))
pl.semilogx(x,y0707,'-',x,y1,'-',x,y2,'-',x,y10,'-')
pl.xlabel(r'$\frac{\omega}{\omega_P}$')
pl.ylabel(r'20lg|$\frac{A(j\omega)}{A_o}$|')
pl.grid()
pl.savefig('fig6.pdf')
pl.close()

#y0707 = 20*f4(x,np.sqrt(2)/2)
y1 = 20*np.log(f4(x,1))
#y2 = 20*f4(x,2)
#y10 = 20*f4(x,10)
pl.semilogx(x,y1,'-')
pl.xlabel(r'$\frac{\omega}{\omega_z}$')
pl.ylabel(r'20lg|$\frac{A(j\omega)}{A_o}$|')
pl.grid()
pl.savefig('fig8.pdf')
pl.close()