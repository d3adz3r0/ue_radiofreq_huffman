class Arbre:

    def __init__(self, valeur, gauche, droit):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

    def affiche(self, profondeur=0):
        print('\t' * (profondeur-1) + '|___' + str(self.valeur))
        self.gauche.affiche(profondeur + 1)
        self.droit.affiche(profondeur + 1)

    def hauteur(self):
        return 1 + max(self.gauche.hauteur(),
                       self.droit.hauteur())

    def nombre_noeuds(self):
        return 1 + self.gauche.nombre_noeuds() + self.droit.nombre_noeuds()

    def nombre_noeuds_internes(self):
        return 1 + self.gauche.nombre_noeuds_internes() + self.droit.nombre_noeuds_internes()


class Feuille(Arbre):

    def __init__(self, valeur):
        Arbre.__init__(self, valeur, None, None)

    def affiche(self, profondeur=0):
        print('\t' * (profondeur-1) + '|___' + str(self.valeur))

    def hauteur(self):
        return 0

    def nombre_noeuds(self):
        return 1

    def nombre_noeuds_internes(self):
        return 0


def genere_ABC(n):
    if n == 0:
        return Feuille(0)
    else:
        left, right = genere_ABC(n-1), genere_ABC(n-1)
        return Arbre(0, left, right)

def compte_tous_les_noeuds(n):
    if n<0:
        raise ValueError('The value has to be positive')
    else:
        return [2 ** (i + 1) - 1 for i in range(n + 1)]

def compte_tous_les_noeuds_internes(n):
    if n==0:
        return [1]
    else:
        return compte_tous_les_noeuds(n - 1)




if __name__ == "__main__":
    # A = Arbre(1, Arbre(2, Arbre(3, Feuille(4), Arbre(5, Feuille(6), Feuille(7))), Arbre(8,
    #                                                                                     Arbre(9, Feuille(10),
    #                                                                                           Feuille(11)),
    #                                                                                     Feuille(12))),
    #           Arbre(13, Feuille(14), Arbre(15, Feuille(16), Feuille(17))))
    A = genere_ABC(3)
    print("####  Affichage : ####")
    A.affiche()
    print('\n')
    print('Hauteur : ',A.hauteur())
    print('Nombre de noeuds : ',A.nombre_noeuds())
    print('Nombre de noeuds internes :',A.nombre_noeuds_internes())
    # N=0
    # print(compte_tous_les_noeuds(N),'\n',compte_tous_les_noeuds_internes(N))

