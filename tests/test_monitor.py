
from http import client

import sys
sys.path.append('../web/carontepass/')
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carontepass.settings")
import django
django.setup()
from carontepass.settings_local import ESP_IP, RASPBERY_IP


def test_raspberrypi():
    h1=client.HTTPConnection(RASPBERY_IP, 80)
    h1.request('GET', '/')
    conn = h1.getresponse()
    assert conn.status==200

def test_caronteclient():
    hostname = ESP_IP
    response = os.system("ping -c 1 " + hostname + " > /dev/null")
    assert response == 0
