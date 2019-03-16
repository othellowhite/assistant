import sqlite3
import pandas as pd


conn=sqlite3.connect('res/core.db')
c = conn.cursor()

# [table example]
# c.executemany("INSERT INTO t_config VALUES (?,?,?,?,?,?)", [
# 	('office', 'localhost:8201', False, "{‘version’: ‘0.0.1’}", '2019-03-01T00:00:00+0900','2019-03-01T00:00:00+0900'),
# 	('http', 'localhost:8201', False, "{‘version’: ‘0.0.1’}", '2019-03-01T00:00:00+0900','2019-03-01T00:00:00+0900'),
# ])

try:
	c.execute('''
		SELECT * 
		FROM t_config 
		''')
	print( 'INFO: sqlite3 connected, \n{}'.format(pd.DataFrame(c.fetchall())) )
except Exception as e:
	if 'no such table: t_config' in str(e):
		c.execute('''
			CREATE TABLE t_config 
				(worker text, path text, active boolean, config text, created_at text, updated_at text)
		''')
	else:
		print( 'ERR: sqlite3 connect failed, {}'.format(e) )