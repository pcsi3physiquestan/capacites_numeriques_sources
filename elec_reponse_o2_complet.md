---
jupytext:
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

# Etude directe d'un système d'ordre 2

On va étudier directement un système d'ordre 2 issu d'un problème de mécanique: le pendule simple sans frottement. L'équation qui régit l'évolution de l'angle $\theta(t)$ que fait le pendule avec un axe horizontal est:

$$
\frac{\rm{d^2}\theta}{\rm{dt^2}} = - \omega_0^2 \sin \theta
$$

avec $\omega_0 = \sqrt{\frac{g}{l}}$ ($l=1\rm{m}$ est la longueur du fil du pendule et $g=9.81 \rm{m.s^{-2}}$ l'intensité du champ de pesanteur).

> __Exercice 1:__  
> 1. Si l'on pose le vecteur `Y(t) = (\theta(t), \dot \theta(t))`, écrire la fonction `F` associée au schéma d'Euler puis utiliser la fonction `euler` (la réécrire dans la cellule suivante pour pouvoir l'utiliser) pour obtenir $\theta(t)$ si $\theta(0) = \pi /4$ et $\dot \theta(0) = 0$

```{code-cell}
:tags: [remove-output,hide-input]

```