#!/usr/bin/env python
"""
User Manager Tests
"""
from nose.tools import *
from OfferBot import UserManager, DBManager, OfferBot

Config = OfferBot.get_config()


def test_usermanager_reputation():
    test_user = {
        'username': 'test_user',
        'jobs': 0,
        'reputation': Config.get("reputation", "Trusted") + 1
    }
    DBManager.add_user(test_user['username'], test_user['jobs'], test_user['reputation'])
    assert UserManager.get_rep_level(test_user['username']) == "Very Trusted"

