#!/usr/bin/env python
"""
Bot User Management
"""

import DBManager
from OfferBot import get_config

Config = get_config()


def get_rep_level(user):
    """
    Gets a text representation of the users rep
    Configurable boundary
    """
    user_db = DBManager.get_user(user)
    rep = user_db['reputation']
    if rep >= Config.get("reputation", "TrustedLevel"):
        return "Very Trusted"
    elif Config.get("reputation", "TrustedLevel") > rep >= Config.get("reputation", "NeutralLevel"):
        return "Trusted"
    elif Config.get("reputation", "NeutralLevel") > rep >= Config.get("reputation", "UntrustedLevel"):
        return "Neutral"
    elif Config.get("reputation", "UntrustedLevel") > rep >= Config.get("reputation", "ScammerLevel"):
        return "Untrusted"
    elif rep < Config.get("reputation", "ScammerLevel"):
        return "Scammer"