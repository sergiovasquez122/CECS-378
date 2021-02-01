import string

def simple_substitution_cipher(message, mapping):
    plaintext = message.replace(' ', '')
    encrypted = ""
    for c in plaintext:
        encrypted += mapping[c]
    return encrypted

def simple_substitution_cipher_decrypt(message, mapping):
    mapping_inv = {v : k for (k, v) in mapping.items()}
    decrypted = ""
    for c in message:
        decrypted += mapping_inv[c]
    return decrypted

def keyword_cipher_construction(keyword):
    cleansed = keyword.replace(' ', '')
    cleansed = cleansed + string.ascii_uppercase
    cleansed = "".join(dict.fromkeys(cleansed))
    mapping = {k : v for (k, v) in zip(string.ascii_uppercase, cleansed)}
    return mapping

def columnar_cipher_construction(keyword):
    cleansed = keyword.replace(' ', '')
    cleansed = "".join(dict.fromkeys(cleansed))
    letters = set(cleansed)
    mapping = {}
    rows = len(cleansed)
    idx = 0
    for c in string.ascii_uppercase:
        if c in letters:
            mapping[c] = idx
            idx += 1
    mapping_to_list = [mapping[c] for c in cleansed]
    return mapping_to_list

def columnar_cipher_encryption(mapping, message):
    cleansed = message.replace(' ', '')
    rows_filled = len(cleansed) // len(mapping)
    rows_partial = len(cleansed) % len(mapping)
    if rows_partial % len(mapping) != 0:
        rows_filled += 1
    matrix = [[' ' for _ in range(len(mapping))] for _ in range(rows_filled)]
    row_idx = 0
    col_idx = 0
    for c in cleansed:
        matrix[row_idx][col_idx] = c
        col_idx += 1
        if col_idx > rows_filled:
            col_idx = 0
            row_idx = row_idx + 1
    encrypted = [' ' for _ in range(len(mapping) * rows_filled)]
    for row_idx, m in enumerate(matrix):
        for col_idx, c in enumerate(m):
            encrypted[(row_idx + 1) * mapping[col_idx] + (row_idx)] = c
    return encrypted

if __name__ == '__main__':
    # constructing mapping for cipher
    mapping = {'A' : 'X', 'B' : 'Q', 'C' : 'K','D' : 'M', 'E' : 'D', 'F' : 'B', 'G' : 'P', 'H' : 'S', 'I' : 'E', 'J' : 'T', 'K' : 'C', 'L' : 'L', 'M' : 'O', 'N' : 'R', 'O' : 'U', 'P' : 'J', 'Q' : 'V', 'R' : 'A', 'S' : 'F', 'T' : 'W', 'U' : 'Z', 'V' : 'G', 'W' : 'H', 'X' : 'N', 'Y' : 'I', 'Z' : 'Y'}
    # problem 1
    encrypted = simple_substitution_cipher("A FEW WORDS ON SECRET WRITING", mapping)
    print(encrypted)
    # problem 2
    decrypted = simple_substitution_cipher_decrypt("WSDBXLLUBWSDSUZFDUBZFSDA", mapping)
    print(decrypted)
    # problem 3
    mapping = keyword_cipher_construction("GILLIGAN")
    encrypted = simple_substitution_cipher("A TALE OF A FATEFUL TRIP", mapping)
    print(encrypted)
    # problem 4
    decrypted = simple_substitution_cipher_decrypt("RGQUNJWNJLDGUAETEOMNABORKGRYGMM", mapping)
    print(decrypted)
    mapping_to_list = columnar_cipher_construction("ZEBRAS")
    encrypted = columnar_cipher_encryption(mapping_to_list, "WE ARE DISCOVERED FLEE AT ONCE")
    print(encrypted)
