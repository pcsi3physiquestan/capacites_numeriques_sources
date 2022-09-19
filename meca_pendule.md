---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,md:myst,py:light
  split_at_heading: true
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

# Etude d'un pendule simple

__But :__ à l’aide d’un langage de programmation, mettre en évidence le non isochronisme des oscillations d'un pendule.

+++

## Position du problème
Nous allons chercher à étudier les oscillations d'un pendule simple :
1. Aux petites oscillations. Ce sera l'occasion de tester le schéma d'Euler mis en place pour étudier le système en le comparant aux attentes.
2. Pour des oscillations quelconques. On cherchera alors à déterminer la période des oscillations en fonction de l'amplitude pour observer le __non isochoronisme des oscillations__. On comparera notamment les résultats trouvés à la formule théorique approchée.

### Rappel : Mise en équation
On considère un pendule simple de longueur $l$ sans sources d'amortissement dans un champ de pesanteur uniforme $g$. La masse au bout du pendule est $m$.

Pour les applications numériques, on prendra $l = 1 m; g = 9.81 m.s^{-2}; m=1 kg$.

On rappelle que la mise en équation du pendule amène à l'équation :

$$
\ddot \theta + {g \over l} \sin \theta = 0
$$

qui devient aux petits angles :

$$
\ddot \theta + {g \over l} \theta = 0
$$

L'énergie potentielle de pesanteur s'écrit :

$$
E_p(\theta) = mgl(1 - \cos \theta)
$$

et l'énergie cinétique : $E_c = {1 \over 2} m l^2 \dot \theta^2$

### Rappel : Schéma d'Euler
On va utiliser un schéma d'Euler explicite. Le système étant d'ordre 2, on utilise un système d'équations différentielles définit par la relation vectorielle :

$$
\frac{\rm{d}Y}{\rm{dt}} = F(t, Y(t))
$$

où 
$ Y(t) = \begin{pmatrix}
\theta(t)\\
\dot \theta(t)
\end{pmatrix}
$

Pour des valeurs discrètes $Y_k$ aux temps $t_k$ (on notera $x_k$ et $v_k$ les valeurs de $\theta(t)$ et $\dot \theta(t)$ aux temps $t_k$), on peut approcher la dérivée de la fonction entre $t_k$ et $t_{k+1}$ par :

$$
\frac{\rm{d}Y}{\rm{dt}} = {Y_{k+1} - Y_{k} \over t_{k+1} - t_k}
$$

soit, en notant $h = t_{k+1} - t_k$ :

$$
Y_{k+1} = Y_k + h \times F(t_k, Y(t_k))
$$

On a la relation de récurrence qui définit les $Y_k$ par le schéma d'Euler (explicite).

+++

## Implémentation du schéma d'Euler
Cette fois, on va directement raisonner avec le __vecteur $Y_k$__ et non avec deux grandeurs séparées $\theta_k$ et $\dot \theta_k$

>  __Exercice 1 :__  
> Vous devez :
> 1. Ecrire une fonction `F_petit` qui prend comme argument un flottant `t` et un vecteur `Y` à deux éléments et qui renvoie le vecteur `F(Y, t)` dans le cas d'un pendule aux petites oscillations.
> 2. Ecrire (ou plutôt réécrire en servant de ce que vous avez fait précédemment) une fonction `euler` qui prend comme arguments :
>     * une fonction `F` (semblable à `F_petit` qui prendra le même type d'arguments et renverra le même type de vecteur).
>     * un vecteur `Y0` donnant les __deux__ conditions initiales (ici à $t=0$) sur les deux composants de `Y`
>     * un flottant `h` qui sera le pas d'intégration $h = t_{k+1} - t_k$
>     * deux flottants `t0` et `tf` qui seront les temps initial et final de l'intégration.
>     et qui renvoie :
>     * un tableau à 3 colonnes contenant respectivement : les temps $t_k$, les angles $\theta_k$ et les vitesses angulaires $\dot \theta_k$.

_Données utiles :_  
* pour rappel, il est plus simple de créer une liste de vecteurs à 3 éléments qu'on transforme en tableau de N lignes et 3 colonnes.
* La sélection de la ligne d'indice i d'un tableau se fait par `tableau[i]`. Attention, les indices commencent à 0 et se terminent à N-1.
* La sélection de la colonne d'indice j d'un tableau se fait par `tableau[:,j]`. Attention, les indices commencent à 0 et se terminent à m-1.
* La sélection de l'élément d'indice (i, j) d'un tableau se fait par `tableau[i, j]`. Attention, les indices commencent à 0 et se terminent à N-1 (ou m-1).

```{code-cell} ipython3
"""
Ne pas oublier d'importer les bibliothèques scientifiques.
"""
```

## Test sur le système aux petits angles

### Intégration numérique
> __Exercice 2 :__  
> Vous devez :
> 1. Ecrire une fonction `sol_ptangle` qui prend comme argument un temps `t` et un vecteur à deux éléments `Y0` et qui renvoie la solution analytique de l'équation du pendule simple aux petits angles avec comme conditions initiales les élements du vecteur `Y0` à l'instant `t`. Cette fonction devra être vectorialisable c'est-à-dire qu'elle doit pouvoir s'appliquer correctement que `t` soit un flottant ou un vecteur numpy.
> 2. Utiliser la fonction `euler` pour résoudre numériquement le cas du pendule aux petits angles en supposant que le pendule par du point le plus bas avec une vitesse angulaire $\omega_i = .1 rad/s$. Tracer alors sur le même graphique la solution analytique et la solution numérique pour les comparer. __On réfléchira au choix du pas d'intégration et à l'intervale de temps $[0, t_f]$ d'étude.__

_Données utiles :_  
* Pour sélectionner une colonne d'un tableau, on utilise la syntaxe `tableau[:, i]` où `i` est l'indice de la colonne (qui démarre à 0).

```{code-cell} ipython3

```

### Détermination de la période.
Par la suite, le signal ne sera plus forcément sinusoïdal mais restera périodique, on va chercher à déterminer la période du signal obtenu par résolution numérique.

__Méthode choisie__ : On va déterminer les temps $t_{0i}$ successifs des points où la solution numérique pour $\theta(t)$ s'annule (plus précisément les temps médians entre deux instants où le signal change de signe). Comme il n'y a que 2 annulations des angles dans une période (cf. étude des systèmes conservatifs), il suffira de compter le nombre $N_0$ de 0. La période $T$ du signal s'écrit alors :

$$
T = {t_{0N_0} - t_{01} \over {N_0 - 1 \over 2}}
$$

> __Exercice 3 :__  
> 1. Ecrire une fonction `periode` qui prend en arguments deux vecteurs de mêmes taille `tk` et `thetak` et qui renvoie la période du signal `thetak` en considérant les `tk` comme les temps associés.
> 2. Tester votre fonction sur le signal intégré numériquement pour vérifier que vous trouvez bien la bonne période.

```{code-cell} ipython3

```

## Anisochronisme des grandes oscillations.
On a observé théoriquement que la période des oscillations dépendaient aux fortes amplitudes des oscillations. Pour une amplitude "pas trop forte", une approximation de l'intégrale trouvée en TD amène à la formule dite de Borda :

$$
T \approx T_0 (1 + {\theta_0 ^2 \over 16})
$$

avec $T_0$ la période propre aux petites oscillations


> __Exercice 4 :__
> 1. Pour une liste d'amplitude angulaire entre 0 et $\pi$ (non inclus) (5 valeurs), vous devez :
>     * Procéder à l'intégration numérique de l'évolution de l'angle _sans approximation_ pour l'amplitude considérée et la solution analytique aux petits angles
>     * Tracer sur deux graphiques : l'évolution temporelle de $\theta(t)$ et le portrait de phase $(\theta(t), \frac{\rm{d}\theta}{\rm{dt}}(t))$ du pendule our l'amplitude considérée.
>     * Comparer à chaque fois la solution aux petits angles et la solution numérique trouvée.
> 2. Ecrire une fonction `periode_borda` qui renvoie pour une amplitude `theta0` donnée la période approchée par la formule de Borda
> 2. Pour une liste d'amplitude angulaire entre $\pi / 50$ et $\pi$ (non inclus) (49 valeurs), vous devez déterminer pour chaque amplitude la période des oscillations pour le signal obtenu numériquement $T_{num}(\theta_0)$ et par la formule de Borda $T_{Borda}(\theta_0)$ puis représenter les deux périodes en fonction de l'amplitude.
>     * Observer alors l'anisochronisme des oscillations
>     * Comparer les résultats obtenus par l'intégrale et par intégration numérique de l'équation différentielle. A partir de quand doit-on considérer la formule de Borda non acceptable.

```{code-cell} ipython3

```

## Trajectoire de diffusion
On s'intéresse au cas où le pendule part de sa position la plus basse avec une vitesse angulaire $\omega_i$.

> __Exercice 5 :__  
> 1. Déterminer par le calcul la pulsation $\omega_i$ qui permet d'atteindre l'angle $\pi$ et de s'y arrêter. En théorie, quel temps met-on pour atteindre ce point ?
> 2. Intégrer l'équation du pendule avec la valeur de $\omega_i$ précédente et observer l'allure de $\theta(t)$ et $\dot \theta(t)$. Commenter
> 3. Intégrer l'équation du pendule avec une valeur de $\omega_i$ supérieure à celle trouvée précédemment et observer l'allure de $\theta(t)$ et $\dot \theta(t)$. Commenter.

```{code-cell} ipython3

```
