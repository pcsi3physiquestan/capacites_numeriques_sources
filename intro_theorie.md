---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,md:myst
  split_at_heading: true
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Approche théorique

Il est important d'obtenir les relations théoriques d'étude AVANT de se lancer dans la programmation. Le but est de relier théoriquement les coordonnées d'un point image à celle d'un point objet et des caractéristiques de la lentille qui les conjugue.

__On rappelle que l'origine des coordonnées sur l'axe optique est situé au point $O$.__ Il correspond aussi à l'origine de la coordonnée transverse d'un point. On considère :
* Un point objet B dont les __coordonnées__ sont :
    * $x_B$ sa coordonnée sur l'axe optique (position longitudinale)
    * $d_B$ sa coordonnée transverse (position tranvsersale)
* Une lentille :
    * de distance focale image $f'$
    * dont le centre optique $O_L$ est situé à la coordonnées $x_L$
* Le point $B_1$, image de $B$ par la lentille $L$. Ses __coordonnées__ sont:
    * $x_{B1}$ sa coordonnée sur l'axe optique (position longitudinale)
    * $d_{B1}$ sa coordonnée transverse (position tranvsersale)

````{admonition} Exercice
:class: tip
Exprimer $x_{B1}$ et $d_{B1}$ en fonction de $x_B$, $d_B$, $f'$ et $x_L$.  
_Conseil:_ Faites un schéma en représentant les différentes grandeurs.
````
```{hint}
_Indications utiles_ :
* Attention à ne pas confondre la position absolue sur un axe et une distance relative entre deux éléments (cf. théorie).
```
````{hint}
:class: dropdown
Si vous avez des difficultés. Voici ce que vous devez trouver.
Montrer que:
\begin{equation}
\begin{cases}
x_{B1} &= x_L + \frac{f' \times (x_B - x_L)}{f' + x_B - x_L}\\
d_{B1} &= d_{B} \times \frac{x_{B1} - x_L}{x_{B} - x_L}
\end{cases}
\end{equation}
````
