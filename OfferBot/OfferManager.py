#!/usr/bin/env python
"""
Bot Offer Management
"""
import praw
import OfferBot
import DBManager
import UserManager
from string import Template

config = OfferBot.get_config()


def on_trigger(submit_id, submit_author, comment):
    """
    On Trigger of bot
    :param submit_id:
    :param submit_author:
    :param comment:
    """
    cid = comment.id
    try:
        cauthor = comment.author.name
    except AttributeError:
        return

    cbody = comment.body.lower()
    message = cbody.split(OfferBot.TRIGGER)[1].split("\n")[0]

    if "accept" in message:
        # UserManager.plus_job(cauthor)
        reply = get_response_accept(cauthor, submit_author)
    elif "plusrep" in message:
        # UserManager.plus_rep(cauthor)
        reply = get_response_plus_rep(cauthor, submit_author)
    elif "minusrep" in message:
        reason = message.split("minusrep")[1]
        reply = get_response_minus_rep(cauthor, submit_author, reason)
    elif "done" in message:
        reply = get_response_done(cauthor, submit_author)
    else:
        reply = get_response_user(cauthor)

    if UserManager.get_rep_level(DBManager.get_user(cauthor)['reputation']) == "Scammer":
        OfferBot.bot_reply(comment, get_response_scammer(cauthor))

    OfferBot.bot_reply(comment, reply)


def get_response_user(user):
    """
    OfferBot Tests
    :param user:
    """
    user_info = DBManager.get_user(user)
    rep = user_info['reputation']
    rep_string = UserManager.get_rep_level(rep)

    response = Template(config.get("offer", "reply"))
    response = response.substitute(username=user, rep=rep_string, repno=rep, jobs=user_info['jobs'])

    return response


def get_response_accept(user, op):
    """
    OfferBot Tests
    :param op:
    :param user:
    """
    response = Template(config.get("offer", "accept_reply"))
    response = response.substitute(username=user, username2=op)

    return response


def get_response_done(user, op):
    """
    OfferBot Tests
    :param op:
    :param user:
    """
    response = Template(config.get("offer", 'completed_reply'))
    response = response.substitute(username=user, username2=op)

    return response


def get_response_scammer(user):
    """
    OfferBot Tests
    :param user:
    """
    response = Template(config.get("offer", "scammer_rep_reply"))
    response = response.substitute(username=user)

    return response


def get_response_plus_rep(user, op):
    """
    OfferBot Tests
    :param user:
    """
    user_info = DBManager.get_user(user)
    rep = user_info['reputation']
    rep_string = UserManager.get_rep_level(rep)

    response = Template(config.get("offer", "plus_rep_reply"))
    response = response.substitute(username=user, username2=op, rep=rep_string, repno=rep)

    return response


def get_response_minus_rep(user, op, reason):
    """
    OfferBot Tests
    :param user:
    :param reason:
    """
    user_info = DBManager.get_user(user)
    rep = user_info['reputation']
    rep_string = UserManager.get_rep_level(rep)

    response = Template(config.get("offer", "minus_rep_reply"))
    response = response.substitute(username=user, username2=op, rep=rep_string, repno=rep, reason=reason)

    return response
