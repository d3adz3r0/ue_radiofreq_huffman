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

        counter_node = 0
        counter_tree = 0

        if len(self.foret) == 1 and type(self.foret[0]) is Feuille:
            return False

        for i in self.foret:
            if type(i) is Feuille:
                counter_node += 1
            elif type(i) is Arbre:
                counter_tree +=1

        if counter_node == 0 and counter_tree == 1:
            return False
        else:
            node_1 = Huffman.pop_min(self)
            node_2 = Huffman.pop_min(self)

            # so node_2 >= node_1

            nouveau = Arbre(frequence=node_1.node_freq()+node_2.node_freq(),gauche=node_1, droit=node_2)

            self.foret.append(nouveau)

            return True

    def arbre(self):
        """
        Comput 'fusion' as much as you can the return the final tree
        :return final_tree:
        """

        while True:
            bol = Huffman.fusion(self)
            if bol is False:
                final_tree = self.foret[0]
                return final_tree

    def affiche(self):
        """
        Display the final tree obtained by using the arbre method
        """
        Huffman.arbre(self).affiche()

    def compresse(self, text):
        """
        Take a text and return its 'translation' in Huffman code
        :param texte:
        :return final_text:
        """
        final_text = ''

        dictionnary = self.arbre().table_de_codage()
        for i in text:
            final_text += dictionnary.get(i)

        return final_text



if __name__ == '__main__':
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
    A.affiche()
    print(A.compresse('ABRA'))