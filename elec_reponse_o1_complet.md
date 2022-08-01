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
La page ci-présente existe en version notebook téléchargeable grâce au bouton ![Bouton](./images/bouton_tl.png) (choisir le format `.ipynb`). On rappelle qu'l faut ensuite l'enregistrer dans un répertoire adéquat sur votre ordinateur (`capa_num` par exemple dans votre répertoire personnel) puis lancer Jupyter Notebook depuis Anaconda pour accéder au notebook, le modifier et exécutez les cellules de code adéquates.

# Implémentation complète

## Implémentation du schéma d'Euler

> __Exercice 1__
> 1. Commencer par importer les bibliothèques scientifiques utiles : numpy, matplotlib.pyplot
> 2. Ecrire une fonction `euler` 
>     * qui prend en arguments :
>         * une variable `f` qui sera une fonction
>         * un flottant `y0` correspond à y(t=0)
>         * un flottant `h` qui sera le pas $h$ d'intégration
>         * deux flottants `t0` et `tf` donnant les temps initiaux et finaux de l'intervalle sur lesquels on va intégrer le signal (Note : `tf` ne sera pas forcément atteint)
>     * et qui renvoie deux vecteurs numpy : 
>         * le premier contient les temps $t_k$ où on a évaluer la fonction (on commence à `t0`)
>         * le second contient les valeurs estimées de $y(t_k)$ ($y_k$).

```{code-cell} ipython3
:tags: [hide-input, remove-output]
"""Ne pas oublier d'importer les bibliothèques scientifiques"""
```

## Application au régime libre et à l'échelon de tension.
__On prendra $\tau = 1$.__ Il s'agit de vérifier que la fonction précédente fonctionne correctement. _Si vous avez fait la comparaison dans l'étude de base, vous pouvez réutiliser une bonne partie du code pour le tracé graphique en choisissant bien le nom de vos variables._

> __Exercice 2__
> 1. Préciser l'expression de la fonction $f(t, y)$  dans le cas d'un régime libre et d'un échelon de tension ($E = 1V$) puis implémenter deux fonctions `f_libre` et `f_echelon` correspondant à ces fonctions (mettre les arguments `t` et `y` même s'ils n'interviennent pas dans la fonction).
> 2. Définir deux fonctions `sol_libre` et `sol_echelon` qui prennent comme argument `t`, `t1` et `y0` et qui renvoient respectivement les solutions pour un régime libre puis pour un échelon de tension avec comme condition initiale $y(t1) = y0$.
> 3. Utiliser le schéma d'Euler que vous avez implémenté pour résoudre numériquement le cas d'un régime libre et d'un échelon de tension. Choisir un pas d'intégration $pas = \frac{1}{1000} \tau$
> 4. Tracer sur le même graphique la réponse numérique et la réponse analytique pour un régime libre puis pour un échelon de tension.

```{code-cell} ipython3
:tags: [hide-input, remove-output]
"""La fonction euler que vous avez défini précédemment est accessibles"""
```

## Erreur et pas d'intégration
__Inutile de faire cette partie si vous l'avez dans l'étude de base.__

> __Exercice 3__
> 1. Reprendre l'exercice précédent mais en affichant deux graphiques (1 colonne et deux lignes) : les solutions analytique et numérique précédentes sur le premier et la valeur absolue des écarts entre les deux solutions sur le second graphique.
> 2. Etudier l'évolution des erreurs en fonction du pas d'intégration (commencer par un pas égal à $\tau$ puis diviser successivement par 5 le pas).

Pour vous aider sur la manière de tracer une fenêtre multi-graphique, utiliser cet [élément de cours](https://pcsi3physiquestan.github.io/intro_python/notebook/plus_loin.html).

_Informations utiles_:
* Vous pouvez tout à fait créer un tracé (`ax[0].plot(...)`) à l'intérieur d'une boucle pour superposer plusieurs courbes.

```{code-cell} ipython3
:tags: [hide-input, remove-output]

```

