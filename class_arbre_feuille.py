class Arbre:
    def __init__(self, frequence, gauche, droit):
        """ Construit un Arbre

            frequence: int
            gauche, droit: Arbre
        """
        self.frequence = frequence
        self.gauche = gauche
        self.droit = droit

    def affiche(self, prefixes = ['    ']):
        """ Affiche l'arbre """
        print(''.join(prefixes[:-1]) + '|___' + str(self.frequence))
        prefixes.append('|   ')
        self.gauche.affiche(prefixes)
        prefixes.pop()
        prefixes.append('    ')
        self.droit.affiche(prefixes)
        prefixes.pop()

    def node_freq(self):
        return self.frequence

    def table_de_codage(self, code='',final_coding_table=None):

        if final_coding_table is None:
            final_coding_table = {}
        coding_table = {}

        if type(self.gauche) is Feuille:
            coding_table[self.gauche.node_symbol()] = code+'0'
            final_coding_table.update(coding_table)
        elif type(self.gauche) is Arbre:
            Arbre.table_de_codage(self.gauche,code=code+'0',final_coding_table=final_coding_table)

        if type(self.droit) is Feuille:
            coding_table[self.droit.node_symbol()] = code+'1'
            final_coding_table.update(coding_table)
        elif type(self.droit) is Arbre:
            Arbre.table_de_codage(self.droit, code=code + '1',final_coding_table=final_coding_table)

        return final_coding_table


class Feuille(Arbre):
    def __init__(self, frequence, symbole):
        """ Construit une feuille

            frequence: int
            symbole: str
        """
        Arbre.__init__(self, frequence, None, None)
        self.symbole = symbole

    def affiche(self, prefixes = ['    ']):
        """ Affiche la feuille """
        print("".join(prefixes[:-1]) + '|___' +
                str(self.frequence) +
                '(' + self.symbole + ')')

    def node_freq(self):
        return self.frequence

    def node_symbol(self):
        return self.symbole

    def table_de_codage(self, code=''):

        coding_table = {}

        coding_table[self.symbole] = code

        return coding_table




if __name__ == "__main__":
    A = Arbre(18,
              Arbre(8,
                    Arbre(3,
                          Feuille(1, 'd'),
                          Feuille(2, 'c')),
                    Feuille(5, 'b')),
              Feuille(10, 'a'))
    A.affiche()
