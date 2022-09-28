"""Module to implement the command to chekc if a FC is valid"""

from getYourCF.runner import Extractor as Extractor
from getYourCF import exception
import pytest
import os
import pathlib
import numpy as np


def validate(code: str):
    assert len(code)==16, "The length of the FC must be 16"

    date = code[8:10]
    month = date.pop(0)

    assert month in exception.month_to_number.items(), "Month not valid"
    
    rlim = 30
    if month in ['A', 'C', 'E', 'L', 'M', 'R', 'T']:
        rlim = 31
    elif month == 'B':
        rlim = 28

    assert 1<=int(date)<=rlim, "Day not valid"

    data_dir = os.path.join(pathlib.Path(__file__).parent.parent.parent, 'data')
    ita = np.loadtxt(os.path.join(data_dir, "Codici_ITA.csv"), delimiter=";", dtype=str)
    ext = np.loadtxt(os.path.join(data_dir, "Codici_EXT.csv"), delimiter=";", dtype=str)
    
    d = { k.upper():v for k,v in ita}
    d.update ({ k.upper():v for k,v in ext})

    assert code[-5:-1] in d.keys()

    extractor = Extractor(code[:-1])
    assert extractor.get_control_digit()==code[-1]


