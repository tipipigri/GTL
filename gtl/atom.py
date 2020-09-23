# -*- coding: utf-8 -*-
"""
Atom are the most small piece of the glyph/character.

Atom have a main `draw()` method that render the piece of the glyph in the definitive rendered form.

:copyright: © 2020 Tipipigri.
:license: Apache2, see LICENSE for more details.
"""
from typing import List

from gtl import transformation


class Atom:
    """
    Atom implementation class.
    """

    def __init__(self, shape: str):
        self.shape = shape

    @property
    def transformations(self) -> List[transformation.Transformation]:
        """
        List of the transformations, None if not added.
        """
        return self.transformations

    @transformations.setter
    def transformations(self, values: List[transformation.Transformation]) -> None:
        for __ in values:
            if not isinstance(__, transformation.Transformation):
                raise ValueError(f"The transformation {__} is invalid")

        self.transformations = values

    def add_transformation(self, element: transformation.Transformation) -> None:
        """
        Add a new transformation to be applied at draw time.
        """
        if not self.transformations:
            self.transformations = []

        self.transformations.append(element)

    def draw(self) -> None:
        """
        Render the small atom piece into the whole glyph.
        """
