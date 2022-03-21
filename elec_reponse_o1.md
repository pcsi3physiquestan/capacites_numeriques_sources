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

# Résolution numérique d'une équation différentielle d'ordre 1

__But :__ mettre en œuvre la méthode d’Euler à l’aide d’un langage de programmation pour simuler la réponse d’un système linéaire du premier ordre à une excitation de forme quelconque.

## Rappels sur la méthode d'Euler

La _méthode d'Euler_ est une méthode numérique d'intégration d'une équation différentielle.

(pospb)=
### Position du problème.
Un équation différentielle d'ordre 1 peut se mettre sous la forme :

$$
\frac{\rm{d}y}{\rm{dt}}(t) = f(t, y)
$$
avec $y(t_0) = y_0$

où $y$ est la fonction inconnue.


> Exemple : Pour un circuit RC série relié à une tension de tension $E(t)$, l'équation d'évolution est :
> 
> $$\frac{\rm{d}u}{\rm{dt}} = \frac{1}{RC}\left (E(t) - u(t) \right )$$
> 
> La fonction $f$ est donc :
> 
> $$f(t, u) = \frac{1}{RC}\left (E(t) - u(t) \right )$$

### Schéma d'intégration d'Euler explicite

La méthode d'Euler consiste à approximer la dérivée par un taux de variation fini calculé pour un pas de temps $h$ choisi :

$$
\frac{\rm{d}y}{\rm{dt}} \approx \frac{y(t + h) - y(t)}{h}
$$
(on parle d'approximation à l'ordre 1.)

On peut ainsi déterminer la valeur de la fonction $y(t + h)$ à partir de $f$ et de la valeur de la fonction à l'instant $t$ :

$$
y(t + h) = y(t) + h \times f(t, y(t))
$$

On ne va donc pas calculer la fonction $y(t)$ pour tout instant $t$ mais une suite de valeurs $y_k$ aux instants $t_k = t_0 + k\times h$ avec $k$ entier. On obtient une suite $(y_k)$ définie par la récurrence :

$$
y_{k+1} = y_k + h \times f(t, y_k)
$$

### Synthèse

Pour résoudre numériquement une équation différentielle d'ordre 1 par la méthode d'Euler avec un pas de temps $h$, on va donc:
* définir une fonction $f(t,y)$ qui est une expression de la dérivée obtenue par l'équation différentielle:

$$
\frac{\rm{d}y}{\rm{dt}}(t) = f(t,y)
$$
* créer un vecteur temps contenant les instants $t_k = t_0 + k \times h$
* calculer un vecteur contenant les éléments de la suite $y_k = y(t_k)$ définie par la récurrence:

$$
y_{k+1} = y_k + f(t_k, y_k) * h
$$
avec $y_0 = y(t_0)$ la condition initiale.

_La définition de $y_k$ par récurrence impose d'utiliser une boucle pour sa création._

## Application en électrocinétique.
On traite le cas général d'un système d'ordre 1 stable de constante de temps $\tau$. On va notamment étudier la réponse à plusieurs entrées :
* un régime libre et un échelon de tension. On comparera avec la réponse attendue pour tester l'intégration numérique.
* une rampe de tension suivie d'une tension constante.

On étudiera l'influence du pas d'intégration sur la fiabilité de l'intégration numérique.

(miseq)=
### Mise en équation
> __Etude théorique__
> On travaille avec un circuit $RC$ série dont la constante de temps est $\tau = RC$. On prendra $R = 10\rm{k\Omega}$ et $C = 100 \rm{\mu F}$.  
> 1. Dans le cas d'un régime libre, préciser l'expression de la fonction $f(t,y)$. Dépend-elle explicitement de $t$?
> 2. Dans le cas où le RC est relié à une source $E = 1V$, préciser l'expression de la fonction $f(t,y)$. Dépend-elle explicitement de $t$?
> 3. On veut étudier le régime transitoire, on va donc intégrer de 0 à $t_f$. Comment choisir le temps final $t_f$ pour observer complètement le régime transitoire ? En déduire le nombre de temps $t_k$ de calcul pour un pas $h$ en fonction de $\tau$ et $h$.