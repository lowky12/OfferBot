import sqlite3

DB_CONN = sqlite3.connect('offerbot.db')
DB_CURSOR = DB_CONN.cursor()

def init_tables():
	DB_CURSOR.execute('CREATE TABLE IF NOT EXISTS users(username text, jobs real, reputation real)')
	DB_CURSOR.execute('CREATE TABLE IF NOT EXISTS  oldposts(id text)')
	DB_CONN.commit()

def add_oldpost(id):
	DB_CURSOR.execute('INSERT INTO oldposts VALUES(?)', [id])
	DB_CONN.commit()

def del_oldpost(id):
	DB_CURSOR.execute('DELETE FROM oldposts WHERE id = ?', [name])
	DB_CONN.commit()

def is_oldpost(id):
	DB_CURSOR.execute('SELECT * FROM oldposts WHERE id = ?', [id])
	return DB_CURSOR.fetchone() is not None

def get_user(name):
	DB_CURSOR.execute('SELECT * FROM users WHERE username = ?', [name])
	return DB_CURSOR.fetchone() is not None

def add_user(name, jobs, rep):
	DB_CURSOR.execute('INSERT INTO users VALUES(?, ?, ?)', [name, jobs, rep])
	DB_CONN.commit()

def update_user(name, jobs, rep):
	DB_CURSOR.execute('UPDATE users SET(username = ?, jobs = ?, reputation = ?) WHERE username = ?', [name, jobs, rep, name])
	DB_CONN.commit()

def del_user(name):	
	DB_CURSOR.execute('DELETE FROM users WHERE username = ?', [name])
	DB_CONN.commit()

def is_user(name):
	DB_CURSOR.execute('SELECT * FROM oldposts WHERE username = ?', [name])
	return DB_CURSOR.fetchone() is not None