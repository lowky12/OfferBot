#!/usr/bin/env python
"""
Bot Setup
"""
from prawoauth2 import PrawOAuth2Server

from OfferBot import USER_AGENT, REDDIT_CLIENT, get_config


SCOPES = []


def setup_bot():
    """
    Sets up the bot by setting the refresh_token and the refresh_token through oauth
    """
    config = get_config()

    app_key = config.get("oauth", "reddit_app_key")
    app_secret = config.get("oauth", "reddit_app_secret")

    oauth_server = PrawOAuth2Server(REDDIT_CLIENT, app_key, app_secret, state=USER_AGENT, scopes=SCOPES)
    oauth_server.start()

    tokens = oauth_server.get_access_codes()
    config.set("oauth", "reddit_refresh_token", tokens['refresh_token'])
    config.set("oauth", "reddit_access_token", tokens['access_token'])

    cfgfile = open("../config.ini", 'w')
    config.write(cfgfile)
    cfgfile.close()

# Main Function
if __name__ == '__main__':
    pass
