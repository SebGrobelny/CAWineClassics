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
		inventory.packaged = row[3] 
		inventory.color = row[5] 
		inventory.variety = row[2] 
		inventory.lot = row[6] 
		inventory.units = row[7]
		inventory.storage = row[8]
		inventory.year = row[9]
		inventory.ava = row[10]
		inventory.alc = row[11]
		inventory.chemanalysis = row[12]
		inventory.current = row[13]
		inventory.pending = row[14]
		inventory.other = row[15]
		inventory.promised = row[16]
		inventory.available = row[17]
		inventory.comments = row[18]
		inventory.save()
