#AREPA - Automatic RElication of PAtterns

import numpy as np

def replicate (na, nb, nc, elements, types, ele_coord):

    exp_elements = elements
    exp_types = types
    exp_coord = ele_coord
    ele_cord_cst = ele_coord
    elementos = []
    tipos = []

    #print(ele_coord)

    for x in range(int(na)):
        for y in range(len(exp_elements)):
            exp_elements[y] = (elements[y])
            exp_types[y] = (types[y])
        elementos = np.append(elementos, exp_elements)
        elementos = np.reshape(elementos,(len(elementos),1))
        tipos = np.append(tipos, exp_types)
        tipos = np.reshape(tipos,(len(tipos),1))

    #print(ele_coord)

    ########################## Multiplication of the 'a' coordinate

    coordenadas_0 = []
    coordenadas_1 = []
    coordenadas = []

    for x in range(int(na)):
        if x == 0:
            for y in range(len(exp_elements)):
                exp_coord [y,0] = (float(ele_cord_cst[y,0]))/(int(na))
            coordenadas_0 = np.append(coordenadas_0, exp_coord)
            coordenadas_0 = np.reshape(coordenadas_0, (int(len(coordenadas_0)/3),3))
        else:
            for y in range(len(exp_elements)):
                exp_coord [y,0] = ((float(ele_cord_cst[y,0])))+(1/(int(na)))
            coordenadas_1 = np.append(coordenadas_1, exp_coord)
            coordenadas_1 = np.reshape(coordenadas_1, (int(len(coordenadas_1)/3),3))
    #print(coordenadas_1, coordenadas_1.shape)
    #print(coordenadas_0, coordenadas_0.shape)
    coordenadas = np.append(coordenadas_0, coordenadas_1)
    coordenadas = np.reshape(coordenadas, (int(len(coordenadas)/3),3))

    #print(coordenadas, coordenadas.shape)
    #print(elementos, elementos.shape)


    ########################## Multiplication of the 'b' coordinate

    exp_ele_x = elementos
    exp_coord_x = coordenadas
    ele_cord_cst_x = coordenadas
    exp_ty_x = tipos
    elementos_b = []
    tipos_b = []

    for x in range(int(nb)):
        for y in range(len(exp_ele_x)):
            exp_ele_x[y] = (elementos[y])
            exp_ty_x[y] = (tipos[y])
        elementos_b = np.append(elementos_b, exp_ele_x)
        elementos_b = np.reshape(elementos_b,(len(elementos_b),1))
        tipos_b = np.append(tipos_b, exp_ty_x)
        tipos_b = np.reshape(tipos_b,(len(tipos_b),1))

    #print(elementos_b, elementos_b.shape)
    #print(tipos_b, tipos_b.shape)

    #print(coordenadas, coordenadas.shape)

    coordenadas_b_0 = []
    coordenadas_b_1 = []
    coordenadas_b = []

    for x in range(int(nb)):
        if x == 0:
            for y in range(len(exp_ele_x)):
                exp_coord_x [y,1] = (float(ele_cord_cst_x[y,1]))/(int(nb))
            coordenadas_b_0 = np.append(coordenadas_b_0, exp_coord_x)
            coordenadas_b_0 = np.reshape(coordenadas_b_0, (int(len(coordenadas_b_0)/3),3))
        else:
            for y in range(len(exp_ele_x)):
                exp_coord_x [y,1] = ((float(ele_cord_cst_x[y,1])))+(1/(int(nb)))
            coordenadas_b_1 = np.append(coordenadas_b_1, exp_coord_x)
            coordenadas_b_1 = np.reshape(coordenadas_b_1, (int(len(coordenadas_b_1)/3),3))
    #print(coordenadas_b_1, type(coordenadas_b_1), coordenadas_b_1.shape)
    #print(coordenadas_b_0, type(coordenadas_b_0), coordenadas_b_0.shape)

    coordenadas_b = np.append(coordenadas_b_0, coordenadas_b_1)
    coordenadas_b = np.reshape(coordenadas_b, (int(len(coordenadas_b)/3),3))

    #print(coordenadas_b, coordenadas_b.shape)
    #print(elementos_b, elementos_b.shape)


    ########################## Multiplication of the 'c' coordinate

    exp_ele_y = elementos_b
    exp_coord_y = coordenadas_b
    ele_cord_cst_y = coordenadas_b
    exp_ty_y = tipos_b
    elementos_c = []
    tipos_c = []

    for x in range(int(nc)):
        for y in range(len(exp_ele_y)):
            exp_ele_y[y] = (elementos_b[y])
            exp_ty_y[y] = (tipos_b[y])
        elementos_c = np.append(elementos_c, exp_ele_y)
        elementos_c = np.reshape(elementos_c,(len(elementos_c),1))
        tipos_c = np.append(tipos_c, exp_ty_y)
        tipos_c = np.reshape(tipos_c,(len(tipos_c),1))

    #print(elementos_c, elementos_c.shape)
    #print(tipos_c, tipos_c.shape)

    print(coordenadas_b, coordenadas_b.shape)

    coordenadas_c_0 = []
    coordenadas_c_1 = []
    coordenadas_c = []

    for x in range(int(nc)):
        if x == 0:
            for y in range(len(exp_ele_y)):
                exp_coord_y [y,2] = (float(ele_cord_cst_y[y,2]))/(int(nc))
            coordenadas_c_0 = np.append(coordenadas_c_0, exp_coord_y)
            coordenadas_c_0 = np.reshape(coordenadas_c_0, (int(len(coordenadas_c_0)/3),3))
        else:
            for y in range(len(exp_ele_y)):
                exp_coord_y [y,2] = ((float(ele_cord_cst_y[y,2])))+(1/(int(nc)))
            coordenadas_c_1 = np.append(coordenadas_c_1, exp_coord_y)
            coordenadas_c_1 = np.reshape(coordenadas_c_1, (int(len(coordenadas_c_1)/3),3))
    #print(coordenadas_c_1, type(coordenadas_c_1), coordenadas_c_1.shape)
    #print(coordenadas_c_0, type(coordenadas_c_0), coordenadas_c_0.shape)

    coordenadas_c = np.append(coordenadas_c_0, coordenadas_c_1)
    coordenadas_c = np.reshape(coordenadas_c, (int(len(coordenadas_c)/3),3))

    #print(coordenadas_c, coordenadas_c.shape)
    #print(elementos_c, elementos_c.shape)

    #return(tipos_c, elementos_c, coordenadas_c, tipos_c.shape, elementos_c.shape, coordenadas_c.shape)
    return(tipos_c, elementos_c, coordenadas_c)

print(replicate(na, nb, nc, types, elements, ele_coord))
