#Variables amb el nom dels fitxers en els que es guarda el Numero de dispositiu, i el numero de vegades del bucle.
fitxerNDispositiu = "NDispositiu"
fitxerNVegadesBucle = "NVegadesBucle"

#Funcio per llegir un fitxer. Donem com a parametre el nom del fitxer. Retorna la lectura.
def lleguirFitxer(file):
    f = open (file,'r')
    text = f.read()
    f.close()
    return text



def formulariCambiValor(titol, default, file):
    print titol, ". Valor per defecte", default
    numero = input()

    try:
        numero = int(numero)
        print "El nou valor es:", numero
    except ValueError:
        numero = default
        print 'Cambiant el valor per el de defecte', default
        
    f = open (file,'w')
    text = f.write(str(numero))
    f.close()


def menu():
    #Declarem a les varables el valor que te el fitxer.
    NDispositiu = int(lleguirFitxer(fitxerNDispositiu))
    NVegadesBucle = int(lleguirFitxer(fitxerNVegadesBucle))

        
    #Menu per l'usuari
    print ("********************************************************************")
    print ("*   1.Cambiar N. de dispositiu.                                    *")
    print "        Dispositiu actual:", NDispositiu
    print ("*   2.Cambiar numero de mostres per calcular la mitjana.           *")
    print "        N. actual:", NVegadesBucle
    print ("*   3.Sortir                                                       *")
    print ("********************************************************************")
    opccio = str(input("Opcio:"))

    if opccio == "1":
        print ("Opcio 1")
        formulariCambiValor("N. de dispositiu nou", "2", fitxerNDispositiu)
    elif opccio == "2":
        print ("Opcio 2")
        formulariCambiValor("N. de vegades per la mitjana", "60", fitxerNVegadesBucle)
    elif opccio =="3":
        exit()
    else :
        print ("Opcio invalida")


while(1==1):
    menu()
