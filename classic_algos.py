# -*- encoding: utf-8 -*-
####################################################################
#               Algorithmes classiques en python                   #
#                       Auteur : SuXess                            #
####################################################################


# algorihme de recherche d'élément dans une liste triée
# Sans perte de généralité nous allons supposer que la
# liste est ordonnée par ordre croissant

import random

def recherche_par_dichotomie(liste, elt):

    l = liste
    first_elt = 0
    last_elt = len(l)
    middle = (first_elt + last_elt) // 2
    index_found = False
    
    if l :                      # checking emptiness of l
        if l[0]  >= l[1] :     # in case the liste is in the inverse order
            l.reverse()
        # kernel of algorithme
        while first_elt <= last_elt :
            if elt == l[middle]:
                print( "l'index de l'élément est : ", middle)
                return middle
            elif elt  > l[middle]:
                # Forget about inferior part of the list and work with the sup one
                first_elt = middle + 1
            elif elt  < l[middle]:
                # Forget about superior part of the list and work with the inf one
                last_elt = middle - 1
            middle = (first_elt + last_elt)//2

def maxi_mini(liste):
    """
        algorithme de recherche de maximum et de minimum
    """
    maxi = liste[0]
    mini = liste[0]

    for elt in liste:
        if maxi < elt:
            maxi = elt
        if mini > elt:
            mini = elt
    print ("maxi est {}, mini est {}".format(maxi, mini))

def recherche_sous_chaine(chaine, sous_chaine):
    #index_1 = 0
    #index_2 = 0
    length_1 = len(chaine)
    length_2 = len(sous_chaine)
    for i in range(0, length_1) :
        index = i
        for j in range(0, length_2):
            if chaine[i] == sous_chaine[j] :
                print ("i = {}, j = {}".format(i, j))
                if j == length_2 - 1:
                    print ( "string found at position {0}".format(index))
                    return True
                i = i + 1
            else :
                break
    return False

def zero_de_f(f, a, b, eps):
    m = (a + b) / 2
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    elif f(m) == 0:
        return m
    if f(a)*f(m) < 0 and b-a >= eps:
        b = m
        zero_de_f(f, a, b, eps)
    elif f(a)*f(m) > 0 and b-a >= eps:
        a = m
        zero_de_f(f, a, b, eps)
    else :                                  # le seul cas restant est eps > (b-a)/10
        print ("la solution est : ", m)

def f(x):
    """
        a custom function x^2 - (1/100)^2
    """
    return x*x - 1/10000

def aire_integrale_rectangle(f, a, b, N, side):
    pas = (b - a)/N
    somme = 0
    for _ in range (N):
        if side:
            somme+=f(a)*pas
        else :
            somme+=f(a + pas) * pas
        a = a + pas
    print ("L'aire du la surface par rectangle est :", somme)
    return somme

def aire_integrale_trapeze(f, a, b, N):
    pas = (b - a)/N
    somme = 0
    for _ in range (N):
        somme+=((f(a+pas) + f(a))/2)*pas
        a = a + pas
    print ("L'aire du la surface par trapezes est :", somme)
    return somme

def g(x):
    print("g de {} = {}".format(x, x**3))


def decomposition(n, b):
    rest = []
    while n != 0 :
        rest.append(n%b)
        n = n//b
    rest.reverse()
    print("la decomposition donne : {}".format(str(rest)))
    return rest

def pgcd(a, b):
    init_a, init_b = a, b
    while b != 0 :
        a, b = b, a%b
    print("pgcd de {} et de {} est : {}".format(init_a, init_b, a))
    return abs(a)

def eval_polynome(poly, x):
    #poly is of type [a_n, a_n-1,...., a_1, a_0]
    #poly = a_n.X**n + a_n-1.X**(n-1) + .... a_1.X + a_0
    val = 0
    for c in poly:
        val = val * x + c
    print("la valeur du polynome est : {}".format(val))
    return val

def produit_matrices(A, B):
    # A = [[a_11,...,a_n1], [a_12,...,a_n2], [a_1m,...., a_nm]]
    # B = [[a_11,...,a_m1], [a_12,...,a_m2], [a_1m,...., a_mk]]
    produit = [[sum(L[j] * B[j][k] for j in range(len(A[0]))) for k in range(len(B[0]))]for L in A]
    print(produit)
    print("Le produit matriciel est : " + str(produit))

def tri(liste):
    print("liste initiale : {}".format(liste))
    for i in range(len(liste)):
        for j in range(i, len(liste)):
             if liste[i] > liste[j] :
                 temp = liste[j]
                 liste[j] = liste[i]
                 liste[i] = temp
    print("liste ordonnee : {}".format(liste))

def calcul_monnaie(x):
    L = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    L.reverse()
    x_1 = x//500
    x_2 = (x - x_1*500)//200
    x_3 = (x - x_1*500 - x_2*200)//100
    x_4 = (x - x_1*500 - x_2*200 - x_3*100)//50
    x_5 = (x - x_1*500 - x_2*200 - x_3*100 - x_4*50)//20
    x_6 = (x - x_1*500 - x_2*200 - x_3*100 - x_4*50 - x_5*20)//10
    x_7 = (x - x_1*500 - x_2*200 - x_3*100 - x_4*50 - x_5*20 - x_6*10)//5
    x_8 = (x - x_1*500 - x_2*200 - x_3*100 - x_4*50 - x_5*20 - x_6*10 - x_7*5)//2
    x_9 = (x - x_1*500 - x_2*200 - x_3*100 - x_4*50 - x_5*20 - x_6*10 - x_7*5 - x_8*2)//1
    produit = 500*x_1 + 200*x_2 + 100*x_3 + 50*x_4 + 20*x_5\
              +10*x_6 + 5*x_7 + 2*x_8 + x_9
    print ("x vaut : {}".format(x))
    print("calcul donne : {}".format(produit))
            

liste = [0, 11, 22, 33, 44, 55, 66, 70.5]
elt = 66
chaine = "abcdefghijklmnopqrstuvwxyz"
sous_chaine = 'hijklmn'
matrice_A = [[1, 2, 3], [4, 5, 6]]
matrice_B = [[1, 2], [3, 4], [5, 6]]
recherche_par_dichotomie(liste, elt)
maxi_mini(liste)
recherche_sous_chaine(chaine, sous_chaine)
zero_de_f(f, -1, 1, 0.1)
aire_integrale_rectangle(lambda x: x**2, 0, 1, 100, True)
aire_integrale_trapeze(lambda x: x**2, 0, 1, 100)
decomposition(1001, 5)
pgcd(1001, 5)
eval_polynome([1, 2, 3, 4], 2)
produit_matrices(matrice_A, matrice_B)
random.shuffle(liste)
tri(liste)
calcul_monnaie(493)             
