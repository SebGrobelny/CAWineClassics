# import modules
import sys,os 

from django.core.wsgi import get_wsgi_application

filename= 'out.csv'
# Full path to your django project directory 
your_djangoproject_home="/home/sgrobelny/desktop/seb-django/mysite" 

print your_djangoproject_home
sys.path.append(your_djangoproject_home) 
print sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
application = get_wsgi_application()

from main.models import Inventory 
import csv

dataReader = csv.reader(open(filename), delimiter=',', quotechar='"') 
for row in dataReader: 		
		inventory = Inventory() 
		inventory.packaged = row[2] 
		inventory.color = row[4] 
		inventory.variety = row[3] 
		inventory.lot = row[5] 
		inventory.units = row[6]
		inventory.storage = row[7]
		inventory.year = row[8]
		inventory.ava = row[9]
		inventory.alc = row[10]
		inventory.chemanalysis = row[11]
		inventory.current = row[12]
		inventory.pending = row[13]
		inventory.other = row[14]
		inventory.promised = row[15]
		inventory.available = row[16]
		inventory.comments = row[17]
		inventory.save()
