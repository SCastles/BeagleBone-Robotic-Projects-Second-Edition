import pygame
import math
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep
import serial
import os

class QuadGame(ConnectionListener):
    def Network_close(self, data):
        exit()
    def Network_gamepad(self, data):
        if data["type"] == 10:
            #print "Pressed button "
            #print data["info"]["button"]
            if data["info"]["button"] == 0:
                os.system('/root/rc_wheeled_auto/rc_wheeled_auto ' + str(0) + ' ' + str(1))
            if data["info"]["button"] == 5:
                os.system('/root/rc_wheeled_auto/rc_wheeled_auto ' + str(10) + ' ' + str(0))
            if data["info"]["button"] == 4:
                os.system('/root/rc_wheeled_auto/rc_wheeled_auto ' + str(-10) + ' ' + str(0))
    def __init__(self):
        address=raw_input("Address of Server: ")
        try:
            if not address:
                host, port="localhost", 8000
            else:
                host,port=address.split(":")
            self.Connect((host, int(port)))
        except:
            print "Error Connecting to Server"
            print "Usage:", "host:port"
            print "e.g.", "localhost:31425"
            exit()
        print "Quad client started"
        self.running=False
        while not self.running:
            self.Pump()
            connection.Pump()
            sleep(0.01)


bg=QuadGame() 
while 1:
    if bg.update()==1:
        break
bg.finished()

