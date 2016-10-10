#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function checks the username and password, with max. no of attempts."""

import getpass
import authentication


def login(username, maxattempts=3):
    """A function checking the login username and password, with max attempts.

    Args:
        username (str): A string representing the username.
        maxattempts (int, optional): an integer stating the max. number of
                                     prompted attempts before the function
                                     returns false. Default: 3.

    Returns:
        bool: True if the username and password are correct, else False.

    Examples:
        >>> login('mike', 2)
        Please enter your password:
        True

        >>> login('violet')
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False
    """
    authenticated = False
    while maxattempts > 0:
        password = getpass.getpass('Please enter your password:')
        authenticated = authentication.authenticate(username, password)
        if authenticated is False:
            maxattempts -= 1
            attempts = 'Incorrect username or password, You have ' + \
                       str(maxattempts) + ' attempts left.'
            print attempts
            if maxattempts == 0:
                return authenticated
        elif authenticated is True:
            return authenticated
