def inv_shift_rows(state_in):
    from cycle import  cycle
    state_out = cycle(state_in, 'right')
    return state_out