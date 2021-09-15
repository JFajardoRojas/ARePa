import re
import numpy as np
import os

PT = ['H' , 'He', 'Li', 'Be', 'B' , 'C' , 'N' , 'O' , 'F' , 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P' , 'S' , 'Cl', 'Ar',
      'K' , 'Ca', 'Sc', 'Ti', 'V' , 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
      'Rb', 'Sr', 'Y' , 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I' , 'Xe',
      'Cs', 'Ba', 'Hf', 'Ta', 'W' , 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 
      'Ra', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Ac', 'Th', 
      'Pa', 'U' , 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'FG', 'X', 'T' ]

def nn(string):
    return re.sub('[^a-zA-Z]','', string)

def nl(string):
    return re.sub('[^0-9]','', string)

def isfloat(value):
    """
        determines if a value is a float
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def iscoord(line):
    """
        identifies coordinates in CIFs
    """
    if nn(line[0]) in PT and line[1] in PT and False not in map(isfloat,line[2:5]):
        return True
    else:
        return False
    
def isbond(line):
    """
        identifies bonding in cifs
    """
    if nn(line[0]) in PT and nn(line[1]) in PT and isfloat(line[2]) and line[-1] in ('S', 'D', 'T', 'A'):
        return True
    else:
        return False

def PBC3DF(c1, c2):
    """
        c1 and c2 are coordinates, either numpy arrays or lists
    """
    diffa = c1[0] - c2[0]
    diffb = c1[1] - c2[1]
    diffc = c1[2] - c2[2]

    if diffa > 0.5:
        c2[0] = c2[0] + 1.0
    elif diffa < -0.5:
        c2[0] = c2[0] - 1.0
    
    if diffb > 0.5:
        c2[1] = c2[1] + 1.0
    elif diffb < -0.5:
        c2[1] = c2[1] - 1.0
 
    if diffc > 0.5:
        c2[2] = c2[2] + 1.0
    elif diffc < -0.5:
        c2[2] = c2[2] - 1.0
    
    return c2

def bbelems(cifname, direc):

    path = os.path.join(direc, cifname)

    with open(path, 'r') as cif:
        cif = cif.read()
        cif = filter(None, cif.split('\n'))
        #cif = cif.split('\n')

    elems = []
    types = []
    elems_append = elems.append
    types_append = types.append
    for line in cif:
        s = line.split()
        if '_cell_length_a' in line:
            a = s[1]
        if '_cell_length_b' in line:
            b = s[1]
        if '_cell_length_c' in line:
            c = s[1]
        if '_cell_angle_alpha' in line:
            alpha = s[1]
        if '_cell_angle_beta' in line:
            beta = s[1]
        if '_cell_angle_gamma' in line:
            gamma = s[1]
        if iscoord(s):
            elems_append(s[1])
        if iscoord(s):
            types_append(s[0])

    return (a, b, c, alpha, beta, gamma, elems, types)

def bb2array(cifname, direc):

    path = os.path.join(direc, cifname)

    with open(path, 'r') as cif:
        cif = cif.read()
        cif = filter(None, cif.split('\n'))

    fcoords = []
    fcoords_append = fcoords.append
    for line in cif:
        s = line.split()
        if '_cell_length_a' in line:
            a = s[1]
        if '_cell_length_b' in line:
            b = s[1]
        if '_cell_length_c' in line:
            c = s[1]
        if '_cell_angle_alpha' in line:
            alpha = s[1]
        if '_cell_angle_beta' in line:
            beta = s[1]
        if '_cell_angle_gamma' in line:
            gamma = s[1]
        if iscoord(s):
            fvec = np.array([float(q) for q in s[2:5]])
            #fcoords_append([s[1],fvec])
            fcoords_append([fvec])


    return fcoords
#print(bb2array("LTA.cif", "zeo_database"))