import sys,os 


# Full path and name to your csv file 
filename = "CWCInventory.csv"
# Full path to your django project directory 
your_djangoproject_home="/home/sgrobelny/desktop/seb-django/mysite" 

print your_djangoproject_home
sys.path.append(your_djangoproject_home) 
print sys.path

from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

application = get_wsgi_application()

from main.models import Inventory 

import csv 


dataReader = csv.reader(open(filename), delimiter=',', quotechar='"') 
for row in dataReader: 
	# Ignore the header row, import everything else 
	if row[0] != 'date' or row[0] != 'last review': 
		inventory = Inventory() 
		inventory.packaged = row[1] 
		inventory.color = row[2] 
		inventory.variety = row[3] 
		inventory.lot = row[4] 
		inventory.units = row[5]
		inventory.storage = row[6]
		inventory.year = row[7]
		inventory.ava = row[8]
		inventory.alc = row[9]
		inventory.chemanalysis = row[10]
		inventory.current = row[11]
		inventory.pending = row[12]
		inventory.other = row[13]
		inventory.promised = row[14]
		inventory.available = row[24]
		inventory.comments = row[25]

		inventory.save()




