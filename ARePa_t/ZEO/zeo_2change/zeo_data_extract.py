import os
import numpy as np
import sys
from R_extract import bbelems, bb2array


# Create a list of all cif files in "zeo_database" directory
zeo_list = os.listdir("zeo_database")
#np.set_printoptions(threshold=sys.maxint)
a=[]
b=[]
c=[]
alpha=[]
beta=[]
gamma=[]
cell=[]
unit_cell=[]
#symmetries=[]

# Iterate through each cif file to extract relevant data
for cif in zeo_list:
    cif_now = open("zeo_database/"+cif, "r")

    cif_file = cif_now.read()
    cf = cif_file.split()               #To read as a list of strings
    cf_leo = cif_file.split('\n')       #To read as a arrange of lines and look into the lines

    # Read cif name
    cif_name = cf[0]

    # Read unit cell parameters
    # Cell parameters
    a_look = cf.index("_cell_length_a")
    a_ind = int(a_look +1)
    b_look = cf.index("_cell_length_b")
    b_ind = int(b_look +1)
    c_look = cf.index("_cell_length_c")
    c_ind = int(c_look +1)
    alpha_look = cf.index("_cell_angle_alpha")
    alpha_ind = int(alpha_look+1)
    beta_look = cf.index("_cell_angle_beta")
    beta_ind = int(beta_look+1)
    gamma_look = cf.index("_cell_angle_gamma")
    gamma_ind = int(gamma_look+1)
    #cell_volume_look = cf.index("_cell_volume")
    #cell_volume_ind = int(cell_volume_look+1)

    # Cell definition

    a_length = (cf[a_ind]) 
    b_length = (cf[b_ind]) 
    c_length = (cf[c_ind]) 
    alpha_value = (cf[alpha_ind])
    beta_value = (cf[beta_ind])
    gamma_value = (cf[gamma_ind])
    #cell_volume = float(cf[cell_volume_ind])
    unit_cell = np.matrix([[a_length,0,0],[0,b_length,0],[0,0,c_length]])

    #Symmetries

    symmetries_in = cf_leo.index('_symmetry_equiv_pos_as_xyz')   #Plus 1 to start directly in the symmetries
    symmetries_fin = cf_leo.index('_atom_site_label')            #Minus 2 to avoid the keyword loops
    symmetries_len = (symmetries_fin-2) - (symmetries_in+1)
    symmetries_list = []

    for line in cf_leo:
        info_line = line.split()
        if "_cell_volume" in line:
            cell_volume = info_line[1]
        else:
            cell_volume = []
        if *"_symmetry_space_group_name_H-M" in line:
            space_group = info_line[1]
        if *"_symmetry_Int_Tables_number" in line:
            int_table = info_line[1]
        if *'_symmetry_cell_setting' in line:
            type_cell = info_line[1]
        #if '_symmetry_equiv_pos_as_xyz'in line:
            #for l in range(int(symmetries_in+1), int(symmetries_fin-2), 1):
                #symmetries_list.append(cf_leo[l])


    a = np.append(a, a_length)
    b=np.append(b, b_length)
    c=np.append(c, c_length)
    alpha=np.append(alpha, alpha_value)
    beta=np.append(beta, beta_value)
    gamma=np.append(gamma, gamma_value)
    cell=np.append(cell, cell_volume)
    #symmetries=np.append(symmetries, symmetries_list)
    #unit_cell=np.append(unit_cell)

print(a, b, c, alpha, beta, gamma)


