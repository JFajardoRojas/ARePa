import os
import numpy as np
import sys
from R_extract import bbelems, bb2array


# Create a list of all cif files in "zeo_database" directory
zeo_list = os.listdir("zeo_database")
a=[]
b=[]
c=[]
alpha=[]
beta=[]
gamma=[]
elements=[]
coords=[]

# Iterate through each cif file to extract relevant data
for f in range(len(zeo_list)):
    cifname = zeo_list[f]
    elements_data = bbelems(cifname, "zeo_database")
    a_length = elements_data[0]
    b_length = elements_data[1]
    c_length = elements_data[2]
    alpha_value = elements_data[3]
    beta_value = elements_data[4]
    gamma_value = elements_data[5]
    elements_list = elements_data[6]
    

    a = np.append(a, a_length)
    b=np.append(b, b_length)
    c=np.append(c, c_length)
    alpha=np.append(alpha, alpha_value)
    beta=np.append(beta, beta_value)
    gamma=np.append(gamma, gamma_value)
    elements=np.append(elements, elements_list)
    elements=np.reshape(elements,(len(elements),1))
    
    #symmetries=np.append(symmetries, symmetries_list)
    #unit_cell=np.append(unit_cell)

    for i in range(len(elements_list)):
        coords_arr = bb2array(cifname, "zeo_database")
        coords_ele = coords_arr[i]

        coords=np.append(coords, coords_ele)
        coords=np.reshape(coords, (int(len(coords)/3), 3))
        coord_ejm = coords[0]


print(a, b, c, alpha, beta, gamma, elements, elements.shape)
print(coords, coords.shape)


