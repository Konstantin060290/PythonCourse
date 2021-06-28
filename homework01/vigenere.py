def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    import string
    str1 = string.ascii_uppercase
    str2 = string.ascii_lowercase
    delta = len(plaintext) - len(keyword)

    new_keyword = ""
    k = 0
    if delta != 0:
        for i in range(0, len(plaintext)):
            if len(keyword) == 1:
                k = 0
            if k > len(keyword)-1:
                k = 0
            new_keyword += keyword[k]
            k += 1
    else:
        new_keyword = keyword
    for i in range(0, len(plaintext)):
        if plaintext[i] in str1:
            index = int(str1.index(plaintext[i])) + int(str1.index(new_keyword[i]))
        else:
            index = int(str2.index(plaintext[i])) + int(str2.index(new_keyword[i]))
        if index > len(str1):
            index = index - len(str1)
            if plaintext[i] in str1:
                ciphertext += str1[index]
            else:
                ciphertext += str2[index]
            continue
        if plaintext[i] in str1:
            ciphertext += str1[index]
        else:
            ciphertext += str2[index]

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext
