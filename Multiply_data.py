import os
import numpy as np
import sys
from R_extract import bbelems, bb2array
from arepa import replicate

np.set_printoptions(threshold=sys.maxsize)


# Create a list of all cif files in "zeo_database" directory
zeo_list = os.listdir("zeo_database")
a=[]
b=[]
c=[]
alpha=[]
beta=[]
gamma=[]
elements=[]
types = []
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
    types_list = elements_data[7]

    a = np.append(a, a_length)
    b=np.append(b, b_length)
    c=np.append(c, c_length)
    alpha=np.append(alpha, alpha_value)
    beta=np.append(beta, beta_value)
    gamma=np.append(gamma, gamma_value)
    elements=np.append(elements, elements_list)
    elements=np.reshape(elements,(len(elements),1))
    types=np.append(types, types_list)
    types=np.reshape(types,(len(types),1))
    
    #symmetries=np.append(symmetries, symmetries_list)
    #unit_cell=np.append(unit_cell)

    for i in range(len(elements_list)):
        coords_arr = bb2array(cifname, "zeo_database")
        coords_ele = coords_arr[i]

        coords=np.append(coords, coords_ele)
        coords=np.reshape(coords, (int(len(coords)/3), 3))
        #coord_ejm = coords[0]

print(a, b, c, alpha, beta, gamma)
#print(coords, coords.shape)

ele_coords = coords
elements = elements
types = types

new_cif = replicate (4, 4, 4, elements, types, ele_coords)
new_ele = new_cif[1]
new_ele_print = str(new_ele).replace("['","").replace("']","").replace('[','').replace(']','')
new_coord = new_cif[2]
new_coord_print = str(new_coord).replace("[","").replace("]","")
new_ty = new_cif[0]
new_ty_print = str(new_ty).replace("['","").replace("']","").replace('[','').replace(']','')

#print(new_cif)
print(new_ty_print)
print(new_ele_print)
print(new_coord_print)


coord_2_calc = np.concatenate((new_ele, new_coord), axis=1)
coord_2_calc_comp = np.concatenate((new_ty, coord_2_calc), axis=1)
coord_2_print = str(coord_2_calc_comp).replace("['","").replace("']","").replace('[','').replace(']','').replace("' '"," ").replace("'  '"," "). replace("'","")
print(coord_2_print)

if not os.path.exists("new_ele_n_coord"):
    os.makedirs("new_ele_n_coord")
    with open("new_ele_n_coord/"+"new_ele.py", 'w') as ele:
        ele.write('Elements Replciated      ' + '\n' )
        ele.write(str(new_ele_print))
    
    with open("new_ele_n_coord/"+"new_coord.py", 'w') as coo:
        coo.write(' Coords Replicated    ' + '\n' )
        coo.write(str(new_coord_print))

    with open("new_ele_n_coord/"+"new_ele_n_coord.py", 'w') as nec:
        nec.write(' elements'+" "+"x"+"y"+"z" + '\n' )
        nec.write(str(coord_2_print))
