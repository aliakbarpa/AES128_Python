#Interpreter is Python 3.6.1
import numpy as np
from aes_init import aes_init
from cypher import cipher
from inv_cypher import inv_cipher
[s_box, inv_s_box, w, poly_mat, inv_poly_mat] = aes_init()
plaintext_hex = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF']
plaintext = np.zeros((1, len(plaintext_hex)), dtype='int16')
for i in range(len(plaintext_hex)):
    plaintext[0, i] = int(plaintext_hex[i], 16)
ciphertext = cipher(plaintext, w, s_box, poly_mat, 1)
re_plaintext = inv_cipher (ciphertext, w, inv_s_box, inv_poly_mat, 1)