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

