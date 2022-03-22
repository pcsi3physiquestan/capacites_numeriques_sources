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

# Etude du redressement monoalternance
Nous allons utiliser la méthode précédente pour chercher le point de fonctionnement du [circuit précédent](pos_pb_eq) à chaque instant $t$ en supposant que $E$ varie: $E(t) = E_0 \cos (2 \pi f t)$ avec $E_0 = 2 \rm{V}$ et $f = 50 \rm{Hz}$.

On suppose que les caractéristiques des dipôles restent valables en régime variable de sorte qu'à un instant $t$, la tension $u_D$ est donnée par la solution de l'équation:

$$
  f(u) = \frac{E(t)-u}{R} - I_s\left(\exp \left(\frac{u}{V_T}\right) - 1\right)
$$
avec $I_s = 95 \rm{\mu A}$ et $V_D = 30 \rm{mV}$ et $t$ un instant connu.

On va donc devoir réaliser une recherche de racine un grand nombre de fois. Il est donc préférable de mettre la série d'instructions pour déterminer la racine de $f$ dans une fonction.

## Fonction pour résoudre

> __Exercice 1:__  
> 1. Importer les bibliothèques `numpy` et `matplotlib.pyplot`
> 1. Définir une fonction `Esource(t)` qui renvoie la valeur de $E(t)$ pour un instant $t$ donné en argument et une fonction `f_test(u)` qui renvoie la valeur de $f$ pour une tension $u$ donnée en argument de la fonction (elle utilisera une valeur `E` de tension pour la source comme une variable globale, les autres grandeurs Is, VT... peuvent être définie dans la fonction `f_test`, cf remarque par la suite).
> 1. _(Si ça na pas été fait précédemment)_ Tracer la fonction $f$ entre $[-1,1]$ pour $t = 0$ (donc $E = 2\rm{V}$) et vérifier graphiquement qu'il n'y bien qu'une seule racine dans l'intervalle (_Note: On peut démontrer que la fonction est strictement décroissante, on a donc bien unicité de la racine quand elle existe._)

__Remarque__:  
Le code ressemblera donc à ceci:

```{code-block}
def Esource(t):
  # corps du code si necessaire
  return ....

def f_test(u):
  # corps du code si necessaire
  # La tension E sera notée E sans être définie par exemple :
  R = 100
  i = (E - u) / R
  return i

# Pour utiliser f_test:
E = 1  # Nécessaire
f_test(u)
# On pourra redéfinir E avant chaque appel de f_test si nécessaire
```

```{code-cell}
:tags: [remove-output,hide-input]

```

> __Exercice 2:__  
> 1. Ecrire une fonction `dicho(f,a0,b0,prec)` qui va chercher la racine de la fonction `f` dans l'intervalle initiale $[a0,b0]$ avec une précision `prec` par la méthode de dichotomie.
> 2. Tester la fonction avec `f_test` et $E = 2\rm{V}$ et vérifier la cohérence avec ce qu'on obtient graphiquement.

* L'argument `f` est la __fonction__ donc `f` ou `f_test`, pas _ce qu'elle renvoie_ (c'est-à-dire `f(0)` ou `f_test(1)`, _on a la même différence entre une fonction et l'image d'une fonction_).
* Par contre, à l'intérieur de `dicho`. Comme `f` est une fonction, on pourra l'appeler en utilisant `f(a)`, `f(1)`...
* On ne modifier __jamais__ la valeur d'un argument (ici `a0` et `b0`) donc il faut les réassigner à deux variables internes à la fonction (`a` et `b` ?) et modifier ces deux variables dans la boucle.
* Il est conseillé de tester initialement si le produit $f(a0)f(b0)$ est bien négatif et renvoyer `None` sinon. Cela évitera des résultats absurdes si l'on cherche dans un intervalle où il n'y a pas de racine. _Quand vous aurez avancé le cours d'informatique, vous pourrez remplacer ce comportement par le renvoie d'une erreur ou Exception._

```{code-cell}
:tags: [remove-output,hide-input]

```

## Application au redressement monoalternance
> __Exercice 3:__  
> Ecrire une suite d'instruction:
> 1. Définir un vecteur `E_k` qui prendre 1000 valeurs de $E(t)$ aux instants $t_k$ équirépartis sur 2 périodes de $E(t)$.
> 2. Dans une boucle, pour chaque valeur de $E_k$, rechercher la tension $u_D$ correspondant et la stocker dans une liste.
> 3. Transformer la liste des tensions `uD` en un vecteur puis obtenir les valeurs d'intensités correspondantes $i(t)$ (pensez aux fonctions vectorialisables pour l'obtenir en une instruction).
> 4. Obtenir les valeurs de la tension $uR$ à chaque instant et tracer $u_R (t)$. Pourquoi parle-t-on de redressement ? monoalternance ?

* Note : Réfléchir au choix de l'intervalle de recherche.
```{code-cell}
:tags: [remove-output,hide-input]

```