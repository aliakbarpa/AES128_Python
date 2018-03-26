def mix_columns(state_in, poly_mat):
    import numpy as np
    state_out = np.zeros((4,4), dtype='int16')
    from poly_mult import poly_mult
    mod_pol =int('100011011',2)
    for i_col_state in range(4):
        for i_row_state in range(4):
            temp_state = 0
            for i_inner in range(4):
                temp_prod = poly_mult(poly_mat[i_row_state, i_inner], state_in[i_inner, i_col_state], mod_pol)
                temp_state = temp_state^temp_prod
            state_out[i_row_state, i_col_state] = temp_state
    return state_out
