#!/usr/bin/env python
"""
Bot Core Functionality
"""
import praw
import ConfigParser

import OfferManager
import UserManager

USER_AGENT = 'python:OfferBot:v1.0.0 (by /u/lowky12)'
REDDIT_CLIENT = praw.Reddit(user_agent=USER_AGENT)

Config = ConfigParser.ConfigParser()


def get_config():
    """
    Gets the config option.
    Reads ini if not read.
    """
    if not Config.sections():
        Config.read("../config.ini")
    return Config


# Main Function
if __name__ == '__main__':
    pass