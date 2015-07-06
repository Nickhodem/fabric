import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fabric.settings')
import random
import django
from django.utils import timezone
django.setup()
from knitting.models import Course, Student, Tutor
'''
class Mateo(Tutor):
    name="Mateusz"
    surname = "Pankiewicz"
    actitle="mgr"
    email = "mateuszpankiewicz@gmail.com"
'''
def populate():
    add_course(title="Digital_Knitting",
               start_date=timezone.now,
               finish_date=timezone.now,
               price=250,
               place="Politechnika",
               vacancy=20,
               registration=timezone.now,
               essence="rhino grasshooper"
               )

def add_course(title,start_date,finish_date,price,place,vacancy,registration,essence,):
    c=Course.objects.get_or_create(title=title)[0]
    #c.tutor=tutor
    c.start_date=start_date
    c.finish_date=finish_date
    c.price=price
    c.place=place
    c.vacancy=vacancy
    c.registration=registration
    c.essence=essence
    c.save()
    return c

if __name__ == '__main__':
    print "Starting Scanning population script..."
    populate()