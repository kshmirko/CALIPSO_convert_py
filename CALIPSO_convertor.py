#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  7 11:20:51 2014

@author: Администратор
"""
import os
import argparse as arg
from glob import glob
import utils.convertor as c
import numpy as np

parser = arg.ArgumentParser(description='Convert CALIPSO hdf into compressed netCDF4 file.')
parser.add_argument('-i','--input-dir',type=str, default='./', help='Directory with hdf files.')
parser.add_argument('-o','--output-file', type=str, default=None, help='File with log.')
parser.add_argument('-u','--unlimited', type=bool, default=False, help='Time is unlimited.')
args = parser.parse_args()

FILES = np.array(glob(os.path.join(args.input_dir, '*.hdf')))
N_FILES = len(FILES)

DATES = np.array(c.get_date_from_fname_v(FILES))
UDATES = np.unique(DATES[0,:])

i=0
N_UDATES = len(UDATES)
while i<N_UDATES:
    idx = DATES[0,:] == UDATES[i]

    size = np.sum(DATES[1,idx])
    if args.unlimited:
        size=None
    
    print c.convert(FILES[idx], length=size)
    i+=1
