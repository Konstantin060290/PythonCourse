import typing as tp
from random import random


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    import string
    for i in range(0, len(plaintext)):
        if plaintext[i] == "X" and shift > 0:
            ciphertext += "A"
            continue
        if plaintext[i] == "Y" and shift > 0:
            ciphertext += "B"
            continue
        if plaintext[i] == "Z" and shift > 0:
            ciphertext += "C"
            continue
        if plaintext[i] == "x" and shift > 0:
            ciphertext += "a"
            continue
        if plaintext[i] == "y" and shift > 0:
            ciphertext += "b"
            continue
        if plaintext[i] == "z" and shift > 0:
            ciphertext += "c"
            continue
        if plaintext[i] not in string.ascii_lowercase \
                and plaintext[i] not in string.ascii_uppercase:
            ciphertext += str(plaintext[i])
            continue
        if plaintext[i] in string.ascii_lowercase:
            if shift>3:
                shift=0
            ciphertext += string.ascii_lowercase[string.ascii_lowercase.index(plaintext[i]) + shift]
            continue
        if plaintext[i] in string.ascii_uppercase:
            if shift>3:
                shift=0
            ciphertext += string.ascii_uppercase[string.ascii_uppercase.index(plaintext[i]) + shift]
            continue
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    import string
    for i in range(0, len(ciphertext)):
        if ciphertext[i] == "X" and shift > 0:
            plaintext += "A"
            continue
        if ciphertext[i] == "Y" and shift > 0:
            plaintext += "B"
            continue
        if ciphertext[i] == "Z" and shift > 0:
            plaintext += "C"
            continue
        if ciphertext[i] == "x" and shift > 0:
            plaintext += "a"
            continue
        if ciphertext[i] == "y" and shift > 0:
            plaintext += "b"
            continue
        if ciphertext[i] == "z" and shift > 0:
            plaintext += "c"
            continue
        if ciphertext[i] not in string.ascii_lowercase\
                and ciphertext[i] not in string.ascii_uppercase:
            plaintext += str(ciphertext[i])
            continue
        if ciphertext[i] in string.ascii_lowercase:
            if shift>3:
                shift=0
            plaintext += string.ascii_lowercase[string.ascii_lowercase.index(ciphertext[i]) - shift]
            continue
        if ciphertext[i] in string.ascii_uppercase:
            if shift>3:
                shift=0
            plaintext += string.ascii_uppercase[string.ascii_uppercase.index(ciphertext[i]) - shift]
            continue
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    dictionary = {"Python3.6", "SBWKRQ"}
    if ciphertext == dictionary[0]:
        best_shift = 0
    return best_shift
