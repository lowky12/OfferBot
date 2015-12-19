#!/usr/bin/env python
"""
Package for OfferBot Tests
"""
import os

if os.path.exists('offerbot.db'):
    os.rename('offerbot.db', 'offerbot.db.bak')


def teardown_package():
    """
    Clean up after Tests
    """
    from OfferBot import DBManager
    DBManager.DB_CONN.close()

    if os.path.exists('offerbot.db'):
        os.remove('offerbot.db')

    if os.path.exists('offerbot.db.bak'):
        os.rename('offerbot.db.bak', 'offerbot.db')
