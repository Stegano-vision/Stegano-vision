import math
import string
import sys
import numpy as np
import ast
from sympy import Matrix
from secretpy import MyszkowskiTransposition, CryptMachine
from secretpy.cmdecorators import UpperCase, Block, SaveAll


# Create two dictionaries, english alphabet to numbers and numbers to english alphabet, and returns them
def get_alphabet():
    alphabet = {}
    for character in string.ascii_uppercase:
        alphabet[character] = string.ascii_uppercase.index(character)

    reverse_alphabet = {}
    for key, value in alphabet.items():
        reverse_alphabet[value] = key
    return alphabet, reverse_alphabet


# Create the matrix k for the key
def get_key_matrix(key, alphabet):
    k = list(key)
    m = int(math.sqrt(len(k)))
    for i, character in enumerate(k):
        k[i] = alphabet[character]

    return np.reshape(k, (m, m))


# Create the matrix of m-grams of a text, if needed, complete the last m-gram with the last letter of the alphabet


def get_text_matrix(text, m, alphabet):
    matrix = list(text)
    remainder = len(text) % m
    for i, character in enumerate(matrix):
        matrix[i] = alphabet[character]
    if remainder != 0:
        for i in range(m - remainder):
            matrix.append(25)

    return np.reshape(matrix, (int(len(matrix) / m), m)).transpose()


# Encrypt a Message and returns the ciphertext matrix
def encrypt(key, plaintext, alphabet):
    m = key.shape[0]
    m_grams = plaintext.shape[1]

    # Encrypt the plaintext with the key provided k, calculate matrix c of ciphertext
    ciphertext = np.zeros((m, m_grams)).astype(int)
    for i in range(m_grams):
        ciphertext[:, i] = np.reshape(np.dot(key, plaintext[:, i]) % len(alphabet), m)
    return ciphertext


# Transform a matrix to a text, according to the alphabet
def matrix_to_text(matrix, order, alphabet):
    if order == "t":
        text_array = np.ravel(matrix, order="F")
    else:
        text_array = np.ravel(matrix)
    text = ""
    for i in range(len(text_array)):
        text = text + alphabet[text_array[i]]
    return text


def get_m():
    while True:
        try:
            m = int(input("Insert the length of the grams (m): "))
            if m >= 2:
                return m
            else:
                print("\nYou must enter a number m >= 2\n")
        except ValueError:
            print("\nYou must enter a number m >= 2\n")


# Check if the key is invertible and in that case returns the inverse of the matrix
def get_inverse(matrix, alphabet):
    alphabet_len = len(alphabet)
    if math.gcd(int(round(np.linalg.det(matrix))), alphabet_len) == 1:
        matrix = Matrix(matrix)
        return np.matrix(matrix.inv_mod(alphabet_len))
    else:
        return None


# Decrypt a Message and returns the plaintext matrix
def decrypt(k_inverse, c, alphabet):
    return encrypt(k_inverse, c, alphabet)


# For generating the key for encrypting using first myszkowski


def get_key_encrypt_myszkowki1(h_key):
    key1 = ""
    l1 = len(h_key)
    l2 = int(len(h_key) / 2)
    for i in range(len(h_key)):
        if i < (l2):
            x = h_key[i]
            x = ord(x) + l1
            key1 += chr(x)
            l1 = l1 + 1
        else:
            x = h_key[i]
            x = ord(x) + l2
            key1 += chr(x)
            l2 = l2 + 1
    return key1


# For generating the key for encrypting using second myszkowski


def get_key_encrypt_myszkowki2(key1):
    h_key = list(key1)
    key1 = ""
    i = 0
    while i < 4:
        x = h_key[i]
        h_key[i] = h_key[i + 1]
        h_key[i + 1] = x
        i = i + 2
    for i in range(4):
        x = h_key[i]
        key1 += chr(ord(x) + i + 1)
    return key1


# Get two dictionaries, english alphabet to numbers and numbers to english alphabet


def encryption(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    # Get two dictionaries, english alphabet to numbers and numbers to english alphabet
    alphabet, reverse_alphabet = get_alphabet()

    # Get the key matrix k
    k = get_key_matrix(key, alphabet)

    # Get the m-grams matrix p of the plaintext
    p = get_text_matrix(plaintext, k.shape[0], alphabet)

    # Encrypt the plaintext
    c = encrypt(k, p, alphabet)

    # Transform the ciphertext matrix to a text of the alphabet
    ciphertext = matrix_to_text(c, "t", reverse_alphabet)

    # Generate the key for the first myszkowski transposition
    key_encrypt_myszkowski1 = get_key_encrypt_myszkowki1(key)

    # First encryption using myszkowski
    cipher = MyszkowskiTransposition()
    ciphertextm1 = cipher.encrypt(ciphertext, key_encrypt_myszkowski1, alphabet)

    # Generate the key for the second myszkowski transposition
    key_encrypt_myszkowski2 = get_key_encrypt_myszkowki2(key)

    # Second encryption using myszkowski
    ciphertextm2 = cipher.encrypt(ciphertextm1, key_encrypt_myszkowski2, alphabet)

    return ciphertextm2


def decryption(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    alphabet, reverse_alphabet = get_alphabet()

    cipher = MyszkowskiTransposition()

    # Generate key for myszkowski2
    key_decrypt_myszkowski2 = get_key_encrypt_myszkowki2(key)

    # First decryption using myszkowski

    deciphertext2 = cipher.decrypt(ciphertext, key_decrypt_myszkowski2, alphabet)

    # Generate key for myszkowski1
    key_decrypt_myszkowski1 = get_key_encrypt_myszkowki1(key)

    # Second decryption using myszkowski

    deciphertext1 = cipher.decrypt(deciphertext2, key_decrypt_myszkowski1, alphabet)

    # Generate key for decrypting the hill cipher

    # Get the key matrix k
    k = get_key_matrix(key, alphabet)

    # Check if the key is invertible and in that case returns the inverse of the matrix
    k_inverse = get_inverse(k, alphabet)

    if k_inverse is not None:
        # Get the m-grams matrix c of the ciphertext
        c = get_text_matrix(deciphertext1, k_inverse.shape[0], alphabet)

        # Decrypt the ciphertext
        p = decrypt(k_inverse, c, alphabet)

        # Transform the ciphertext matrix to a text of the alphabet
        plaintext = matrix_to_text(p, "t", reverse_alphabet)
        plaintext = str(plaintext)
        if plaintext[(len(plaintext) - 1)] == "Z":
            plaintext = plaintext[: len(plaintext) - 1]
    else:
        plaintext = "not invertible"
    return plaintext
