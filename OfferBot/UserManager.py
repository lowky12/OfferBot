#!/usr/bin/env python
"""
Bot User Management
"""

import DBManager
from OfferBot import get_config

Config = get_config()


def plus_job(user):
    """
    Adds a job to a user
    :param user:
    """
    userdb = DBManager.get_user(user)
    new_jobs = userdb['jobs'] + 1
    DBManager.update_user(user, new_jobs, userdb['reputation'])


def minus_job(user):
    """
    Removes a job to a user
    :param user:
    """
    userdb = DBManager.get_user(user)
    new_jobs = userdb['jobs'] - 1
    DBManager.update_user(user, new_jobs, userdb['reputation'])


def plus_rep(user, increase=1):
    """
    Adds rep to a user
    :param increase:
    :param user:
    """
    userdb = DBManager.get_user(user)
    new_rep = userdb['reputation'] + increase
    DBManager.update_user(user, userdb['jobs'], new_rep)


def minus_rep(user, decrease=1):
    """
    Removes rep from a user
    :param decrease:
    :param user:
    """
    userdb = DBManager.get_user(user)
    new_rep = userdb['reputation'] - decrease
    DBManager.update_user(user, userdb['jobs'], new_rep)


def get_rep_level(rep):
    """
    Gets a text representation of the users rep
    Configurable boundary
    :param rep:
    """
    trusted_level = Config.getint("reputation", "TrustedLevel")
    neutral_level = Config.getint("reputation", "NeutralLevel")
    untrusted_level = Config.getint("reputation", "UntrustedLevel")
    scammer_level = Config.getint("reputation", "ScammerLevel")

    if rep >= trusted_level:
        return "Very Trusted"
    elif trusted_level > rep >= neutral_level:
        return "Trusted"
    elif neutral_level > rep >= untrusted_level:
        return "Neutral"
    elif untrusted_level > rep >= scammer_level:
        return "Untrusted"
    elif rep < scammer_level:
        return "Scammer"
