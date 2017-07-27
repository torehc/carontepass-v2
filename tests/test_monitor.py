
from http import client
import os


print(os.getcwd())

import sys
sys.path.append('../')
from web.carontepass.carontepass.settings_local import ESP_IP, RASPBERY_IP


def test_raspberrypi():
    h1=client.HTTPConnection(RASPBERY_IP, 80)
    h1.request('GET', '/')
    conn = h1.getresponse()
    assert conn.status==200

def test_caronteclient():
    hostname = ESP_IP
    response = os.system("ping -c 1 {} > /dev/null".format(hostname))
    assert response == 0
