import sqlite3

"""
sql_statement - string
args - tuple. If only one item, must append with empty comma.
example: sql_statement = 'SELECT * FROM Stock WHERE TickerSymbol=?
		 args = ('APPL',)
"""
def db_query(sql_statement, args=(), onerow=False):
	conn = sqlite3.connect('db.sqlite3')
	conn.row_factory = sqlite3.Row

	cursor = conn.cursor()
	try:
		cursor.execute(sql_statement, args)

		# Will always return a single record
		#row = cursor.fetchone()
		rows = cursor.fetchone() if onerow else cursor.fetchall()
		if not rows:
			return None if onerow else []
		rows = dict(rows) if onerow else [dict(row) for row in rows]
		return rows
	finally:
		conn.close()

def db_execute(sql, args=()):
    """
    Execute a query and return number of affected rows
    """
    conn = sqlite3.connect('db.sqlite3')
	
    cursor = conn.cursor()
    cursor.execute(sql, args)

    row_values = cursor.lastrowid

    conn.commit()
    conn.close()

    return row_values
