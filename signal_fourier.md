---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,py:light
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Analyse spectrale d'un signal
_Méthodes numériques_

Dans cette séance, vous allez apprendre à :
* Utiliser les objets Python comme les vecteurs numpy et réaliser des tracés graphiques.
* Créer des fonctions Python et utiliser des boucles.
* Créer une fonction qui construit numériquement l'allure d'un signal temporel à partir de son spectre.
* Obtenir le spectre d'un signal grâce à des fonctions natives de la bibliothèques `numpy.fft`

+++

## Position du problème

(theoriques)=
### Eléments théoriques
On rappelle que le __spectre__ d'un signal est sa décomposition en somme de sinusoïdes où l'on donne : la _fréquence_ ($f_i$), l'_amplitude_ $(A_i)$ et la _phase à l'origine_ ($\phi_i$) de chaque sinusoïde de la décomposition :

$$
s(t) = \sum_{i} A_i \cos \left ( 2 \pi f_i t + \phi_i \right )
$$

_Pour rappel, pour les signaux périodiques, la somme est infinie et les fréquences $f_i$ sont des multiples de la fréquence $f$ du signal._

### Réflexions préliminéaires

__But :__ On veut pouvoir représenter un signal de deux manières :
* son allure temporelle représentée mathématiquement par la fonction $x(t)$ évaluée sur un intervalle $[t_1, t_2]$
* son spectre représenté par l'ensemble des triplets $(f_i, A_i, \phi_i)$ de sa décomposition

__Travail (5 minutes) :__ Réfléchir au(x) type(s) de variable(s) qui permettent, sous `Python` de stocker la représentation de l'allure temporelle (l'intervalle $[t_1, t_2]$ et les valeurs de x sur cet intervalle) et à leur structure puis au(x) type(s) de variable(s) qui permettent de stocker la représentation du spectre d'un signal _(on supposera la somme finie, quitte à limiter la somme à N fréquences dans le cas de sommes infinies)_.

__Après avoir réfléchi à la question précédente__, passer à la suite qui propose une représentation temporelle et fréquentielle sous Python.

+++

### Représentation des signaux

#### Représentation temporelle
Dans un calcul numérique, l'évaluation de la fonction (pour sont tracé par exemple) ne peut être fait que pour des __valeurs discrètes__. On va donc définir pour un signal $s(t)$ dont on connaît la fonction temporelle $s$ :
1. Une fonction qui associe à une valeur de temps $t_k$ la valeur calculée $s(t_k)$.
2. Un vecteur numpy contenant des valeurs d'abscisses temporelles $t_i$ régulièrement réparties entre deux valeurs choisies $t_1$ et $t_2$ et de longueur $N$.
3. Un vecteur numpy contenant les valeurs du signal $s_i$ aux instants $t_i$ : $s_k = s(t_k)$.

On pourra alors tracer le signal temporel ou obtenir son spectre grâce aux fonctions natives de `numpy.fft`

#### Représentation fréquentielle.
Il y a une série de trois grandeurs, on va donc représenter le spectre d'un signal par trois vecteurs :
* un contenant les fréquences $f_i$ de la décomposition
* un contenant les amplitudes $A_i$ de la décomposition
* un contenant les phases à l'origine $\phi_i$ de la décomposition

On pourra alors reconstruire la fonction $s(t)$ comme donnée précédemment et ainsi visualiser son allure temporelle. On pourra aussi représenter le spectre du signal.

On réfléchira aux listes des m premiers éléments des décompositions spectrales des signaux créneaux et triangulaires (de fréquence $f_0$) données ci-dessous :

$$
s_{creneau} = \sum_{i=1}^{m} {4 \over \pi (2i + 1)}\ \sin \left ( 2 \pi (2i + 1) f_0 t \right)
$$

$$
s_{triangle} = \sum_{i=1}^{m} {8 \over {\left (\pi (2i + 1)\right)}^2}\ \sin \left ( 2 \pi (2i + 1) f_0 t \right)
$$


