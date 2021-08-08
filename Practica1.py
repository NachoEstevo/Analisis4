#!/usr/bin/env python
# coding: utf-8

# <h1>Guia 1 Python Teoria de error</h1>

# In[3]:


import math


# In[4]:


first = 22/7
errOne = abs(math.pi - first)
print(errOne)


# In[5]:


second = 333/106
errTwo = abs(math.pi - second)
print(errTwo)


# In[6]:


third = 355/113
errThree = abs(math.pi - third)
print(errThree)


# Errores relativos y porcentuales  er(x) = e(x)/X  ejemplo 0.00059/3.141 ese es el relativo. Multiplicado por 100 da el porcentual 

# In[7]:


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

# In[13]:


firstE = 2.72
errOneE = abs(math.e - firstE)
print(errOneE)
print('Cotas: ',firstE-errOneE,'< e <',firstE + errOneE)


# In[15]:


secondE = 2.718
errTwoE = abs(math.e - secondE)
print(errTwoE)
print('Cotas: ',secondE-errTwoE,'< e <',secondE + errTwoE)


# In[17]:


thirdE = 2.7183
errThreeE = abs(math.e - thirdE)
print(errThreeE)
print('Cotas: ',thirdE-errThreeE,'< e <',thirdE + errThreeE)


# In[11]:


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

# In[43]:


lSpeedFoucalt = 298000
lSpeed = 299776

absError = abs(lSpeed - lSpeedFoucalt)
print(absError)

relError = absError/lSpeed
print(relError)

percentError = relError*100
print(round(percentError,3),'%')


# In[45]:


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

# In[25]:


#Approximate e with the limit
def aproxE(n):
   return((1+1/n)**n)

val1 = aproxE(10)
print(val1)

absErr1 = abs(math.e - val1)
print('absolute error:',absErr1)


# In[26]:


val2 = aproxE(100)
print(val2)

absErr2 = abs(math.e - val2)
print('absolute error:',absErr2)


# In[27]:


val3 = aproxE(10**25) #Se aleja mas del valor esperado. Obtenemos e al resolver la indeterminacion cuando x tiende a inf
print(val3)

absErr3 = abs(math.e - val3)
print('absolute error:',absErr3)


# <h2>Ejercicio 4</h2>

# In[53]:


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

