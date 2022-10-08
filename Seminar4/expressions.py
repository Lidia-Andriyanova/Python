import random

def coefficients(count, min_value, max_value):
    coefs = dict()
    for i in range(count + 1):
        coef = random.randint(min_value, max_value + 1)
        coefs[i] = coef
    return coefs

def monomial(coef, degree, sign):
    mono_str = ''
    if coef > 0:
        if sign:
            mono_str += ' + '
    elif coef < 0:
        if sign:
            mono_str += ' - '
        else:
            mono_str += '-'
    coef = abs(coef)
    if coef > 0:
        if coef > 1:
            mono_str += str(coef)
        if degree >= 1:
            mono_str += 'x'
        if degree > 1:
            mono_str += '^' + str(degree)
    return mono_str

def polynom(coefs):
    res_str = ''
    cur_degree = max(coefs.keys())
    while cur_degree >= 0:
        if cur_degree in coefs:
            coef = coefs[cur_degree]
        else:
            coef = 0
        res_str += monomial(coef, cur_degree, res_str != '')
        cur_degree -= 1
    if res_str != '':
        res_str += ' = 0'
    else:
        res_str += '0 = 0'
    return res_str

def file_write(file_name, in_str):
    with open(file_name, 'w') as file_info:
        file_info.write(in_str)

def file_read(file_name):
    with open(file_name, 'r') as file_info:
        return file_info.readline()

def coefs_from_polynom(poly):
    poly = poly.replace(' ', '')
    coefs = dict()
    i = 0
    while i < len(poly):
        neg_sign = False
        if poly[i] in ['-', '+'] or (i == 0 and poly[i].isdigit()):
            if poly[i] == '-':
                neg_sign = True
            if poly[i] in ['-', '+']:
                i += 1

            coef = ''
            while i < len(poly):
                if poly[i].isdigit():
                    coef += poly[i]
                else:
                    break
                i += 1
            if coef == '':
                coef = '1'
            if neg_sign:
                coef = '-' + coef

            if poly[i] + poly[i + 1] == 'x^':
                i += 2
                degree = ''
                while i < len(poly):
                    if poly[i].isdigit():
                        degree += poly[i]
                    else:
                        break
                    i += 1
                i -= 1
            elif poly[i] == 'x':
                degree = '1'
            else:
                degree = '0'

            coefs[int(degree)] = int(coef)
        i += 1
    return coefs

def polynom_sum(coefs1, coefs2):
    coef_sum = dict()
    if max(coefs1.keys()) > max(coefs2.keys()):
        cur_degree = max(coefs1.keys())
    else:
        cur_degree = max(coefs2.keys())
    while cur_degree >= 0:
        if cur_degree in coefs1:
            coef1 = coefs1[cur_degree]
        else:
            coef1 = 0
        if cur_degree in coefs2:
            coef2 = coefs2[cur_degree]
        else:
            coef2 = 0
        coef_sum[cur_degree] = coef1 + coef2
        cur_degree -= 1
    return coef_sum
