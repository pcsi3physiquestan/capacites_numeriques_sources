---
jupytext:
  formats: ipynb,md:myst,py:light
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
La page ci-présente existe en version notebook téléchargeable grâce au bouton ![Bouton](./images/bouton_tl.png) (choisir le format `.ipynb`). On rappelle qu'il faut ensuite l'enregistrer dans un répertoire adéquat sur votre ordinateur (`capa_num` par exemple dans votre répertoire personnel) puis lancer Jupyter Notebook depuis Anaconda pour accéder au notebook, le modifier et exécutez les cellules de code adéquates.

# Implémentation basique

## Définition des fonctions pour le schéma d'Euler
On va commencer par définir la fonction $f(t,y)$ pour quelques équations différentielles:

* $\frac{\rm{d}y_1}{\rm{dt}} + \sin(t) * y_1(t) =2$ avec $y_1(t=0) = 0$
* $\exp(t) * \frac{\rm{d}y_2}{\rm{dt}} + \cos(t) * y_2(t)^2 = 0$ avec $y_2(t=0) = 1$
* $\frac{\rm{d}y_3}{\rm{dt}} + \frac{\exp(y_3(t))}{5} = 3 \sin t$ avec $y_3(t=0) = 0$

Pour chaque cas, on réalisera une intégration jusqu'à $t = 10$.

> __Exercice 1:__  
> Dans la cellule ci-après, vous devez:
> 1. Importer les deux bibliothèques `numpy` et `matplotlib.pyplot`
> 2. Créer trois fonctions `f1(t:float, y:float) -> float, f2(t:float, y:float) -> float` et `f3(t:float, y:float) -> float` prenant __deux arguments__ `t` et `y` (correspondant à un instant $t_k$ et à $y_k = y(t_k)$) et qui renvoie la valeur $f_{1,2, 3}(t_k, u_k)$ pour chaque cas où $f_i$ est l'expression que vous aurez trouvez de la dérivée grâce à l'équation différentielle (cf. la [position du problème expliquée précédemment](pospb)).  
__Attention : Même si $f3$ ne dépend pas explicitement du temps, on gardera $t$ comme argument de la fonction car cet argument est nécessaire quand on utilisera les fonctions natives de `numpy` pour intégrer une équation différentielle.__

```{code-cell} ipython3
:tags: [hide-input, remove-output]
"""Ne pas oublier d'importer les bibliothèques scientifiques et d'éxécuter la cellule."""
```

## Implémentation du schéma d'Euler

_On propose d'écrire d'abord une série d'instructions puis de transformer cette série d'instructions en une fonction. Si vous vous sentez assez à l'aise, vous pouvez directement passer à l'exercice 4 pour créer directement la fonction._

> __Exercice 2__ : Avec une boucle for  
> 1. Ecrire une suite d'instructions qui:
>     * (Préparation) Définit le pas `h` ($h = 0.1$), l'instant initial `t_0`, le temps final `t_f`, la condition initiale `y0`, et le nombre d'intégration `N` à réaliser.
>     * (Initialisation) Créer deux __listes__ vide `tkf` et `ykf` dans lesquels on stockera les valeurs $t_k$ et $y_k$ puis ajouter à ces listes les conditions initiales $t_0$ et $y_0$.
>     * (Boucle) Dans une boucle for, réalise plusieurs fois l'intégration numérique avec le pas `h` et la fonction `f1`. A chaque fois, vous devrez calculer la valeur $y_{k+1}$ que vous stockerez dans la liste `ykf` puis le nouveau temps $t_{k+1}$ que vous stockerez dans la liste `tkf`. Bien réfléchir aux bornes de la boucle.
>     * (Terminaison) Pour une utilisation plus simple ensuite des listes de valeurs `tkf` et `ykf`, transformer les deux listes en deux vecteurs `numpy` (fonction `numpy.array`).
> 2. Tracer $y1(t)$.
> 3. Pour comprendre en pratique le principe de la méthode d'Euler, ajouter les instructions suivantes (pas à connaître) puis réfléchir à ce qui a été tracé et au lien avec la méthode d'Euler.

```{code-block}
# On suppose que matplotlib.pyplot a été importé avec l'alias plt et numpy avec l'alias np
t, y = np.linspace(min(tkf),max(tkf),20), np.linspace(min(ykf),max(ykf),20)
tgrid, ygrid = np.meshgrid(t, y)
plt.quiver(tgrid, ygrid, np.ones((len(t), len(y))), f1(tgrid,  ygrid), angles='xy')
```

```{code-cell} ipython3
:tags: [hide-input, remove-output]

```

> __Exercice 3__ : Avec une boucle while  
> 1. Ecrire une suite d'instructions qui:
>     * (Préparation) Définit le pas `h`, l'instant initiale `t_0`, le temps final `t_f`, la condition initiale `y0`.
>     * (Initialisation) Créer deux __listes__ vide `tkw` et `ykw` dans lesquels on stockera les valeurs $t_k$ et $y_k$ puis ajouter à ces listes les conditions initiales $t_0$ et $y_0$.
>     * (Boucle) Dans une boucle while, réalise plusieurs fois l'intégration numérique avec le pas `h` et la fonction `f2`. A chaque fois, vous devrez calculer la valeur $y_{k+1}$ que vous stockerez dans la liste `ykw` puis le nouveau temps $t_{k+1}$ que vous stockerez dans la liste `tkw`. Bien réfléchir à la condition de sortie de la boucle.
>     * (Terminaison) Pour une utilisation plus simple ensuite des listes de valeurs `tkw` et `ukw`, transformer les deux listes en deux vecteurs `numpy` (fonction `numpy.array`).
> 2. Tracer $y2(t)$.
> 3. Utiliser la même série d'instructions que pour la boucle for pour visualiser à nouveau le principe de la méthode d'Euler.


```{code-cell} ipython3
:tags: [hide-input, remove-output]

```

> __Exercice 4__ : Dans une fonction  
> 1. Ecrire maintenant une fonction `euler(f:callable, y0:float, t0: float, tf: float, pas:float) -> (numpy.ndarray, numpy.ndarray)` qui, prenant pour argument la fonction `f` définie dans le schéma d'Euler, la condition initiale `y0`, les temps initiaux et finaux `t0` et `tf` et le `pas` d'intégration, renvoie deux __vecteurs numpy__ contenant respectivement les $t_k$ et les $y_k$. Vous pouvez utiliser une boucle for ou while comme vous voulez.
> 2. Tester votre fonctions sur `f1, f2, f3` et vérifier que vous obtenez les mêmes résultats que précédemment.



```{code-cell} ipython3
:tags: [hide-input, remove-output]

```

### Influence du pas d'intégration
> __Exercice 5__ :
> 1. Utiliser la fonction `euler` précédente en changeant le pas d'intégration pour `f1`. Que se passe-t-il quand ce pas devient grand?
> 2. En déduire comment choisir correctement le pas d'intégration.

```{code-cell} ipython3
:tags: [hide-input, remove-output]
```

## Fonctions des bibliothèques scientifiques
````{margin}
Les méthodes d'intégration par défaut de ces fonctions sont un peu plus complexe et précises que le schéma d'Euler explicite mais l'idée générale reste la même.
````
Il existe deux fonctions appartenant au modulke `scipy.integrate` permettant de réaliser l'intégration numérique d'une équation différentielle d'ordre 1:
* `solve_ivp(f:callable, t_span:(float, float), y0:float, t_eval=numpy.ndarray) -> dict`
    * Ses arguments sont:
        * `f` : la fonction du schéma d'Euler, comme pour notre fonction `euler`
        * `t_span` : un tuple de deux valeurs : $t_0$ et $t_f$.
        * `y0` : condition initiale
        * `t_eval` : la liste (ou vecteur) des instants $t_k$ où l'on veut estimer la fonction.
    * Elle renvoie un __dictionnaire__ dont les clés utiles sont (on a assigner le retour à une variable `solution`pour l'exemple):
        * `solution['t']` : vecteur des instants où $y(t) a été évaluées (donc identique à  `t_eval`)
        * `solution['y']` : __tableau__ dont chaque __ligne__ est un vecteur donnant la solution (cf. suite). Pour notre équation d'ordre 1, il n'y a donc qu'une ligne (une seule fonction inconnue) ainsi, pour obtenir le vecteur solution, il faut écrire `solution['y'][0]`.
* `odeint(f:callable, y0:float, t:numpy.ndarray, tfirst=True)` -> numpy.ndarray
    * Ses arguments sont:
        * `f` : la fonction du schéma d'Euler, comme pour notre fonction `euler`
        * `y0` : condition initiale
        * `t` : la liste (ou vecteur) des instants $t_k$ où l'on veut estimer la fonction.
        * `tfirst` : booléan mis à `True` pour préciser que le premier argument de `f1, f2, f3` est `t` (et pas y).
    * Elle renvoie un __tableau numpy__ donc chaque __colonne__ est la solution pour une fonction inconnue. Pour notre équation d'ordre 1, il n'y a donc qu'une colonne (une seule fonction inconnue) ainsi, pour obtenir le vecteur solution, il faut écrire `solution[:, 0]` (toute les lignes, premières colonne).


> __Exercice 6__ :
> 1. Utiliser les fonctions `solve_ivp` et `odeint` pour retrouver les solutions des équations différentielles précédentes et vérifier la cohérence avec les résultats précédents.