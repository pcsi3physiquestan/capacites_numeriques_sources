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
La page ci-présente existe en version notebook téléchargeable grâce au bouton ![Bouton](./images/bouton_tl.png) (choisir le format `.ipynb`). On rappelle qu'l faut ensuite l'enregistrer dans un répertoire adéquat sur votre ordinateur (`capa_num` par exemple dans votre répertoire personnel) puis lancer Jupyter Notebook depuis Anaconda pour accéder au notebook, le modifier et exécutez les cellules de code adéquates.

# Analyse spectrale d'un signal
_Méthodes numériques_

Dans cette séance, vous allez apprendre à :
* Utiliser les objets Python comme les vecteurs numpy
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

__Travail (5/10minutes) :__ Réfléchir au(x) type(s) de variable(s) qui permettent, sous `Python` de stocker la représentation de l'allure temporelle (l'intervalle $[t_1, t_2]$ et les valeurs de x sur cet intervalle) et à leur structure puis au(x) type(s) de variable(s) qui permettent de stocker la représentation du spectre d'un signal _(on supposera la somme finie, quitte à limiter la somme à N fréquences dans le cas de sommes infinies)_.

__Après avoir réfléchi à la question précédente__, passer à la suite qui propose une représentation temporelle et fréquentielle sous Python.

+++

### Représentation des signaux

#### Représentation temporelle
Dans un calcul numérique, l'évaluation de la fonction (pour sont tracé par exemple) ne peut être fait que pour des __valeurs discrètes__. On va donc définir pour un signal $s(t)$ dont on connaît la fonction temporelle $s$ :
1. Une fonction qui associe à une valeur de temps $t_i$ la valeur calculée $s(t_i)$.
2. Un vecteur numpy contenant des valeurs d'abscisses temporelles $t_k$ régulièrement réparties entre deux valeurs choisies $t_1$ et $t_2$ et de longueur $N$.
3. Un vecteur numpy contenant les valeurs du signal $s_k$ aux instants $t_k$ : $s_k = s(t_k)$.

On pourra alors tracer le signal temporel ou obtenir son spectre grâce aux fonctions natives de `numpy.fft`

#### Représentation fréquentielle.
Il y a une série de trois grandeurs, on va donc représenter le spectre d'un signal par trois vecteurs :
* un contenant les fréquences $f_i$ de la décomposition
* un contenant les amplitudes $A_i$ de la décomposition
* un contenant les phases à l'origine $\phi_i$ de la décomposition

On pourra alors reconstruire la fonction $s(t)$ comme donnée précédemment et ainsi visualiser son allure temporelle. On pourra aussi représenter le spectre du signal.

On réfléchira aux listes des m premiers éléments des décompositions spectrales des signaux créneaux et triangulaires (de fréquence $f_0$) données ci-dessous :

$$
s_{creneau} = \sum_{k=1}^{m} {4 \over \pi (2k + 1)}\ \sin \left ( 2 \pi (2k + 1) f_0 t \right)
$$

$$
s_{triangle} = \sum_{k=1}^{m} {8 \over {\left (\pi (2k + 1)\right)}^2}\ \sin \left ( 2 \pi (2k + 1) f_0 t \right)
$$

+++

## Du spectre à la représentation temporelle.

> __Exercice 1__  
> Dans la cellule de code suivante, vous devez :
> 1. Ecrire une fonction `fonc_temp` qui prend 4 arguments : 1 flottant `t` et 3 vecteurs numpy `fs`, `amps`, `phis` (liste des fréquences amplitudes et phases à l'origine du spectre) et qui renvoie la valeur de $s$ définie dans les [Eléments théoriques](theoriques) évaluée à l'instant `t`.
> 2. Ecrire une fonction `evalue_temp` qui prend comme arguments : 3 vecteurs numpy `fs`, `amps`, `phis`, 2 flottants `t1`, `t2` et un entier `N` et qui renvoie deux vecteurs numpy:
>    1. un vecteur contenant `N` valeurs de temps $t_k$ régulièrement réparties entre `t1` et `t2`
>    2. un vecteur contenant les valeurs $s_k$ qui sont les évaluatinos de $s$ (définie dans les Eléments théoriques) aux instants $t_k$
> 3. Ecrire une fonction `trace_spec` qui prend comme arguments 3 vecteurs numpy `fs`, `amps`, `phis` et qui trace le spectre du signal.
> 4. Ecrire une fonction `trac_temp` qui prend comme arguments : 3 vecteurs numpy `fs`, `amps`, `phis`, 2 flottants `t1`, `t2` et un entier `N` et qui trace l'allure temporelle de $s$ entre `t1` et `t2` en évaluant `N` valeurs de temps régulièrement réparties.
> 5. Utiliser les fonctions précédentes pour tracer le spectre puis l'allure temporelle d'un signal créneau et d'un signal triangle à partir des $m$ premières composantes spectrales de leur décomposition (m = 10). On discutera de la validité d'approximer les signaux créneaux et triangle par leurs 10 premières composantes.

_Quelques indications utiles :_
* Si une fonction retourne deux éléments (ex : return x, y) alors pour récuperer les __deux__ variables lors de l'appel de la fonction, on écrira `x0, y0 = fonction_appelee(...)`
* _Pour le tracé des spectres_ : La fonction `bar(x, y, width, ...)` de `matplotlib.pyplot` fonctionne comme `plot` (mêmes options) mais trace des barres au lieu de points. L'argument `width` défini la largeur des barres, on prendra `0.05`

```{code-cell} ipython3
"""Quelques indications :
- N'oubliez d'importer les bibliothèques scientifiques
- Pensez à utiliser les fonctions précédentes au lieu de tout réécrire.
- Pensez aux fonctions numpy pour créer simplement des vecteurs.
"""



```

## Du tracé temporelle au spectre
On suppose qu'on dispose de `N` mesures d'un signal $s$ faites avec une fréquence d'échantillonnage `fe`. Ces valeurs sont stockées dans un vecteur numpy `sk`. On veut obtenir la transformée de Fourier du signal $s$ basé sur les mesures `sk`.

Nous allons utiliser la fonction native `fft` de la bibliothèque `numpy.fft`.
* `fft(sk)` permet de calculer la TF à partir de `sk` pour une liste de valeurs de fréquences discrètes $f_i$. La fonction renvoie les amplitudes sous formes de grandeurs complexes :
    * Le module est l'amplitude de la composante spectrale
    * son argument est la phase à l'origine du signal.

Les valeurs $f_i$ auxquelles le spectre est évalué sont données par la liste suivante :

$$
[0, 1, ..., N-1] \times {fe \over N}
$$

> __Exercice 2__  
> Vous devez :
> 1. Ecrire une fonction `eval_fft` qui prend comme argument un vecteur numpy `sk` et une fréquence d'échantilonnage `fe` et qui renvoie :
>    1. une liste numpy contenant les fréquences $f_i$
>    2. une liste numpy contenant les amplitudes associées à chaque composante spectrale de la TF de `sk`
>    3. une liste numpy contenant les phases à l'origine associées à chaque composante spectrale de la TF de `sk`
> 2. Créer des vecteurs de taille $N = 100$ simulant la mesure (parfaite !) d'un signal (prendre à chaque fois des amplitudes égales à $1 SI$) :
>    1. sinusoïdal de fréquence 2kHz (réfléchir aux choix de la fréquence d'échantillonnage) et de valeur moyenne $1 SI$
>    1. produit de deux sinusoïdes de fréquences 100Hz et 1kHz.
>    1. créneau de fréquence 2kHz (réfléchir aux choix de la fréquence d'échantillonnage)
> 3. Obtenir puis tracer le spectre pour chacun des signaux précédents. Commenter ce qu'on observe. On parlera en TP de __repli spectral__. En pratique, on ne peut mesurer une fréquence supérieure à $f_e/2$, c'est le __critère de Shannon-Nyquist__. Modifier la fonction `eval_fft` pour ne renvoyer les fréquences ainsi que les amplitudes et phases que jusqu'à $f_e/2$.
> 4. Reconstruire le signal à partir des spectres obtenues et les tracer. On représente sur le même graphique, le signal acquis pour comparaison avec le signal reconstruit (le problème de repli spectral vous obligera à multiplier par 2 toutes les amplitudes).


_Données utiles_ :
* Les fonctions `abs` et `angle` de la bibliothèque `numpy` permettent de calculer respectivement le module et l'argument d'un complexe et peuvent s'appliquer sur un vecteur entier.
* Plusieurs fonctions ont déjà été créés pour les dernières questions, ce n'est pas la peine de les réécrire.

```{code-cell} ipython3
"""On importe pour vous la fonction fft"""
from numpy.fft import fft  # Avec cette méthode d'importation, vous pouver utiliser directement la syntaxe fft(...)



```

```{code-cell} ipython3

```
