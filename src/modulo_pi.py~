#!/usr/bin/python
PI=3.1415926535897931159979634685441852
import sys
def fun_pi(n):
  n = int(n)
  suma=0.0
  for i in range(1,n+1):
    a= (i-1.0)/float(n)
    b= i/float(n)
    x_i= (i-0.5)/float(n) 
    f= 4.0/(1+((x_i)**2))
    suma=suma+f
  pi=(1/float(n))*suma
  return pi

if __name__=='__main__':
  
  if len(sys.argv) != 3:
    print '     Usted no ha introducido todos los argumentos necesarios.'
    print '     El programa se ejecutara con unos valores predeterminados.'
    n = 5
    veces = 5
  else:    
    n = int(sys.argv[1])
    veces = int(sys.argv[2])
  print ''
  print 'i  PI35DT                                  lista i                                 PI35DT - lista i'
  for rep in range(1, veces+1):
    resta = fun_pi(n)-PI
    print '%d  %1.35f | %1.35f | %1.35f' % (rep, PI, fun_pi(n), resta)
    n = n*2
    

      