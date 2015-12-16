#!/usr/bin/env python
"""
Database Manager Tests
"""
from nose.tools import *
import os
import os.path
from OfferBot import DBManager


def setup_module(module):
    if os.path.exists('offerbot.db'):
        os.rename('offerbot.db', 'offerbot.db.bak')

    DBManager.init_tables()


def teardown_module(module):
    if os.path.exists('offerbot.db'):
        os.remove('offerbot.db')

    if os.path.exists('offerbot.db.bak'):
        os.rename('offerbot.db.bak', 'offerbot.db')


def test_dbmanager_oldposts():
    test_id = "0"

    DBManager.add_oldpost(test_id)
    assert DBManager.is_oldpost(test_id) is True

    DBManager.del_oldpost(test_id)
    assert DBManager.is_oldpost(test_id) is False


def test_dbmanager_users():
    test_user = {
        'username': 'test_user',
        'jobs': 0,
        'reputation': 10
    }

    DBManager.add_user(test_user['username'], test_user['jobs'], test_user['reputation'])
    assert DBManager.is_user(test_user['username'])

    get_test_user = DBManager.get_user(test_user['username'])
    assert get_test_user['reputation'] == test_user['reputation']

    DBManager.update_user(test_user['username'], test_user['jobs'], 20)
    get_test_user = DBManager.get_user(test_user['username'])
    assert get_test_user['reputation'] == 20
