def find_inverse(b_in, mod_pol):
    from poly_mult import poly_mult
    for i in range(1, 256):
        prod = poly_mult(b_in, i, mod_pol)
        if prod == 1:
            return i


