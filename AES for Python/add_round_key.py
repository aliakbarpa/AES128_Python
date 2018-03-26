def add_round_key(state_in, round_key):
    import numpy as np
    state_out = np.zeros((4,4), dtype='int16')
    [row, col] = state_in.shape
    for i in range(row):
        for j in range(col):
            state_out[i, j] = state_in[i, j] ^ round_key[i, j]
    return state_out
