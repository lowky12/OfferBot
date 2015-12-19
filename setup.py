"""
Setup for OfferBot
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': "OfferBot",
    'version': '1.0.0',
    'description': 'Reddit OfferBot',
    'author': 'lowky12',
    'author_email': 'lowky12@lowky12.com',
    'url': 'lowky12.com',
    'download_url': 'https://github.com/lowky12/OfferBot',
    'requires': ['praw', 'prawoauth2', 'nose'],
    'packages': ['OfferBot'],
    'scripts': [],
    'test_suite': 'nose.collector'
}

setup(**config)
