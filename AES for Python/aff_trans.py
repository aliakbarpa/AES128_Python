def aff_trans(b_in):
    from poly_mult import poly_mult
    mod_pol = int('100000001', 2)
    mult_pol = int('00011111', 2)
    add_pol = int('01100011', 2)
    temp = poly_mult(b_in, mult_pol, mod_pol)
    b_out = temp ^ add_pol
    return b_out

