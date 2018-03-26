def sub_bytes (bytes_in, s_box):
    import numpy as np
    [row, col] = bytes_in.shape
    bytes_out = np.zeros((row, col), dtype='int16')
    for i in range(row):
        for j in range(col):
            bytes_out[i, j] = s_box[0, bytes_in[i, j]]
    return bytes_out
