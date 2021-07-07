# librería de ecuaciones física 

from sympy import init_session
init_session(use_latex=True)

print('-'*30)
print('Biblioteca con las ecuaciones cinemáticas más importantes')
print('Se proporcionan las ecuaciones de movimiento y de velocidad en una lista')


def MRU(x0,v0,t):
    return(x0+v0*t,v0)
print('MRU(x0,v0,t) ==>  (Ec pos, Ec vel)')

def MRU_x(x0,v0,t):
    return(MRU(x0,v0,t)[0])
print('MRU_x(x0,v0,t) ==> (Ec pos)')

def MRU_v(x0,v0,t):
    return(MRU(x0,v0,t)[1])
print('MRU_v(x0,v0,t) ==> (Ec vel)')

def MRUA(x0,v0,a,t):
    return(x0+v0*t+1/2*a*t**2, v0+a*t)
print('MRUA(x0,v0,a,t) ==>  (Ec pos, Ec vel)')

def MRUA_x(x0,v0,a,t):
    return(MRUA(x0,v0,a,t)[0])
print('MRUA_x(x0,v0,a,t) ==>  (Ec pos)')

def MRUA_v(x0,v0,a,t):
    return(MRUA(x0,v0,a,t)[1])
print('MRUA_v(x0,v0,a,t) ==>  (Ec vel)')

# Definimos la función Sol_correcta(solución_lista) que escoge la solución
# correcta. 

def sSol_correcta(s):
    # Es solución única
    if len(s)>1:                   # Si es doble solución...
        if s[0]*s[1]<0:            #  Si tienen diferente signo
            t_sol=max(s[0],s[1])   #    la solución es la mayor de ellas
        else:                      #  Si tiene el mismo signo (mal ambos neg)
            t_sol=min(s[0],s[1])   #    la solución es la menor de ellas
    else:                          # es solución única
        t_sol = s[0]               #    para evitar que sea una lista
    return(t_sol)

def Sol_correcta(s):
    # Es solución única
    if len(s)>1:                   # Si es doble solución...
        if ( s[0]**2<0 or s[1]**2<0):    # Alguno es número complejo
            print ('¡¡ Alguna solucion es compleja !!.\n   Revisa tus ecuaciones.')
            return
        else:
            if s[0]*s[1]<0:            #  Si tienen diferente signo
                t_sol=max(s[0],s[1])   #    la solución es la mayor de ellas
            else:                      #  Si tiene el mismo signo (mal ambos neg)
                t_sol=min(s[0],s[1])   #    la solución es la menor de ellas
    else:                          # es solución única
        t_sol = s[0]               #    para evitar que sea una lista
    return(t_sol)
print('\nLa siguiente función devuelve de estre las soluciones de una ecuación de segundo grado, la positiva, y si son dos, la menor de estas.')
print('Sol_correcta(s) ==>  Solución correcta')
