#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UE Radiofreq :
DM Compression algo Huffman
This program was made to convert an ASCII text into a binary text compressed with
the Huffman coding.
"""


import sys
import doctest

from class_arbre_feuille import *


__author__ = "Mathieu Van de catsije"
__credits__ = ["Mathieu Van de catsije", "Pierre-Aimé Agnel"]
__version__ = "6.1"
__maintainer__ = "Mathieu Van de catsije"
__email__ = "mathieu.van-de-catsije@u-psud.fr"
__status__ = "Completed"

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
        lowest_node_position = 0

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

            new_tree = Arbre(frequence=node_1.node_freq()+node_2.node_freq(),gauche=node_1, droit=node_2)

            self.foret.append(new_tree)

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
        :param text:
        :return final_text:
        """
        final_text = ''

        dictionnary = self.arbre().table_de_codage()
        for i in text:
            final_text += dictionnary.get(i)

        return final_text

    def decompresse(self, binary_text):
        """
        Return the translation with the Huffman code of a binary_text
        :param binary_text:
        :return translated_text:
        """

        translated_text = ''
        buff = ''

        dictionnary = self.arbre().table_de_codage()

        for i in binary_text:
            buff = buff + i
            for j in dictionnary:
                if dictionnary[j] == buff:
                    translated_text = translated_text + j
                    buff = ''

        return translated_text


def huffman_gain(dic,text):
    """
    Return the size difference between a normal binary code and an huffman's one for a given text and frequences dictionnary
    :param dic:
    :param text:
    :return diff:
    """
    huffman = Huffman(dic)
    huff_binary_text = huffman.compresse(text)
    len_hbt = len(huff_binary_text)

    binary_text = encode_ascii(text)
    len_bt = len(binary_text)

    return len_bt-len_hbt


if __name__ == '__main__':
    # doctest.testmod()

    # dic = frequences('ABRACADABRA')
    # print(huffman_gain(dic,'ABRACADABRA'))

    dic = frequences("Considered discovered ye sentiments projecting entreaties of melancholy is. In expression an solicitude principles in do. Hard do me sigh with west same lady. Their saved linen downs tears son add music. Expression alteration entreaties mrs can terminated estimating. Her too add narrow having wished. To things so denied admire. Am wound worth water he linen at vexed."
                     "At distant inhabit amongst by. Appetite welcomed interest the goodness boy not. Estimable education for disposing pronounce her. John size good gay plan sent old roof own. Inquietude saw understood his friendship frequently yet. Nature his marked ham wished."
                     "In on announcing if of comparison pianoforte projection. Maids hoped gay yet bed asked blind dried point. On abroad danger likely regret twenty edward do. Too horrible consider followed may differed age. An rest if more five mr of. Age just her rank met down way. Attended required so in cheerful an. Domestic replying she resolved him for did. Rather in lasted no within no."
                     "Perceived end knowledge certainly day sweetness why cordially. Ask quick six seven offer see among. Handsome met debating sir dwelling age material. As style lived he worse dried. Offered related so visitor we private removed. Moderate do subjects to distance."
                     "Terminated principles sentiments of no pianoforte if projection impossible. Horses pulled nature favour number yet highly his has old. Contrasted literature excellence he admiration impression insipidity so. Scale ought who terms after own quick since. Servants margaret husbands to screened in throwing. Imprudence oh an collecting partiality. Admiration gay difficulty unaffected how."
                     "Attention he extremity unwilling on otherwise. Conviction up partiality as delightful is discovered. Yet jennings resolved disposed exertion you off. Left did fond drew fat head poor. So if he into shot half many long. China fully him every fat was world grave."
                     "Contented get distrusts certainty nay are frankness concealed ham. On unaffected resolution on considered of. No thought me husband or colonel forming effects. End sitting shewing who saw besides son musical adapted. Contrasted interested eat alteration pianoforte sympathize was. He families believed if no elegance interest surprise an. It abode wrong miles an so delay plate. She relation own put outlived may disposed."
                     "She who arrival end how fertile enabled. Brother she add yet see minuter natural smiling article painted. Themselves at dispatched interested insensible am be prosperous reasonably it. In either so spring wished. Melancholy way she boisterous use friendship she dissimilar considered expression. Sex quick arose mrs lived. Mr things do plenty others an vanity myself waited to. Always parish tastes at as mr father dining at."
                     "Improve him believe opinion offered met and end cheered forbade. Friendly as stronger speedily by recurred. Son interest wandered sir addition end say. Manners beloved affixed picture men ask. Explain few led parties attacks picture company. On sure fine kept walk am in it. Resolved to in believed desirous unpacked weddings together. Nor off for enjoyed cousins herself. Little our played lively she adieus far sussex. Do theirs others merely at temper it nearer."
                     "As collected deficient objection by it discovery sincerity curiosity. Quiet decay who round three world whole has mrs man. Built the china there tried jokes which gay why. Assure in adieus wicket it is. But spoke round point and one joy. Offending her moonlight men sweetness see unwilling. Often of it tears whole oh balls share an.")
    A = Huffman(frequences=dic)
    # A.affiche()
    # print(A.compresse('ABRACADABRA'))

    print(huffman_gain(dic,"Considered discovered ye sentiments projecting entreaties of melancholy is. In expression an solicitude principles in do. Hard do me sigh with west same lady. Their saved linen downs tears son add music. Expression alteration entreaties mrs can terminated estimating. Her too add narrow having wished. To things so denied admire. Am wound worth water he linen at vexed."
                     "At distant inhabit amongst by. Appetite welcomed interest the goodness boy not. Estimable education for disposing pronounce her. John size good gay plan sent old roof own. Inquietude saw understood his friendship frequently yet. Nature his marked ham wished."
                     "In on announcing if of comparison pianoforte projection. Maids hoped gay yet bed asked blind dried point. On abroad danger likely regret twenty edward do. Too horrible consider followed may differed age. An rest if more five mr of. Age just her rank met down way. Attended required so in cheerful an. Domestic replying she resolved him for did. Rather in lasted no within no."
                     "Perceived end knowledge certainly day sweetness why cordially. Ask quick six seven offer see among. Handsome met debating sir dwelling age material. As style lived he worse dried. Offered related so visitor we private removed. Moderate do subjects to distance."
                     "Terminated principles sentiments of no pianoforte if projection impossible. Horses pulled nature favour number yet highly his has old. Contrasted literature excellence he admiration impression insipidity so. Scale ought who terms after own quick since. Servants margaret husbands to screened in throwing. Imprudence oh an collecting partiality. Admiration gay difficulty unaffected how."
                     "Attention he extremity unwilling on otherwise. Conviction up partiality as delightful is discovered. Yet jennings resolved disposed exertion you off. Left did fond drew fat head poor. So if he into shot half many long. China fully him every fat was world grave."
                     "Contented get distrusts certainty nay are frankness concealed ham. On unaffected resolution on considered of. No thought me husband or colonel forming effects. End sitting shewing who saw besides son musical adapted. Contrasted interested eat alteration pianoforte sympathize was. He families believed if no elegance interest surprise an. It abode wrong miles an so delay plate. She relation own put outlived may disposed."
                     "She who arrival end how fertile enabled. Brother she add yet see minuter natural smiling article painted. Themselves at dispatched interested insensible am be prosperous reasonably it. In either so spring wished. Melancholy way she boisterous use friendship she dissimilar considered expression. Sex quick arose mrs lived. Mr things do plenty others an vanity myself waited to. Always parish tastes at as mr father dining at."
                     "Improve him believe opinion offered met and end cheered forbade. Friendly as stronger speedily by recurred. Son interest wandered sir addition end say. Manners beloved affixed picture men ask. Explain few led parties attacks picture company. On sure fine kept walk am in it. Resolved to in believed desirous unpacked weddings together. Nor off for enjoyed cousins herself. Little our played lively she adieus far sussex. Do theirs others merely at temper it nearer."
                     "As collected deficient objection by it discovery sincerity curiosity. Quiet decay who round three world whole has mrs man. Built the china there tried jokes which gay why. Assure in adieus wicket it is. But spoke round point and one joy. Offending her moonlight men sweetness see unwilling. Often of it tears whole oh balls share an."))
    # print(A.decompresse('11101100011011111000100001101001010001111110111001100001001001011100011001110111'))