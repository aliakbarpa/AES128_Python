def cycle(matrix_in, direction):
    import numpy as np
    import operator
    b = np.zeros((4, 4), dtype='int16')
    if abs(operator.eq(direction, 'left')):
        b[0] = matrix_in[0]
        b[1] = [matrix_in[1, 1], matrix_in[1, 2], matrix_in[1, 3], matrix_in[1, 0]]
        b[2] = [matrix_in[2, 2], matrix_in[2, 3], matrix_in[2, 0], matrix_in[2, 1]]
        b[3] = [matrix_in[3, 3], matrix_in[3, 0], matrix_in[3, 1], matrix_in[3, 2]]
    else:
        b[0] = matrix_in[0]
        b[1] = [matrix_in[1, 3], matrix_in[1, 0], matrix_in[1, 1], matrix_in[1, 2]]
        b[2] = [matrix_in[2, 2], matrix_in[2, 3], matrix_in[2, 0], matrix_in[2, 1]]
        b[3] = [matrix_in[3, 1], matrix_in[3, 2], matrix_in[3, 3], matrix_in[3, 0]]
    return b