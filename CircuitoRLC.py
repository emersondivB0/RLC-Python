#from locale import MON_1
import numpy as np
import matplotlib.pyplot as graf
import scipy.signal as signal
import scipy.stats as stats

#DEFINIR SUBRUTINAS
#DETERMINAR EL TIPO DE RESPUESTA
def respuestaDC():
    global a
    global w
    a=R/(2*L)
    w=1/np.sqrt(L*C)
    print(a,w)
    if a>w:
        sobre_DC()
    elif a==w:
        critica_DC()
    else:
        sub_DC()
    return


#SUBRUTINAS PARA DC
def sobre_DC():
    m1=(-a)+np.sqrt((a**2)-(w**2))
    m2=(-a)-np.sqrt((a**2)-(w**2))
    C1=Vo/(L*(m1-m2))
    a1=0
    b1=(m1-m2)
    t = np.linspace(a1, b1, 1000)
    vi=np.ones(1000)*Vo
    i = C1*(np.exp(m1*t)-np.exp(m2*t))
    graf.subplot(122)
    graf.title('Respuesta i(t) Sobreamortiguada.')
    graf.plot(t,i)
    graf.xlabel('t')
    graf.ylabel('i(t)')
    graf.grid(True)
    graf.subplot(121)
    graf.title('Entrada de Vo')
    graf.plot(t,vi)
    graf.xlabel('t')
    graf.ylabel('Vi')
    graf.grid(True)
    graf.show()

def critica_DC():
    m1=(-a)
    C1=Vo/L
    a1=0
    b1=(a)
    t = np.linspace(a1, b1, 1000)
    vi=np.ones(1000)*Vo
    i = np.multiply(C1*t,(np.exp(m1*t)))
    graf.subplot(122)
    graf.title('Respuesta i(t) Críticamente amortiguada.')
    graf.plot(t,i)
    graf.xlabel('t')
    graf.ylabel('i(t)')
    graf.grid(True)
    graf.subplot(121)
    graf.title('Entrada de Vo')
    graf.plot(t,vi)
    graf.xlabel('t')
    graf.ylabel('Vi')
    graf.grid(True)
    graf.show()

def sub_DC():
    m1=-np.sqrt(-(a**2)+(w**2))
    C1=-Vo/(L*m1)
    a1=0
    b1=-m1/4
    print(m1)
    t = np.linspace(a1, b1, 1000)
    vi=np.ones(1000)*Vo
    i = np.multiply(C1*(np.exp(-a*t)),np.sin(-m1*t))
    graf.subplot(122)
    graf.title('Respuesta i(t) Subamortiguada.')
    graf.plot(t,i)
    graf.xlabel('t')
    graf.ylabel('i(t)')
    graf.grid(True)
    graf.subplot(121)
    graf.title('Entrada de Vo')
    graf.plot(t,vi)
    graf.xlabel('t')
    graf.ylabel('Vi')
    graf.grid(True)
    graf.show()

# SUBRUTINAS PARA AC
def respuestaAC():
    w=2*(np.pi)*f
    XC=1/(w*C)
    XL=w*L
    Z=np.sqrt((R**2)+((XL-XC)**2))
    Io=Vo/Z
    phi=np.arctan((XL-XC)/R)
    t = np.linspace((-3/f), (3/f), 1000)
    vi = Vo*(np.sin(w*t))
    i = Io*(np.sin((w*t)-phi))
    print(w)
    graf.subplot(122)
    graf.title('Respuesta i(t) con entrada AC.')
    graf.plot(t,i,'r')
    graf.xlabel('t')
    graf.ylabel('i(t)')
    graf.grid(True)
    graf.subplot(121)
    graf.title('Entrada v(t) Senoidal.')
    graf.plot(t,vi)
    graf.xlabel('t')
    graf.ylabel('vi(t)')
    graf.grid(True)
    graf.show()

#ENTRADA DE VARIABLES
print("A continuación vamos a ingresar los valores críticos.")
print("Resistencia (Ohm):")
R= float(input())
print("Capacitancia (F):")
C=float(input())
print("Inductacia (H):")
L=float(input())

#SELECCIONAR FUENTE
print("Seleccione el tipo de Fuente.")
print("Para Fuente Continua ingrese DC, Para Alterna ingrese AC")
TF=input()

if TF=="DC":
    print("Ingrese valor de señal (v):")
    Vo=float(input())
    respuestaDC()
elif TF=="AC":
    print("Ingrese valor de amplitud (v):")
    Vo=float(input())
    print("Ingrese valor de frecuencia (Hz):")
    f=float(input())
    respuestaAC()
else:
    print("Valor incorrecto, ingrese DC o AC.")

