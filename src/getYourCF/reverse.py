"""Module to implement the command to chekc if a FC is valid"""

from getmycf.runner import Extractor


def validate(code: str):
    assert len(code)==16, "The length of the FC must be 16"

    