import sys
import time

def callMe(name, number):
    print("&: Hello?")
    time.sleep(1)
    print("&: Wie is daar?")
    time.sleep(1)
    print("#: Ik ben het"+ name)
    time.sleep(1)
    print("&:Hallo "+ name+ " Sorry ik ben nu heel erg bezig met iets?")
    time.sleep(1)
    print("#: Oke geen probleem.")
    time.sleep(1)
    print("&: wat is jou telefoonnummer?")
    time.sleep(1)
    print("#Mijn nummer is ", number)
    time.sleep(1)
    print("&: dank je wel. Ik bel je wel later, doei!")
    time.sleep(1)
    print("#: Doei!")
    time.sleep(1)
    print("druk...")

callMe(sys.argv[1], sys.argv[2])