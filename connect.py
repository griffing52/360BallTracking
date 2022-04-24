import threading
import time
import json
import keyboard
import socket
from networktables import NetworkTables, NetworkTablesInstance

HOST = "127.0.0.1"
PORT = 65432

cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

NetworkTables.initialize(server=HOST) # localhost for simulation, 10.TE.AM.2 format for real robot
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print("Waiting")
    if not notified[0]:
        cond.wait()

# Insert your processing code here
print("Connected!")

inst = NetworkTablesInstance.getDefault().getTable("SmartDashboard")
# inst = NetworkTablesInstance.getDefault().getTable("SmartDashboard")

robot = inst.getEntry("Field/Robot")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print('Connected by ', addr)

with conn:
    while True:
        response = conn.recv(1024)
        if not response:
            break
        vals = robot.getDoubleArray([0])
        data = ",".join(map(str, vals))
        conn.send(data.encode())

conn.close()
s.close()