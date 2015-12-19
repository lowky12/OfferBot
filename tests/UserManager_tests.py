#!/usr/bin/env python
"""
User Manager Tests
"""
from nose.tools import *
import os
from OfferBot import UserManager, DBManager, OfferBot

Config = OfferBot.get_config()


def setup_module():
    """
    Setups the tables if not already
    """
    if not os.path.exists('offerbot.db'):
        DBManager.init_tables()


def test_usermanager_reputation():
    """
    Setups tests the user managers reputation function
    """
    test_user = {
        'username': 'test_user_rep',
        'jobs': 1,
        'reputation': int(Config.get("reputation", "TrustedLevel")) + 1
    }
    DBManager.add_user(test_user['username'], test_user['jobs'], test_user['reputation'])
    rep_level = UserManager.get_rep_level(test_user['username'])
    assert rep_level == "Very Trusted"
