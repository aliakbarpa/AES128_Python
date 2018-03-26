def aes_init():
    from s_box_gen import s_box_gen
    from key_expansion import key_expansion
    from rcon_gen import rcon_gen
    from poly_mat_gen import poly_mat_gen
    import numpy as np
    [s_box, inv_s_box] = s_box_gen(1)
    rcon = rcon_gen(1)
    key_hex = ['FF', '11', '12', '25', '99', 'F0', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01']
    key = np.zeros((1, len(key_hex)), dtype='int16')
    for i in range(len(key_hex)):
        key[0, i] = int(key_hex[i], 16)
    w = key_expansion(key, s_box, rcon, 1)
    [poly_mat, inv_poly_mat] = poly_mat_gen(1)
    return s_box, inv_s_box, w, poly_mat, inv_poly_mat
