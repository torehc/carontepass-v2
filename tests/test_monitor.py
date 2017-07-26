
from http import client
import os

RPI_IP='192.168.1.94'
CARONTE_IP='192.168.1.21'

def test_raspberrypi():
    h1=client.HTTPConnection(RPI_IP,80)
    h1.request('GET','/')
    conn = h1.getresponse()
    assert conn.status==200

def test_caronteclient():
    hostname = CARONTE_IP
    response = os.system("ping -c 1 " + hostname + " > /dev/null")
    assert response == 0
