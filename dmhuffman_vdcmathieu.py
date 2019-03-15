"""
UE Radiofreq :
DM Compression algo Huffman

@author : Mathieu Van de catsije
"""

import sys
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

    def pop_min(self):
        """
        Return the node with the lowest value and remove it from forest variable
        :return lowest_node:
        """

        lowest_node_freq = sys.maxsize

        for i in range(len(self.foret)):
            node = self.foret[i]
            if node.node_freq() < lowest_node_freq:
                lowest_node_freq = node.node_freq()
                lowest_node_position = i

        lowest_node = self.foret[lowest_node_position]
        self.foret.pop(lowest_node_position)

        return lowest_node

    def fusion(self):
        """
        Take the two lowest node of foret and fuse them into a tree. Return True if
        the fusion is possible, false if it is not (in case all node has already been fused)
        :return True/False:
        """

        if len(self.foret) == 1:
            return False
        else:
            node_1 = Huffman.pop_min()
            node_2 = Huffman.pop_min()

            # so node_2 >= node_1

            nouveau = Arbre()



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
    A.pop_min()
    for f in A.foret:
        f.affiche()