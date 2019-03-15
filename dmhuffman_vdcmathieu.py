"""
UE Radiofreq :
DM Compression algo Huffman

@author : Mathieu Van de catsije
"""

import doctest
from class_arbre_feuille import *

def encode_ascii(text_to_encode):
    """
    Take a string in ASCII characters and return the encoding into binary number.
    :param text_to_encode:
    :return encoded_text:

    >>> encode_ascii("bonjour")
    '01100010011011110110111001101010011011110111010101110010'
    """

    encoded_text = []

    for i in range(len(text_to_encode)):
        letter_to_encode = text_to_encode[i]
        letter_placement = ord(letter_to_encode)
        binary = "{:08b}".format(letter_placement)
        encoded_text += binary

    encoded_text = "".join(map(str, encoded_text))

    return encoded_text

def frequences(text):
    """
    Take a string and return a dictionnary countaining each letter of the string with its appearence associated
    :param text:
    :return dictionnary:

    >>> frequences('ABRACADABRA')
    {'A': 5, 'B': 2, 'R': 2, 'C': 1, 'D': 1}
    """

    dictionnary = {}

    for i in text:
        if dictionnary.get(i) is None:
            dictionnary[i] = 1
        else:
            dictionnary[i] = dictionnary.get(i) + 1

    return dictionnary

class Huffman:

    """ Huffman's contruction algorithm"""

    def __init__(self, frequences):

        """
        Init
        Frequences : freq's dictionnary
        """

        self.foret = []

        for i in frequences:
            feuille_to_add = Feuille(frequence=frequences[i], symbole=i)
            self.foret.append(feuille_to_add)



if __name__=='__main__':
    doctest.testmod()
    # A = Arbre(18,
    #           Arbre(8,
    #                 Arbre(3,
    #                       Feuille(1, 'd'),
    #                       Feuille(2, 'c')),
    #                 Feuille(5, 'b')),
    #           Feuille(10, 'a'))
    # A.affiche()

    dic = frequences('ABRACADABRA')
    A = Huffman(frequences=dic)
    for f in A.foret:
        f.affiche()