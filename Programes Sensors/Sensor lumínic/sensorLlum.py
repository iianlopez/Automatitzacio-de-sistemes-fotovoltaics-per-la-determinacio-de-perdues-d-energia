#!/usr/bin/env python
import smbus
import time
import MySQLdb
from array import *
import sys


"""
INICIALITZEM EL DISPOSITIU CONECTAT PER I2C.
"""


# Get I2C bus
bus = smbus.SMBus(1)

# TSL2561 address, 0x39(57)
# Select control register, 0x00(00) with command register, 0x80(128)
#       0x03(03)    Power ON mode
bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
# TSL2561 address, 0x39(57)
# Select timing register, 0x01(01) with command register, 0x80(128)
#       0x02(02)    Nominal integration time = 402ms
bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

time.sleep(0.5)

#Variables amb el nom dels fitxers en els que es guarda el Numero de dispositiu, i el numero de vegades del bucle.
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

    NDispositiu = int(lleguirFitxer(fitxerNDispositiu))
    nVegades = int(lleguirFitxer(fitxerNVegadesBucle))

    #Aqui comenccaria el bucle
    contador = 0

    infrared = []
    visible = []

    infraredAvg = 0
    visibleAvg = 0

    while contador<nVegades :
        # Read data back from 0x0C(12) with command register, 0x80(128), 2 bytes
        # ch0 LSB, ch0 MSB
        data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

        # Read data back from 0x0E(14) with command register, 0x80(128), 2 bytes
        # ch1 LSB, ch1 MSB
        data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

        # Convert the data
        ch0 = data[1] * 256 + data[0]
        ch1 = data1[1] * 256 + data1[0]
        infrared.append(int(ch1))
        visible.append(int((ch0 - ch1)))
        time.sleep(1)
        contador = contador +1
        print contador , "/" , nVegades



    infraredAvg = float(sum(infrared)/len(infrared))
    visibleAvg = float(sum(visible)/len(visible))

    total = float(infraredAvg + visibleAvg)

    print ("IR", infraredAvg)
    print ("visible",  visibleAvg)
    print ("Total", total)

    SQL = ("INSERT INTO `dadessensorllum` (`id_dispositiu`, `data`, `lux`) VALUES ('" + str(NDispositiu) +"', CURRENT_TIMESTAMP, '" + str(total)  +  "')")

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
