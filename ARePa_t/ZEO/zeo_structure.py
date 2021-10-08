import os as os
import numpy as np

#Create the list of zeolites from a directory zeo_change
zeo_list = os.listdir("zeo_2change")

for zeolite in zeo_list:
    zeolite_now = open("zeo_2change/"+zeolite, "r")
    zeolite_file = zeolite_now.read()
    zf = zeolite_file.split()