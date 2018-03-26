def key_expansion(key, s_box, rcon,  x):
    import numpy as np
    from sub_bytes import sub_bytes
    from rot_word import rot_word
    if x > 0:
        verbose_mode = 1
    else:
        verbose_mode = 0
    if key.size != 16:
        print('Key has to be a vector (not a cell array) with 16 elements.')
        return
    [row, col] = key.shape
    for i in range (row):
        for j in range (col):
            if key[i, j]<0 or key[i, j]>255:
                print('Elements of key vector have to be bytes (0 <= key(i) <= 255).')
                return
    if verbose_mode == 1:
        print(' \n'
              '********************************************\n'
              '*                                          *\n'
              '*         K E Y   E X P A N S I O N        *\n'
              '*                                          *\n'
              '********************************************\n'
              ' \n')
    w = np.reshape(key, (4, 4), 'F').T
    temp = np.zeros((1, 4), dtype='int16')
    r = np.zeros((1, 4), dtype='int16')
    if verbose_mode == 1:
        print('w(1:4, :) :\n', w)
    for i in range (4, 44):
        temp[0, :] = w[i - 1, :]
        if (i+1)%4 ==1:
            temp = rot_word(temp)
            if verbose_mode == 1:
                print('After rot_word :  ', temp[0, :])
            temp = sub_bytes(temp, s_box)
            if verbose_mode == 1:
                print('After sub_bytes : ', temp[0, :])
            r[0, :] = rcon[int(i / 4 - 1),:]
            if verbose_mode ==1 :
                print('rcon(', i+1 , ', :) :   ', r[0, :])
            for j in range (4):
                temp[0, j] = temp[0, j] ^ r[0, j]
            if verbose_mode == 1:
                print('After rcon xor :  ', temp[0, :])
        for j in range (4):
            temp[0, j] = w[i-4, j] ^ temp[0, j]
        w = np.vstack((w, temp))
        if verbose_mode == 1:
            print('w(', i+1 , ', :) :      ', w[i, :])
    return w








