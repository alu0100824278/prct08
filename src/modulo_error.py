#!/usr/bin/python
import sys
import modulo_pi

def error(n, veces, umbral):  
  for rep in range(1, veces+1):
    aprox = modulo_pi.fun_pi(n)
    resta = abs(aprox - modulo_pi.PI)
    fallo = 0
    if resta > umbral:
      fallo = fallo + 1
  porc = (fallo/float(n))*100
  return porc
           
if __name__=='__main__':
  
  if len(sys.argv) != 4:
    print '     Usted no ha introducido todos los argumentos necesarios.'
    print '     El programa se ejecutara con unos valores predeterminados.'
    n = 5
    veces = 5
    umbral = 10e-04
  else:    
    n = int(sys.argv[1])
    veces = int(sys.argv[2])
    umbral = float(sys.argv[3])
  
  porcentaje = error(n, veces, umbral)
  print 'El porcentaje de errores es: %f ' % porcentaje
  print ''
    