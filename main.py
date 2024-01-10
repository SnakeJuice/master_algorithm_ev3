#!/usr/bin/env pybricks-micropython
##########################################################
# Algoritmo Master que maneja la conexión entre robots   #
#                                                        #
# Autores:                                               #
# - Cristian Anjari                                      #
# - Marcos Medina                                        #
#                                                        #
# Para proyecto de tesis 2023                            #
#                                                        #
# Universidad de Santiago de Chile                       #
# Facultad de Ciencia                                    #
#                                                        #
# Licenciatura en Ciencia de la Computación/             #
# Analista en Computación Científica                     #
#                                                        #
# Santiago, Chile                                        #
# 05/01/2024                                             #
##########################################################
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
from pybricks.tools import wait

ev3 = EV3Brick()

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)
rbox = TextMailbox('rec1', server)

# The server must be started before the client!
ev3.screen.print('waiting for connection...')
server.wait_for_connection(2)
#ev3.screen.print('connected!')
#robot.wait(300)
ev3.screen.clear()

while True:
    mbox.wait()
    print("mbox.read ",mbox.read())
    print("rbox.read ",rbox.read())
    mbox.send('inicia buscador')
    mbox.wait_new()

# Si el mbox.read inicia con un [ significa que es una lista y la guardamos en una variable
    if(mbox.read()[0] == '['):
        rojos = mbox.read()
        ev3.screen.print("lista roja",rojos)
        ev3.speaker.beep()
    
    mbox.send('recibido')
    mbox.wait_new()

    if(mbox.read()[0] == '['):
        verde = mbox.read()
        ev3.screen.print("lista verde",verde)
        mbox.send('listo')

    mbox.wait_new()
    print("mbox.read ",mbox.read())
    if(mbox.read() == 'terminado'):
        rbox.send('Recolector1 muevete')
        ev3.speaker.beep()