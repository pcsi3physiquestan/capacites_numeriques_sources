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

# Utilisation de fonctions

Par la suite, on sera amené à réutiliser l'intégration et la dérivation numérique sur des vecteurs de valeurs comme réalisée dans [la dernière partie](cas_exp). On va donc écrire deux fonctions `deriv` et `integ` qui vont réaliser respectivement :
* la dérivation numérique d'une fonction $f$ donnée par un vecteur de valeurs `yk` et les instants de mesure `tk`: calcul des $f'(t_k)$
* la primitivation numérique d'une fonction $f$ donnée par un vecteur de valeurs `yk` et les instants de mesure `tk`: calcul des $I_k = \int_{t_0}^{t_k} f(t) dt$


On testera les deux fonctions grâce aux fichier de données utilisé [précédemment](https://github.com/pcsi3physiquestan/donnees_exp/blob/main/circuit_rc.dat?raw=true)

## Création des fonctions
> __Exercice 1:__  
> 1. Ecrire une fonction `deriv(x,y)` qui prend comme argument deux vecteur `x` et `y` contenant le même nombre de valeur et qui renvoie le calcul de la dérivée pour chaque abscisse $x_k$ de `x` de la fonction $f$ qui aurait les valeurs $y_k = f(x_k)$ (les $y_k$ sont les éléments de `y`). Comme [précédement](cas_exp), on réalisera une dérivation centrée sauf en $x_0$ (dérivation à droite) et en $x_{finale}$ (dérivation à gauche).
> 2. Ecrire une fonction `inter(x,y)` qui prend comme argument deux vecteur `x` et `y` contenant le même nombre de valeur et qui renvoie le calcul des intégrales $I_k = \int_{x_0}^{x_k} f(x) dx$ pour chaque abscisse $x_k$ de `x` où la fonction $f$ aurait les valeurs $y_k = f(x_k)$ (les $y_k$ sont les éléments de `y`). Comme [précédement](cas_exp), on réalisera une intégration par la méthode des trapèzes.

```{code-cell}
:tags: [remove-output,hide-input]

```

## Test des fonctions

> __Exercice 2:__  
> 1. Charger comme [précédemment](cas_exp) les données dans deux vecteurs `tk` et `ukb` puis obtenir les valeurs de tension en volt dans un vecteur `uk`
> 2. Utiliser les fonctions `deriv` et `integ` créés précédemment pour obtenir $i(t)$ et $E_J(t)$ puis les tracer.

```{code-cell}
:tags: [remove-output,hide-input]

```