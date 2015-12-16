#!/usr/bin/env python2
"""
Bot Core Functionality
"""
import time

import praw
from prawoauth2 import PrawOAuth2Server, PrawOAuth2Mini

import OfferManager
import UserManager

USER_AGENT = 'python:OfferBot:v1.0.0 (by /u/lowky12)'
REDDIT_CLIENT = praw.Reddit(user_agent=USER_AGENT)

# Main Function
if __name__ == '__main__':
	pass