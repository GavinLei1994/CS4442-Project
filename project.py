#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 21:10:20 2022

@author: gavin
"""
#import keras
from keras.models import load_model

model = keras.models.load_model('model.h5')

model.save('model.h5')  # creates a HDF5 file 'my_model.h5'
del model  # deletes the existing model

# returns a compiled model
# identical to the previous one