def poly_mult (a, b, mod_pol):
    ab = 0
    aa=bin(a)
    length=len(aa)

    for i_bit in range(length-1, 1, -1):
        if aa[i_bit]=='1':
            b_shift = b<<(length-1-i_bit)
            ab = ab ^ b_shift

    for i_bit in range(0, 8):
        if bin(ab)[2:].zfill(16)[i_bit]=='1':
            mod_pol_shift = mod_pol<<(7-i_bit)
            ab = ab ^ mod_pol_shift
    return ab

