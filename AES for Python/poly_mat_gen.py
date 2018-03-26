def poly_mat_gen(x):
    import numpy as np
    from cycle import cycle
    if x > 0:
        verbose_mode = 1
    else:
        verbose_mode = 0
    if verbose_mode == 1:
        print(' \n'
              '********************************************\n'
              '*                                          *\n'
              '*     P O L Y _ M A T   C R E A T I O N    *\n'
              '*                                          *\n'
              '********************************************\n'
              ' \n')
    row_hex = ['02', '03', '01', '01']
    row = np.zeros((1, len(row_hex)), dtype='int16')
    for i in range(len(row_hex)):
        row[0, i] = int(row_hex[i], 16)
    rows = np.vstack((row, row))
    rows = np.vstack((rows, rows))
    poly_mat = cycle(rows, 'right')
    inv_row_hex = ['0e', '0b', '0d', '09']
    inv_row = np.zeros((1, len(row_hex)), dtype='int16')
    for i in range(len(inv_row_hex)):
        inv_row[0, i] = int(inv_row_hex[i], 16)
    inv_rows = np.vstack((inv_row, inv_row))
    inv_rows = np.vstack((inv_rows, inv_rows))
    inv_poly_mat = cycle(inv_rows, 'right')
    if verbose_mode == 1:
        print('poly_mat : \n', poly_mat)
        print('inv_poly_mat : \n', inv_poly_mat)
    return poly_mat, inv_poly_mat


