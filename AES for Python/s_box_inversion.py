def s_box_inversion(s_box):
    import numpy as np
    inv_s_box = np.zeros((1, 256), dtype='int16')
    for i in range(256):
        inv_s_box[0, s_box[0, i]] = i
    return inv_s_box

