def cipher (plaintext, w, s_box, poly_mat, x):
    import numpy as np
    from add_round_key import add_round_key
    from shift_rows import shift_rows
    from mix_columns import mix_columns
    from sub_bytes import sub_bytes
    if x > 0:
        verbose_mode = 1
    else:
        verbose_mode = 0
    if plaintext.size != 16:
        print('Plaintext has to be a vector (not a cell array) with 16 elements.')
        return
    [row, col] = plaintext.shape
    for i in range(row):
        for j in range(col):
            if plaintext[i, j] < 0 or plaintext[i, j] > 255:
                print('Elements of plaintext vector have to be bytes (0 <= key(i) <= 255).')
                return
    [row2, col2] = w.shape
    if row2 != 44 and col2 != 4:
        print('w has to be an array (not a cell array) with [44 x 4] elements.')
        return
    for i in range(row2):
        for j in range(col2):
            if w[i, j] < 0 or w[i, j] > 255:
                print('Elements of w vector have to be bytes (0 <= key(i) <= 255).')
                return
    if verbose_mode == 1:
        print(' \n'
              '********************************************\n'
              '*                                          *\n'
              '*               C I P H E R                *\n'
              '*                                          *\n'
              '********************************************\n'
              ' \n')
    state = np.reshape(plaintext, (4, 4), 'F')
    if verbose_mode == 1:
        print('Initial state :  \n', state)
    round_key = np.zeros((4, 4), dtype='int16')
    round_key[:, :] = w[0:4, :].T
    if verbose_mode == 1:
        print('Initial round key :              \n', round_key)
    state = add_round_key(state, round_key)
    for iround in range(1, 10):
        if verbose_mode == 1:
            print('State at start of round ', iround, ' :      \n', state)
        state = sub_bytes(state, s_box)
        if verbose_mode == 1:
            print('After sub_bytes :                \n', state)
        state = shift_rows(state)
        if verbose_mode == 1:
            print('After shift_rows :                \n', state)
        state = mix_columns(state, poly_mat)
        if verbose_mode == 1:
            print('After  mix_columns :                \n', state)
        round_key[:, :] = w[4*iround:4+4*iround, :].T
        if verbose_mode == 1:
            print('Round key :                      \n', round_key)
        state = add_round_key(state, round_key)
    if verbose_mode == 1:
        print('State at start of final round :  \n', state)
    state = sub_bytes(state, s_box)
    if verbose_mode == 1:
        print('After sub_bytes :                \n', state)
    state = shift_rows(state)
    if verbose_mode == 1:
        print('After shift_rows :               \n', state)
    round_key[:, :] = w[40:44, :].T
    if verbose_mode == 1:
        print('Round key :                      \n', round_key)
    state = add_round_key(state, round_key)
    if verbose_mode == 1:
        print('Final state :                    \n', state)
    ciphertext = np.reshape(state, (1, 16), 'F')
    return ciphertext
