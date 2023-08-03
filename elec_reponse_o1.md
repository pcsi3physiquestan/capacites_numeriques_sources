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
\frac{\rm{d}y}{\rm{dt}}(t) = f(t, y(t))
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
On considère N+1 instants $t_k$ espacés d'un _pas d'intégration_ $h$ ($t_{k+1} - t_k = h$) et commençant à $t_0$. On note les valeurs de la fonctions $y$ aux instants $t_k$ $y_k = y(t_k)$. On définit ainsi deux suites $(t_k)_{k\in[0,N]}$ et $(y_k)_[k \in 0,N]$

#### Vision intégrale
Intégrons l'équation différentielle entre $t_0$ et $t_k$:

$$
\int_{t_0}^{t_k} \frac{\rm{d}y}{\rm{dt}}(t) \rm{d}t = \int_{t_0}^{t_k} f(t, y(t)) \rm{d}t
$$
soit:

$$
y(t_{k}) - y(t_0) = \int_{t_0}^{t_k} f(t, y(t)) \rm{d}t
$$

_Une méthode d'intégration numérique consiste à approcher l'intégrale du membre de droite par un calcul numérique comme on a pu le faire précédemment. Dans le cas de la méthode d'Euler, il s'agit d'approcher cette intégrale par la méthode des rectangles vue précédemment._

En pratique, on utilise une relation de récurrence comme pour le calcul d'intégrale pour calculer les termes de la suite $(t_k)$ pas à pas. En effet, de:

$$
\begin{cases}
y(t_{k}) &= y(t_0) + \int_{t_0}^{t_k} f(t, y(t)) \rm{d}t\\
y(t_{k+1}) &= y(t_0) + \int_{t_0}^{t_{k+1}} f(t, y(t)) \rm{d}t
\end{cases}
$$

```{margin}
La méthode des rectangles à droite peut aussi être utilisées mais comme elle utilise $y_{k+1}$ - alors inconnue, on dit qu'elle est _implicite_.
```
Il vient la relation de récurrence:

$$
y(t_{k+1}) = y(t_k) + \int_{t_k}^{t_{k+1}} f(t, y(t)) \rm{d}t \underbrace{\approx}_{rectangle} y(t_k) + f(t_k, y({t_k})) * h
$$

soit la récurrence qu'on appelle...

````{important} __Schéma d'Euler explicite.__
\begin{equation}
y_{k+1} = y_k + f(t_k, y_k) * h
\end{equation}
````

#### Vision différentielle
````{margin}
On parle d'approximation à l'ordre 1.
````
On peut voir aussi la méthode d'Euler comme une approximation de la dérivée par un taux de variation fini calculé pour un pas de temps $h$ choisi :

$$
\frac{\rm{d}y}{\rm{dt}} \approx \frac{y(t_{k+1}) - y(t_k)}{t_{k+1}-t_k}
$$

```{margin}
On rappelle que $t_{k+1}-t_k = h$
```
On peut ainsi déterminer la valeur de $y_{k+1}=y(t_{k+1})$ par récurrence à partir de $y_k=y(t_k)$ et $f$ :

$$
y_{k+1} = y_k + h \times f(t_k, y_k)
$$

_C'est le même schéma d'Euler_
### Synthèse

Pour résoudre numériquement une équation différentielle d'ordre 1 par la méthode d'Euler avec un pas de temps $h$, on va donc:
* définir une fonction $f(t,y)$ qui est une expression de la dérivée obtenue par l'équation différentielle:

```{margin}
La définition de $y_k$ par récurrence impose d'utiliser une boucle pour sa création.
```

$$
\frac{\rm{d}y}{\rm{dt}}(t) = f(t,y)
$$

* créer une liste temps contenant les instants $t_k = t_0 + k \times h$
* calculer une liste contenant les éléments de la suite $y_k = y(t_k)$ définie par la récurrence:

$$
y_{k+1} = y_k + f(t_k, y_k) * h
$$
avec $y_0 = y(t_0)$ la condition initiale.

<!-- ## Application en électrocinétique.
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
> 3. On veut étudier le régime transitoire, on va donc intégrer de 0 à $t_f$. Comment choisir le temps final $t_f$ pour observer complètement le régime transitoire ? En déduire le nombre de temps $t_k$ de calcul pour un pas $h$ choisi en fonction de $\tau$ et $h$. -->