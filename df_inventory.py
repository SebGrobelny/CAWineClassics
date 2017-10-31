# import modules
import pandas as pd
import sqlite3
from pandas.io import sql


def create_df_inventory():

	xls_file = pd.ExcelFile('CWC.csv')
	print xls_file.sheet_names
	df = xls_file.parse('CWC Inventory')
	print df

	for index, row in df.iterrows():
		print index
		print row
		# for i in range(0,len(row)):
		# 	print "index "+str(i)
		# 	print "row "+str(row[i])

	# conn = sqlite3.connect('inventory1.db')

	# df.to_sql(name='CWC', con=conn) 


	# df.to_sql('inventory.db', engine, if_exists='replace')

create_df_inventory()
# conn = sqlite3.connect('inventory1.db')
# conn.execute("SELECT * FROM CWC;")