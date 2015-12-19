#!/usr/bin/env python
"""
Bot Core Functionality
"""
import praw
import time
from prawoauth2 import PrawOAuth2Mini
import ConfigParser

import DBManager
import OfferManager

USER_AGENT = 'python:OfferHelper:v1.0.0 (by /u/lowky12)'
REDDIT_CLIENT = praw.Reddit(user_agent=USER_AGENT)
SCOPES = []

config = ConfigParser.ConfigParser()
MAX_POSTS = config.getint('config', 'max_posts')
TRIGGER = config.get("offer", "trigger")


def get_config():
    """
    Gets the config option.
    Reads ini if not read.
    """
    if not config.sections():
        config.read("config.ini")
    return config


def bot_oauth():
    """
    Sets up oauth
    """
    if not config.get('oauth', 'reddit_refresh_token'):
        print("Run OfferBotSetup.py to get OAuth tokens")
        exit()

    oauth_server = PrawOAuth2Mini(REDDIT_CLIENT,
                                  app_key=config.get('oauth', 'reddit_app_key'),
                                  app_secret=config.get('oauth', 'reddit_app_secret'),
                                  access_token=config.get('oauth', 'reddit_access_token'),
                                  scopes=SCOPES,
                                  refresh_token=config.get('oauth', 'reddit_refresh_token'))
    return oauth_server


def bot_main(oauth_helper):
    """
    Main bot function
    :param oauth_helper:
    """
    oauth_helper.refresh()
    subreddit = REDDIT_CLIENT.get_subreddit(config.get('config', 'subreddit'))
    submissions = list(subreddit.get_new(limit=MAX_POSTS))
    for submission in submissions:
        sid = submission.id
        try:
            sauthor = submission.author.name
        except AttributeError:
            continue
        comments = submission.get_comments(limit=MAX_POSTS)
        comments.reverse()
        for comments in comments:
            bot_post_logic(sid, sauthor, comments)


def bot_post_logic(sid, sauthor, comment):
    """
    Logic for each post
    :param sid:
    :param sauthor:
    :param comment:
    :return:
    """
    cid = comment.id
    try:
        cauthor = comment.author.name
    except AttributeError:
        return

    if cauthor.lower() == REDDIT_CLIENT.user.name.lower():
        return

    if DBManager.is_oldpost(cid):
        return
    DBManager.add_oldpost(cid)

    cbody = comment.body.lower()
    if TRIGGER.lower() in cbody:
        OfferManager.on_trigger(sid, sauthor, comment)


def bot_reply(post, reply):
    """
    Reply's to post with reply adding configurable footer
    :param post:
    :param reply:
    """
    reply = reply + config.get('config', 'bot_footer')
    try:
        post.reply(reply)
    except praw.requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            print('403 FORBIDDEN - is the bot banned from %s?' % post.subreddit.display_name)




# Main Function
if __name__ == '__main__':
    oauth = bot_oauth()

    while True:
        try:
            bot_main(oauth)
        except praw.errors.OAuthInvalidToken:
            oauth.refresh()
        time.sleep(30)
