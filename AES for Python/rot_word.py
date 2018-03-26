def rot_word(w_in):
    import numpy as np
    w_out = np.zeros((1, 4), dtype='int16')
    w_out[0] = [w_in[0, 1], w_in[0, 2], w_in[0, 3], w_in[0, 0]]
    return w_out
