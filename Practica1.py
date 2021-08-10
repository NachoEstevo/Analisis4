#!/usr/bin/env python
# coding: utf-8

# <h1>Guia 1 Python Teoria de error</h1>

# In[2]:


import math


# In[3]:


first = 22/7
errOne = abs(math.pi - first)
print(errOne)


# In[4]:


second = 333/106
errTwo = abs(math.pi - second)
print(errTwo)


# In[5]:


third = 355/113
errThree = abs(math.pi - third)
print(errThree)


# Errores relativos y porcentuales  er(x) = e(x)/X  ejemplo 0.00059/3.141 ese es el relativo. Multiplicado por 100 da el porcentual 

# In[6]:


relOne = errOne/math.pi
relTwo = errTwo/math.pi
relThree = errThree/math.pi

print('relative one: ', relOne)
print('relative two: ', relTwo)
print('relative three: ', relThree)

print('----------------------')

print('porcentual one: ', round(relOne*100,3),'%')
print('porcentual two: ', round(relTwo*100,3),'%')
print('porcentual three: ', round(relThree*100,3),'%')


# Calculo de error de otro numero irracional. e

# In[7]:


firstE = 2.72
errOneE = abs(math.e - firstE)
print(errOneE)
print('Cotas: ',firstE-errOneE,'< e <',firstE + errOneE)


# In[8]:


secondE = 2.718
errTwoE = abs(math.e - secondE)
print(errTwoE)
print('Cotas: ',secondE-errTwoE,'< e <',secondE + errTwoE)


# In[9]:


thirdE = 2.7183
errThreeE = abs(math.e - thirdE)
print(errThreeE)
print('Cotas: ',thirdE-errThreeE,'< e <',thirdE + errThreeE)


# In[10]:


relOneE = errOneE/math.e
relTwoE = errTwoE/math.e
relThreeE = errThreeE/math.e

print('relative one: ', relOneE)
print('relative two: ', relTwoE)
print('relative three: ', relThreeE)

print('----------------------')

print('porcentual one: ', round(relOneE*100,3),'%')
print('porcentual two: ', round(relTwoE*100,3),'%')
print('porcentual three: ', round(relThreeE*100,3),'%')


# In[ ]:





# <h2>Ejercicio 2</h2>

# En 1862 el fisico Foucault, utilizando un espejo giratorio, calculo en 298000 km/s la velocidad
# de la luz. Aceptando como exacta la velocidad de 299776 km/s, calcular el error absoluto y el
# error relativo cometido por Foucault.
# Por otra parte, la determinacion de la constante universal h, que desempena un papel central
# en la teoria de la mecanica cuantica, realizada por Planck en 1913 dio el valor de 6.41 x 10-27
# erg por seg. Adoptando el valor de 6.623 x 10-27 erg por seg, calcular el error absoluto y relativo
# cometido por Planck.
# .Que medida tiene menor error absoluto? .Cual es mas precisa?
# 

# In[11]:


lSpeedFoucalt = 298000
lSpeed = 299776

absError = abs(lSpeed - lSpeedFoucalt)
print(absError)

relError = absError/lSpeed
print(relError)

percentError = relError*100
print(round(percentError,3),'%')


# In[12]:


planck = 6.41*(10**-27)
realConstant = 6.623*(10**-27)

absError2 = abs(realConstant - planck)
print(absError2)

relError2 = absError2/realConstant
print(relError2)

percentError2 = relError2*100
print(round(percentError2,3),'%')


# The approximation for the speed of light, made by Foucault was 2.624% more accurate than the one made by Planck

# <h2>Ejercicio 3</h2>

# In[13]:


#Approximate e with the limit
def aproxE(n):
   return((1+1/n)**n)

val1 = aproxE(10)
print(val1)

absErr1 = abs(math.e - val1)
print('absolute error:',absErr1)


# In[14]:


val2 = aproxE(100)
print(val2)

absErr2 = abs(math.e - val2)
print('absolute error:',absErr2)


# In[15]:


val3 = aproxE(10**25) #Se aleja mas del valor esperado. Obtenemos e al resolver la indeterminacion cuando x tiende a inf
print(val3)

absErr3 = abs(math.e - val3)
print('absolute error:',absErr3)


# <h2>Ejercicio 4</h2>

# In[16]:


#Derivada del sen(x)

xArr = [1,0.5,0.1,0.01,0]
hArr = [10**-1,10**-2,10**(-30)]

def derivateSin(x,h):
    return (math.sin(x+h) - math.sin(x))/h

def derivateCos(x,h):
     return (math.cos(x+h) - math.cos(x))/h

for x in xArr:
    for h in hArr:
        print('Sin derivate in:',x, 'with h =',h,'=',round(derivateSin(x,h),3))
        print('Cos derivate in:',x, 'with h =',h,'=',round(derivateCos(x,h),3),'\n')


# <h2>Ejercicio 5</h2>

# Escribir y probar un programa para calcular:
#         f(x) = sqrt(x^2 + 1)-1
#         g(x) = x^2/sqrt(x^2 + 1)-1
# para una sucesión de valores de x, como: 8^-1, 8^-2, 8^-3
# ...Aunque f = g, la computadora dará resultados diferentes.
# ¿Cuáles de los resultados son de fiar y cuáles no? 

# In[25]:


def f(x):
    return math.sqrt(x**2 + 1)-1
def g(x):
    return x**2/math.sqrt(x**2 + 1)-1

xArr = [8**-1,8**-2,8**-3]

for x in xArr:
    print('f(',x,') = ',f(x))
    print('g(',x,') = ',g(x))
    print('\n')


# <h2>Ejercicio 6</h2>

# Usar la computadora para imprimir los valores de las funciones
# 
# en 101 puntos igualmente espaciados y que cubran el intervalo [0.99, 1.01]. Calcular cada función en la
# forma en que está escrita. Observar que las tres funciones son matemáticamente idénticas. Explique
# porque no todos los valores son positivos. 

# In[36]:



def f(x):
    return x**8 - 8*x**7 + 28*x**6 - 56*x** 5 + 70*x** 4 -56*x** 3 + 28*x**2 - 8*x + 1

def g(x):
    return (((((((x-8)*x + 28)*x - 56)*x + 70)*x - 56)*x + 28)*x - 8)*x + 1

def h(x):
    return (x - 1)**8

for i in range(0, 101):
    x = 0.99 + i*0.0002
    print("%.4f | f(x) = %25s | g(x) = %25s | h(x) = %25s" % (x, f(x), g(x), h(x)))


# <h2>Ejercicio 8</h2>

# Formula Cuadratica: Haga un programa que evalúe las raíces con el primer algoritmo y con el segundo para
# x^2 + bx + 1 =0
# con b = 10, 100, 1000, 10000... Discutir los resultados obtenidos.

# In[41]:


def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2.0 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2.0 * a)
    return x1, x2

def improved_Quadratic(a, b, c):
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2.0 * a)
    x1 = c / (a*x2)
    return round(x1,4), round(x2,4)


# In[45]:


print('Ordinary quadratic formula: ',quadratic(1, 62.10, 1))

print('Improved Quadratic: ',improved_Quadratic(1, 62.10,1))


# In[51]:


for x in range(1, 10):
    b = 10**x
    print("%15s | Quad: %30s | Imp Quad: %30s" % (b, quadratic(1,b,1), improved_Quadratic(1,b,1)))


# In[ ]:




