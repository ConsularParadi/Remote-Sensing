#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
__author__ -> Rishi Sharma
__email__ -> consularparadi@gmail.com
__status__ -> Prototype
'''
# %%
from radiant_mlhub import Dataset
ds = Dataset.fetch('nasa_rwanda_field_boundary_competition')
ds.download()

#%%
import rasterio as rio
