#!/usr/bin/env python
"""
Database Manager Tests
"""
from nose.tools import *
import os
from OfferBot import DBManager


def test_dbmanager_init_tables():
    """
    Tests the creation of the sqlite tables
    """
    DBManager.init_tables()
    assert os.path.exists('offerbot.db')


def test_dbmanager_oldposts():
    """
    Tests the oldpost section of the database
    """
    test_id = "0"

    if DBManager.is_oldpost(test_id):
        DBManager.del_oldpost(test_id)

    DBManager.add_oldpost(test_id)
    assert DBManager.is_oldpost(test_id)

    DBManager.del_oldpost(test_id)
    assert DBManager.is_oldpost(test_id) is False


def test_dbmanager_users():
    """
    Tests the user section of the database
    """
    test_user = {
        'username': 'test_user',
        'jobs': 0,
        'reputation': 10
    }

    if DBManager.is_user(test_user['username']):
        DBManager.del_user(test_user['username'])

    DBManager.add_user(test_user['username'], test_user['jobs'], test_user['reputation'])
    assert DBManager.is_user(test_user['username'])

    get_test_user = DBManager.get_user(test_user['username'])
    assert get_test_user['reputation'] == test_user['reputation']

    DBManager.update_user(test_user['username'], 20, test_user['reputation'])
    get_test_user = DBManager.get_user(test_user['username'])
    assert get_test_user['jobs'] == 20

    DBManager.del_user(test_user['username'])
    assert DBManager.is_user(test_user['username']) is False
