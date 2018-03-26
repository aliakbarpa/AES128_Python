def shift_rows(state_in):
    from cycle import  cycle
    state_out = cycle(state_in, 'left')
    return state_out