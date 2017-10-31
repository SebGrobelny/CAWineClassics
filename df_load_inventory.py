# import modules
import pandas as pd
import sqlite3
from pandas.io import sql
import sys,os 


# Full path to your django project directory 
your_djangoproject_home="/home/sgrobelny/desktop/seb-django/mysite" 

print your_djangoproject_home
sys.path.append(your_djangoproject_home) 
print sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from main.models import Inventory 

xls_file = pd.ExcelFile('CWC.csv')
print xls_file.sheet_names
df = xls_file.parse('CWC Inventory')
print df

for index, row in df.iterrows():
		
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
		invenotry.comments = row[17]
