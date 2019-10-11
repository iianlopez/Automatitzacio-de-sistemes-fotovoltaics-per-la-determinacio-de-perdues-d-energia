#!/usr/bin/env python
from ina219 import INA219
import time
import MySQLdb
from array import *
import sys

SHUNT_OHMS = 0.1
MAX_EXPECTED_AMPS = 0.2

fitxerNDispositiu = "NDispositiu"
fitxerNVegadesBucle = "NVegadesBucle"

while (true): #Comença el bucle infinit.
    #Funcio per llegir un fitxer. Donem com a parametre el nom del fitxer. Retorna la lectura.
    def lleguirFitxer(file):
        f = open (file,'r')
        text = f.read()
        f.close()
        return text

    #Dispositiu 1 es la estacio de control de llum
    """
    #Comprovem que s'estigui donant el parametre realcionat amb el dispositiu. Si no es dona. El programa es tanca, ja que no sabem a quin dispositu estem calculant.

    if (len(sys.argv)>1):
         nDispositiu = sys.argv[1]
         print "Dispositiu ", nDispositiu
         
    else :
        print ("No hi s'ha indicat el parametre del dispositiu")
        exit()
            
    """



    """
    nVegades = 60
    """

    NDispositiu = int(lleguirFitxer(fitxerNDispositiu))
    nVegades = int(lleguirFitxer(fitxerNVegadesBucle))

    #Aqui comenccaria el bucle
    contador = 0

    v = []
    p = []

    vAvg = 0
    pAvg = 0

    while contador<nVegades :
         ina = INA219(SHUNT_OHMS)
         ina.configure(ina.RANGE_16V)
         v.append(int(ina.shunt_voltage()*1000))
         p.append(int(ina.power()*1000))
         time.sleep(1)
         contador = contador +1
         print contador , "/" , nVegades


    #print v
    #print p

    pAvg = float(sum(p)/len(p))/1000
    vAvg = float(sum(v)/len(v))/1000

    print pAvg
    print vAvg

    #print ("V", vAvg)
    #print ("P",  pAvg)

    SQL = ("INSERT INTO `dades` (`id_dispositiu`, `data`, `w`, `v`) VALUES ('" + str(NDispositiu) +"', CURRENT_TIMESTAMP, '" + str(pAvg) + "', '" + str(vAvg) +  "')")

    #print SQL

    db = MySQLdb.connect("localhost", "admin", "123456", "Hiperion")
    curs=db.cursor()

    try:
        curs.execute (SQL)

        db.commit()
        print ("Enregistrat")

    except:
        print ("ERROR: the database is being rolled back")
        print SQL
        db.rollback()
        
    time.sleep(300) #Espera de 300 segons = 5 Minuts.

    
