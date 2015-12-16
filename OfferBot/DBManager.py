#!/usr/bin/env python
"""
Bot Database Management
"""
import sqlite3

DB_CONN = sqlite3.connect('offerbot.db')
DB_CURSOR = DB_CONN.cursor()


def init_tables():
    """
    Sets up the database
    """
    DB_CURSOR.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, jobs REAL, reputation REAL)')
    DB_CURSOR.execute('CREATE TABLE IF NOT EXISTS  oldposts(id TEXT)')
    DB_CONN.commit()


def add_oldpost(id):
    """
    Adds an old post to the database with id
    """
    DB_CURSOR.execute('INSERT INTO oldposts VALUES(?)', [id])
    DB_CONN.commit()


def del_oldpost(id):
    """
    Removes an old post from the database with id
    """
    DB_CURSOR.execute('DELETE FROM oldposts WHERE id = ?', [id])
    DB_CONN.commit()


def is_oldpost(id):
    """
    Checks if old post with id is in the database
    """
    DB_CURSOR.execute('SELECT * FROM oldposts WHERE id = ?', [id])
    return DB_CURSOR.fetchone() is not None


def get_user(name):
    """
    Gets user data from the database from the username
    """
    DB_CURSOR.execute('SELECT * FROM users WHERE username = ?', [name])
    return DB_CURSOR.fetchone() is not None


def add_user(name, jobs=0, rep=0):
    """
    Adds a user to the database with the username, current jobs default 0, and rep default 0
    """
    DB_CURSOR.execute('INSERT INTO users VALUES(?, ?, ?)', [name, jobs, rep])
    DB_CONN.commit()


def update_user(name, jobs, rep):
    """
    Updates the jobs and reputation of a user with the username
    """
    DB_CURSOR.execute('UPDATE users SET jobs = ?, reputation = ? WHERE username = ?', [jobs, rep, name])
    DB_CONN.commit()


def del_user(name):
    """
    Removes the user from the database with the username
    """
    DB_CURSOR.execute('DELETE FROM users WHERE username = ?', [name])
    DB_CONN.commit()


def is_user(name):
    """
    Checks if user is in database with the username
    """
    DB_CURSOR.execute('SELECT * FROM oldposts WHERE username = ?', [name])
    return DB_CURSOR.fetchone() is not None