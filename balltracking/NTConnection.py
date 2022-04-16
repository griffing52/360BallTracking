import threading
from networktables import NetworkTables, NetworkTablesInstance


# manages NetworkTables Connection
class NTConnection:
    # HOST = "127.0.0.1" or "localhost" for localhost
    def __init__(self, HOST="10.2.94.2"):
        self.HOST = HOST

        cond = threading.Condition()
        notified = [False]

        def connectionListener(connected, info):
            print(info, '; Connected=%s' % connected)
            with cond:
                notified[0] = True
                cond.notify()

        NetworkTables.initialize(server=self.HOST) # localhost for simulation, 10.TE.AM.2 format for real robot
        NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

        with cond:
            print("Waiting")
            if not notified[0]:
                cond.wait()

        # Insert your processing code here
        print("Connected!")

        self.instance = NetworkTablesInstance.getDefault().getTable("SmartDashboard") # TODO previously SmartDashboard