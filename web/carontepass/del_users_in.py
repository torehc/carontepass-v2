#script to delete users that are into the space
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carontepass.settings")
import django
django.setup()
from access.models import Log

len_ = len(Log.objects.filter(user_in=True).all())

for i in range(len_):
    obj = Log.objects.filter(user_in=True).first()
    obj.user_in = False
    obj.save()