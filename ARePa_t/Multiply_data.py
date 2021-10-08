import os
import numpy as np
import sys
import math
import datetime as datetime
from R_extract import bbelems, bb2array
from arepa import replicate

np.set_printoptions(threshold=sys.maxsize)

# Create a list of all cif files in "zeo_database" directory
zeo_list = os.listdir("zeo_database")
#print(zeo_list)
#print(len(zeo_list))

# Iterate through each cif file to extract relevant data

#DEF FUNCTION TO PRINT

for f in range(len(zeo_list)):
    cifname = zeo_list[f]
    #print(cifname)                  #This provides de list of data names

    if cifname == zeo_list[f]:

        elements_data = bbelems(cifname, "zeo_database")
        coords_data = bb2array(cifname, "zeo_database")
        a_length = elements_data[0]
        b_length = elements_data[1]
        c_length = elements_data[2]
        alpha_value = elements_data[3]
        beta_value = elements_data[4]
        gamma_value = elements_data[5]
        elements_list = elements_data[6]
        types_list = elements_data[7]
        space_group = str(elements_data[8])
        space_g = str(space_group).replace("['","").replace("']","").replace('[','').replace(']','').replace("' '"," ").replace("'  '"," ").replace("'","").replace('"',"").replace(",","").replace(" ","")
        int_table = elements_data[9]
        coordens = coords_data[0:len(elements_list)]
        coordens = np.reshape(coordens, (int(len(coordens)),3))

        print(cifname)
        print(coordens)
    
    #print(coordens, type(coordens), coordens.shape)
    #print(cifname)
    #print(elements_list, type(elements_list), len(elements_list))
    #print(types_list, type(types_list), len(types_list))
        a_each = a_length 
    #print(a_each)
        b_each = b_length
    #print(b_each)
        c_each = c_length
    #print(c_each)
        alpha = alpha_value
    #print(alpha)
        beta = beta_value
    #print(beta)
        gamma = gamma_value
    #print(gamma)

        #Metric tensor definition
        a_sq = float(a_each)
        #a_s = str(a_sq)
        b_sq = float(b_each)
        #b_s = str(b_sq)
        c_sq = float(c_each)
        #c_s = str(c_sq)
        a_angle = float(alpha)
        b_angle = float(beta)
        g_angle = float(gamma)


        a_1 = a_sq ** 2
        a_2 = a_sq * b_sq * (math.cos(g_angle * math.pi / 180))
        a_3 = a_sq * c_sq * (math.cos(b_angle * math.pi / 180))
        b_1 = b_sq * a_sq * (math.cos(a_angle * math.pi / 180))
        b_2 = b_sq ** 2
        b_3 = b_sq * c_sq * (math.cos(a_angle * math.pi / 180))
        c_1 = c_sq * a_sq * (math.cos(b_angle * math.pi / 180))
        c_2 = b_sq * c_sq * (math.cos(a_angle * math.pi / 180))
        c_3 = c_sq ** 2

        #print(a_sq, type(a_sq), a_s, type(a_s))   math.sqrt(np.linalg.det(

        unit_c = np.asarray(([a_1, a_2, a_3],[b_1, b_2, b_3],[c_1, c_2, c_3]))

        unit_cell_sq = np.linalg.det(unit_c)
        
        unit_cell = math.sqrt(unit_cell_sq)
        unit_cell = str(unit_cell)

        #print(cifname, a_each, b_each, c_each, alpha, beta, gamma, coordens, elements_list, types_list)

        ele_coords = coordens
        elements = elements_list
        types = types_list

        na = 3 #input('Number of replications on "a" direction: ')
        nb = 3 #input('Number of replications on "b" direction: ')
        nc = 3 #input('Number of replications on "c" direction: ')

        #New Unit Cell Dimmensions

        a_le = a_sq * na
        a_le = str(a_le)
        b_le = b_sq * nb
        b_le = str(b_le)
        c_le = c_sq * nc
        c_le = str(c_le)

        new_cif = replicate (na, nb, nc, elements, types, ele_coords)
        new_ele = new_cif[1]
        new_ele_print = str(new_ele).replace("['","").replace("']","").replace('[','').replace(']','')
        new_coord = new_cif[2]
        new_coord_print = str(new_coord).replace("[","").replace("]","")
        new_ty = new_cif[0]
        new_ty_print = str(new_ty).replace("['","").replace("']","").replace('[','').replace(']','')
        #print(cifname)
        #print(new_cif[2])

        coord_2_calc = np.concatenate((new_ele, new_coord), axis=1)
        coord_2_calc_tot = np. concatenate((new_ty, coord_2_calc), axis=1)
        coord_2_print = str(coord_2_calc_tot).replace("['","").replace("']","").replace('[','').replace(']','').replace("' '"," ").replace("'  '"," "). replace("'","")
        print(coord_2_print)

        if not os.path.exists("new_cif_files_replica"):
            os.makedirs("new_cif_files_replica")
        file_title = "File created by Fernando Fajardo-Rojas's code on " + str(datetime.datetime.now())
        with open("new_cif_files_replica/"+"a_"+str(na)+"_b_"+str(nb)+"_c_"+str(nc)+"_"+cifname, 'w') as cif:

            cif.write('data_'+ cifname +'\n')
            cif.write(file_title +'\n')
            cif.write(' '+'\n')
            cif.write('###################################################################################'+'\n')
            cif.write('#                                                                                 #'+'\n')
            cif.write('#    Code developed in the CoDeMatE LAB                ######  ######  ##   ##    #'+'\n')
            cif.write('#    Chemical & Biological Engineering Department      #       #       # # # #    #'+'\n')
            cif.write('#    Colorado School of Mines                          #       ######  #  #  #    #'+'\n')
            cif.write('#    Email: jfajardorojas@mines.edu                    #            #  #     #    #'+'\n')
            cif.write('#                                                      ######  ######  #     #    #'+'\n')
            cif.write('#                                                                                 #'+'\n')
            cif.write('###################################################################################'+'\n')
            cif.write(' '+'\n')
            cif.write('_audit_creation_method               '+ 'JFRcode' +'\n')
            cif.write('_cell_length_a                       '+ a_le +'\n')
            cif.write('_cell_length_b                       '+ b_le +'\n')
            cif.write('_cell_length_c                       '+ c_le +'\n')
            cif.write('_cell_angle_alpha                    '+ alpha +'\n')
            cif.write('_cell_angle_beta                     '+ beta +'\n')
            cif.write('_cell_angle_gamma                    '+ gamma +'\n')
            cif.write('_cell_volume                         '+unit_cell+'\n')
            cif.write(' '+'\n')
            cif.write('_symmetry_space_group_name_H-M      '+ space_g +'\n')
            cif.write('_symmetry_Int_Tables_number         '+ int_table +'\n')

            cif.write(' '+'\n')
            cif.write('loop_                                 '+'\n')

            cif.write(' _atom_site_label                     '+'\n')
            cif.write(' _atom_site_type_symbol               '+'\n')
            cif.write(' _atom_site_fract_x                   '+'\n')
            cif.write(' _atom_site_fract_y                   '+'\n')
            cif.write(' _atom_site_fract_z                   '+'\n')
            cif.write(coord_2_print)

