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

# Système d'équations et ordre 2
Le but est de voir comment utiliser la méthode d'intégration d'Euler explicite pour étudier le régime transitoire d'un système d'équations. On a alors un système d'équations différentielles. La théorie relative à la méthode d'intégration par Euler explicite ayant déjà été donnée, nous allons ici partir d'un exemple pour comprenre sa généralisation à des systèmes d'ordre supérieurs.

## Système d'équations - Position du problème
On s'intéresse au système d'équations différentielle suivant :

$$
\begin{cases}
\frac{\rm{d}u}{\rm{dt}} = - \frac{1}{\tau} v - \frac{2}{\tau}u\\
\frac{\rm{d}v}{\rm{dt}} = - \frac{1}{\tau} v - \frac{1}{\tau}u
\end{cases}
$$

### Vision vectorielle
Le système d'équations différentielles précédent peut être vu comme une seule équation différentielle d'ordre 1 faisant un intervenir des vecteurs:
>
$$ {\rm{d} \over \rm{d}t}
\begin{pmatrix}
u\\
v
\end{pmatrix}
=
\begin{pmatrix}
- {1 \over \tau} v - {2 \over \tau} u\\
- {1 \over \tau} v - {1 \over \tau} u
\end{pmatrix}
$$

soit, en définissant le vecteur:

$$ Y(t)=
\begin{pmatrix}
u(t)\\
v(t)
\end{pmatrix}
$$

Sa dérivée est:

\begin{equation}
{\rm{d}Y \over \rm{d}t} = F(t, Y(t))
\end{equation}

avec :

$$ F(t, Y(t)) = 
\begin{pmatrix}
- {1 \over \tau} v(t) - {2 \over \tau} u(t)\\
- {1 \over \tau} v(t) - {1 \over \tau} u(t)
\end{pmatrix}
$$

_On rappelle que d'un point de vue vectoriel:_

* `u = Y[0]` et `v = Y[1]`.
* `F` prend comme argument un vecteur `Y` (de taille 2) et renvoie un vecteur de taille 2.
* On n'a techniquement pas besoin du temps puisque `F` ne dépend pas explicitement du temps mais on prendra l'habitude de le mettre comme argument même si on ne l'utilise pas (pour des fonctions comme `solve_ivp`).

### Schéma d'Euler
Le principe du schéma d'Euler est alors identique au cas d'ordre 1 avec une seule fonction:

$$
Y_{k+1} \approx Y_k + F(t_k, Y_k) \times h
$$
avec $Y_{k} = Y(t_k)$ et $h = t_{k+1} - t_k$

__Dans l'expression précédente, la somme correspond à la somme vectorielle (somme des coordonnées terme à terme $\overrightarrow{w_1} + \overrightarrow{w_2}$) et la multiplication à la multiplication d'un vecteur par un scalaire ($\lambda \overrightarrow{w}$).__

__Il faudra juste veiller à ce que la fonction $F$ renvoie un vecteur numpy et que $y_0$ soit un vecteur numpy dans les programmes (de manière à faciliter la somme vectorielle et la multiplication par un scalaire - pas besoin de boucle).__ Les valeurs $u_k$ et $v_k$ calculées aux instant $t_k = t_0 + hk$ sont alors stockées dans deux vecteurs numpy (on pourra les rassembler dans un seul tableau numpy à deux colonnes comme le fait `odeint`  _(ce que fera naturellement la fonction `euler` créée dans la partie précédente)_ ou à deux lignes comme le fait `solve_ivp`.

+++

(sys_o2)=
## Système d'ordre 2

Lors qu'on doit résoudre un système d'ordre 2 du type:

$$
\frac{\rm{d^2}y}{\rm{dt^2}} = G(t, y(t), \frac{\rm{d}y}{\rm{dt}}(t))
$$

on peut toujours le réécrire sous la forme d'un système d'équations différentielles d'ordre 1 où les deux fonctions inconnues sont:

$$ Y(t)=
\begin{pmatrix}
u(t) = y(t)\\
v(t) = \dot y(t)
\end{pmatrix}
$$

En effet, la dérivée de $Y$ est:

\begin{equation}
{\rm{d}Y \over \rm{d}t} =
\begin{pmatrix}
\dot y(t)\\
\ddot y(t)
\end{pmatrix}
=

\begin{pmatrix}
v(t)\\
g(t, u(t), v(t))
\end{pmatrix}
\end{equation}

On peut donc se ramener au cas précédent en posant:

$$ F(t, Y(t)) = 
\begin{pmatrix}
v(t)\\
g(t, u(t), v(t))
\end{pmatrix}
$$

La méthode permettant de résoudre un système d'équation permettra donc aussi de résoudre un système d'ordre 2 (et on obtient en prime la dérivée de la solution aux instants $t_k$).