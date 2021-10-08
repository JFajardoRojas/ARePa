import os as os
import numpy as np
import datetime
from re import search

#input
atom2change = input("Which atom do you wanna change? (Atomic symbol): ")
atom_for = input("Which atom do you wanna place instead? (Atomic symbol): ")

#Reading Initial file
zeo_file = open("MTF.cif", "r")
z_file = zeo_file.read()
z_file_list = z_file.split()
z_file_leo = z_file.split('\n')

symmetries_in = z_file_leo.index('_symmetry_equiv_pos_as_xyz')   #Plus 1 to start directly in the symmetries
symmetries_fin = z_file_leo.index('_atom_site_label')            #Minus 2 to avoid the keyword loops
symmetries_len = (symmetries_fin-2) - (symmetries_in+1)

coord_in = z_file_list.index('_atom_site_fract_z') #Plus 1 to start in the first atom
coord_fin = len(z_file_list)
coord_len = (coord_fin) - (coord_in+1)

symmetries_list = []
coord_list = []


for line in z_file_leo:
    info_line = line.split()
    if '_cell_length_a' in line:
        a = info_line[1]
    if '_cell_length_b' in line:
        b = info_line[1]
    if '_cell_length_c' in line:
        c = info_line[1]
    if '_cell_angle_alpha' in line:
        alpha = info_line[1]
    if '_cell_angle_beta' in line:
        beta = info_line[1]
    if '_cell_angle_gamma' in line:
        gamma = info_line[1]
    if "_symmetry_space_group_name_H-M" in line:
        space_group = info_line[1] + info_line[2]
    if "_symmetry_Int_Tables_number" in line:
        int_table = info_line[1]
    if '_symmetry_cell_setting' in line:
        unit_cell = info_line[1]
    if '_symmetry_equiv_pos_as_xyz'in line:
        for l in range(int(symmetries_in+1), int(symmetries_fin-2), 1):
            symmetries_list.append(z_file_leo[l])


for line in z_file_list:
    if '_atom_site_fract_z'in line:
        for i in range(int(coord_in+1), int(coord_fin), 1):
            coord_list.append(z_file_list[i])
            coord_l = np.asarray(coord_list)

#coord = coord_list.split()




#Index identification
ind=[]
for item in range(len(z_file_list)):
    if z_file_list[item] == atom2change:   #Modify for User input
        ind.append(item)

print(ind) #Test for index identification //WORKING

#Atomic Modification on z_file_list
for i in range(len(ind)):
    z_file_list[ind[i]] = atom_for 

    #Modify for User input //atom_to name of the input

#print(z_file_list) #Test for Si replace for AL // WORKING

#print(z_file)


#data_cif = []
    if not os.path.exists("changed_structures"):
        os.makedirs("changed_structures")
    for atom2 in range(len(ind)):
        file_title = "File created by Fernando Fajardo-Rojas's code on " + str(datetime.datetime.now())
        data_cif_name = "MTF_"+atom2change+'_'+str(atom2+1)+".cif"
        #data_cif.append(data_cif_name)
        #print(data_cif) #Test name modification through counting //WORKING

        with open("changed_structures/" + data_cif_name, 'w') as cif:

            cif.write('data_'+ data_cif_name +'\n')
            cif.write(file_title +'\n')
            cif.write('########################################################'+'\n')
            cif.write('#                                                      #'+'\n')
            cif.write('#    Code developed in the CoDeMatE LAB                #'+'\n')
            cif.write('#    Chemical & Biological Engineering Department      #'+'\n')
            cif.write('#    Colorado School of Mines                          #'+'\n')
            cif.write('#    Email: jfajardorojas@mines.edu                    #'+'\n')
            cif.write('#                                                      #'+'\n')
            cif.write('########################################################'+'\n')
            cif.write(' '+'\n')
            cif.write('_audit_creation_method               '+ 'JFRcode' +'\n')
            cif.write('_cell_length_a                       '+ a +'\n')
            cif.write('_cell_length_b                       '+ b +'\n')
            cif.write('_cell_length_c                       '+ c +'\n')
            cif.write('_cell_angle_alpha                    '+ alpha +'\n')
            cif.write('_cell_angle_beta                     '+ beta +'\n')
            cif.write('_cell_angle_gamma                    '+ gamma +'\n')
            cif.write(' '+'\n')
            cif.write('__symmetry_space_group_name_H-M      '+ space_group +'\n')
            cif.write('_symmetry_Int_Tables_number          '+ int_table +'\n')
            cif.write('_symmetry_cell_setting               '+ unit_cell +'\n')
            cif.write(' '+'\n')
            cif.write('loop_                                 '+'\n')
            cif.write(' _symmetry_equiv_pos_as_xyz           '+'\n')
            
            for sym in range(int(symmetries_len)):
                cif.write(symmetries_list[sym]               +'\n')

            cif.write(' '+'\n')
            cif.write('loop_                                 '+'\n')
            cif.write(' _atom_site_label                     '+'\n')
            cif.write(' _atom_site_type_symbol               '+'\n')
            cif.write(' _atom_site_fract_x                   '+'\n')
            cif.write(' _atom_site_fract_y                   '+'\n')
            cif.write(' _atom_site_fract_z                   '+'\n')

            for coo in range(int(coord_len)):
                cif.write(coord_l[coo]       +'\n')



            #for item in range(len(z_file_list)):

                #if z_file_list[item] == z_file_list[ind[atom2]]:
                    #cif.write(z_file_list[item-1]+' '+z+'    '+z_file_list[item+1])

                #else:
                 #   for j in range(len(coord_list)):
                  #      cif.write(coord_list[j]+ '\n')           

                #else:
                
                    #cif.write("  "+z_file_list[int(coord_in)+j]+" "+'\n') 
                        #"+coord_list[j+1]+"  "+coord_list[j+2]+"  "+coord_list[j+3]+"  "+coord_list[j+4]+"   "+                         '\n')



                #if 'Si' == str(coord_list[j]):
                #if coord_list[coord_list.index(j)] == ind[atom2]:
                    #cif.write('Aqui ponemos el que queremos  '+'\n')

                #else:
                    #cif.write('Las otras coordenadas         '+'\n')


#print(z_file_list)
print (symmetries_list)

#print(coord)

print (coord_l)
#print (coord)














