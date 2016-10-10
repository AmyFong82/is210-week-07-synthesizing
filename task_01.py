#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A function returns a list of matchups between players."""


def get_matches(players):
    """A function returns a list of matchups between players.

    Args:
        players (list): a list of player names.

    Returns:
        list: a list of tuples of matchups between players.

    Examples:
        >>> get_matches(['James', 'Jesse', 'Jennifer'])
        [('James', 'Jennifer'), ('Jesse', 'James'), ('Jennifer', 'Jesse')]

        >>> get_matches(['Harry', 'Howard', 'Hugh', 'Hay'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Harry', 'Hay'), ('Howard',
        'Hugh'), ('Howard', 'Hay'), ('Hugh', 'Hay')]
    """
    newlist = []
    for player1 in players:
        for myind, player2 in enumerate(players):
            if players.index(player1) < myind:
                pair = player1, player2
                newlist.append(pair)
    return newlist
