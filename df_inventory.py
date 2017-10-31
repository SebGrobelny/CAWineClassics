# import modules
import pandas as pd
import sqlite3
from pandas.io import sql

import csv 


def create_df_inventory():

	xls_file = pd.ExcelFile('CWC.csv')
	print xls_file.sheet_names
	df = xls_file.parse('CWC Inventory')
	print df

	# for index, row in df.iterrows():
	# 	print index
	# 	print row
		# for i in range(0,len(row)):
		# 	print "index "+str(i)
		# 	print "row "+str(row[i])

	df.to_csv('out.csv')

create_df_inventory()
# 	df.to_sql('inventory1.db', engine, if_exists='replace')

# create_df_inventory()
# conn = sqlite3.connect('inventory1.db')

# with sqlite3.connect("inventory1.db") as connection:
# 	csvWriter = csv.writer(open("final.csv", "w"))
# 	c = connection.cursor()
# 	rows = c.fetchall()
# 	print rows
# 	csvWriter.writerows(rows)

# conn.execute("SELECT * FROM CWC;")