
from http import client

RPI_IP='192.168.1.94'

def test_raspberrypi():
    h1=client.HTTPConnection(RPI_IP,80)
    h1.request('GET','/')
    conn = h1.getresponse()
    assert conn.status==200


