import numpy as np
import pandas as pd
import os
from os import listdir
from os.path import isfile, join


def read_reports(p):
    print(f"Reading KidTrax/{p}")
    return pd.read_excel(os.path.abspath(os.path.join('KidTrax', p)))


filename = 'Valentine_ProgramOperations_Mar2022'

out = os.path.abspath(os.path.join(os.getcwd(), 'KidTrax'))
only_files = [f for f in listdir(out) if isfile(join(out, f))]

kid_trax_reports = [read_reports(p) for p in only_files if p != '.DS_Store']

for r in kid_trax_reports:
    print(r)