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

__Si vous vous sentez suffisamment à l'aise,__ vous pouvez passer directement à l'étude approfondie.

# Etude de base

## Exemple d'utilisation des représentations.
### Tracé temporel

On se propose de mettre en place les représentations précédentes dans des cas particuliers sans faire appel à la création de fonction dans un premier temps.

> __Exercice A__  
> On considère un signal sinusoïdal de fréquence 100 Hz, d'amplitude 4 S.I. et de phase à l'origine $-\pi/2$.
> 1. (Théorie): Quelle valeur donner à $t_2$ dans l'intervalle $[0;t_2]$ pour observer 5 périodes ? Quelle est l'expression mathématique de $s(t)$ ?
> 2. Ecrire dans la cellule suivante 5 instructions qui:
>     * Importe le module `numpy` sous l'alias `np`
>     * Importe le module `matplotlib.pyplot` sous l'alias `plt`
>     * Crée un _vecteur_ `numpy` nommé `tk` contenant 1000 valeurs $t_k$ également espacées entre 0 et $t_2$.
>     * Crée un _vecteur_ `numpy` nommé `sk` contenant les 1000 valeurs $s_k = s(t_k)$.
>     * Affiche la taille du vecteur `sk`
> * Pensez à exécutez la cellule une fois écrite.
> * On se rappellera qu'il y a deux façons de créer une suite de valeurs dans un vecteur `numpy`. Réfléchir à la plus adéquat.

```{code-cell}
:tags: [hide-input, remove-output]

```

> __Exercice B__  
> _Les modules importés précédemment restent importés tant que vous êtes sur ce notebook. Inutile de les réimporter. De plus, les variables créées précédemment sont toujours en mémoire._
> Ecrire une suite d'instruction traçant l'allure de $s(t)$. On rappelle qu'il faut:
> 1. Créer la fenêtre graphique et les axes.
> 2. Légender les axes ($s$ et $t$) et titrer le graphique (ici "Signal sinusoïdal")
> 3. Tracer la courbe (inutile de la légender car il n'y en a qu'une).
> 4. Ajouter une grille (`ax.grid()` ou `ax` est la variable où sont stockées les axes).
> 5. Afficher le graphique (`plt.show()`)

```{code-cell}
:tags: [hide-input, remove-output]

```

> __Exercice C__  
> On considère un signal $s_2 (t)$ défini comme la somme de deux signaux sinusoïdaux : le premier de fréquence 100 Hz, d'amplitude 2 S.I. et de phase à l'origine $-\pi/3$ et le second de fréquence 1000 Hz, d'amplitude 2 S.I. et de phase à l'origine $0$. On veut tracer ce signal sur $[0;t_2]$ (même valeur de $t_2$ que précédemment). On va utiliser la représentation fréquentielle proposée dans la présentation. Dans la cellule suivante, vous devez:
> 1. Définir trois vecteurs `fs`, `amps`, `phis` contenant respectivement les fréquences, amplitudes et phases à l'origine des composantes du signaux.
> 2. Ecrire 3 instructions qui:
>     * Initialise la variable `si2` comme un vecteur numpy contenant que des 0 et de taille identique à `tk` (cette variable est toujours définie).
>     * Ajoute à `si2` un vecteur contenant les valeurs, aux instants $t_k$ de la première composante. __On ne rentrera pas à la main les valeurs de fréquence, amplitude et phase à l'origine, mais on utilisera les vecteurs `fs`, `amps`, `phis` créés précédemment pour aller chercher ces valeurs.
>     * Ajoute à `si2` un vecteur contenant les valeurs, aux instants $t_k$ de la deuxième composante. __On ne rentrera pas à la main les valeurs de fréquence, amplitude et phase à l'origine, mais on utilisera les vecteurs `fs`, `amps`, `phis` créés précédemment pour aller chercher ces valeurs.
>     * Tracer l'allure du signal $s_2 (t)$ grâce aux vecteurs précédents (on rappelle que `tk` est toujours défini)

```{code-cell}
:tags: [hide-input, remove-output]

```

> __Exercice D__  
> Le but est d'automatiser la méthode précédente en utilisant une boucle pour qu'elle puisse se généraliser à une somme de m sinusoïdes. m étant quelconque.
> 1. Copier votre code précédent dans la cellule ci-après et remplacer les lignes après l'initialisation de `si2` par une boucle. _On rappelle que la taille d'un vecteur à 1 dimension peut s'obtenir avec la fonction `len`) et que la fonction `range(m)` crée une suite de valeurs allant de 0 __inclus__ à m __exclus__._
> 2. Vérifier son bon fonctionnement en traçant à nouveau la courbe.


```{code-cell}
:tags: [hide-input, remove-output]

```

> __Exercice E__  
> On considère un signal $s_c (t)$ composé de $m$ composantes (de fréquences notées $f_k$, n allant de 0 à m-1) dont les phases à l'origine sont toutes égales à $\pi / 2$, les fréquences sont $f_k = (2 * k + 1) * f_0$ avec $f_0 = 100 Hz$ et d'amplitudes respectives $c_k = \frac{4}{(2k + 1) \pi}$. (C'est le développement d'un créneau).
> 1. A l'aide du code précédent, tracer l'allure temporelle du signal précédent pour $m = 5$ puis $m=10$. On réfléchira à la façon de créer les vecteurs `fsc`, `ampsc` et `phisc` (1 seule ligne d'instruction est nécessaire à chaque fois en utilisant la fonction `np.arange`).


```{code-cell}
:tags: [hide-input, remove-output]

```

### Tracé des spectres.
Pour tracer les spectres, on va utiliser la fonction `bar(x, y, width,...)` de la bibliothèque `matplotlib.pyplot`. Elle fonctionne comme plot (même options comme `label`) mais trace des barres au lieu de points. L'argument `width` défini la largeur des barres, on prendra `0.05`.
> __Exercice F__  
> 1. Utiliser la fonction `bar` pour tracer les spectres de $s_2(t)$ et $s_c(t)$ à partir des listes `fs` et `amps` (ou `fsc` et `ampsc`).

```{code-cell}
:tags: [hide-input, remove-output]

```

On s'intéresse maintenant au cas où la décomposition spectrale n'est pas donnée. On va même prendre un signal non périodique $e(t) = A e^{-t/\tau}$ avec $A = 1.SI$ et $\tau = 2 s$. En pratique, un tel signal est de spectre continu mais comme pour toute étude numérique, on ne peut calculer les amplitudes que pour des valeurs discrètes. Le spectre qu'on va obtenir sera donc discret: on obtiendra les amplitudes $c_i$ des composantes spectrales $f_i$.

On suppose qu'on dispose de `N` mesures d'un signal $e$ faites avec une fréquence d'échantillonnage `fe`. Ces valeurs sont stockées dans un vecteur numpy `ek`. On veut obtenir la transformée de Fourier du signal $s$ basée sur les mesures `ek`.

Nous allons utiliser la fonction native `fft` de la bibliothèque `numpy.fft`.
* `fft(sk)` permet de calculer la TF à partir de `ek` pour une liste de valeurs de fréquences discrètes $f_i$. La fonction renvoie les amplitudes __sous forme d'un vecteur de grandeurs complexes__ :
    * Le module est l'amplitude de la composante spectrale
    * son argument est la phase à l'origine du signal.

Les valeurs $f_i$ auxquelles le spectre est évalué sont données par la liste suivante (non renvoyé par `fft`):

$$
[0, 1, ..., N-1] \times {fe \over N}
$$

> __Exercice G__  
> 1. (Théorie): On suppose qu'on a échantillonner le signal $e(t)$ avec une fréquence $f_e = 1 kHz$ pendant $t_f = 10 s$. Quel est l'intervalle de temps $t_e$ entre deux mesures? Quel est le nombre de points mesures $N$ ?
> 2. Dans la cellule suivante, créer un vecteur `tk` correspondant aux instants $t_k$ de mesures puis un vecteur `ek` correspondant aux valeurs $e(t_k)$. Réfléchir aux choix de la fonction à utiliser (`arange` ou `linspace`) aux vues des données.
> 3. Dans la même cellule, créer un vecteur `fi` contenant les fréquences auxquelles le spectre va être évalués (on rappelle qu'il aura la même taille que `ek`).
> 4. Dans la même cellule, écrire une suite d'instructions (3 instructions) qui utilise la fonction `fft` de `numpy` pour obtenir un vecteur contenant les amplitudes de la décomposition de $e(t)$ et un vecteur contenant les phases à l'origine de la décomposition de $e(t)$ à partir du vecteur `ek`. _Les fonctions `np.abs` et `np.angle` renvoient respectivement les modules et arguments d'un vecteur de complexes (sous forme de vecteur)._
> 5. Tracer dans deux graphiques différents l'allure temporelle de $e(t)$ et le spectre obtenu par les instructions précédentes.


```{code-cell} ipython3
"""On importe pour vous la fonction fft"""
from numpy.fft import fft  # Avec cette méthode d'importation, vous pouver utiliser directement la syntaxe fft(...)



```

Vous avez maintenant toutes les instructions de base pour réaliser le TP. Celui-ci vous demandera de les réutiliser mais dans des __fonctions__ pour automatiser les études.