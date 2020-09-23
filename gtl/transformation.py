# -*- coding: utf-8 -*-
"""
Transformations are the functions applied to the bit at draw time. As per now they should be idempotent.

:copyright: © 2020 Tipipigri.
:license: Apache2, see LICENSE for more details.
"""
from gtl import atom


class Transformation:
    """
    Transformation object implementation.
    """

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def transform(piece: atom.Atom) -> atom.Atom:
        """
        Implement the main functions application.
        """
        return piece

    @staticmethod
    def apply(piece: atom.Atom) -> None:
        """
        Execute the transformation on the bit.
        """
        print(piece)
