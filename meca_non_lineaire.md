---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,py:light,md:myst
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

# Système conservatif : Effets non linéaires.

__But :__  résoudre numériquement une équation différentielle du deuxième ordre non-linéaire et faire apparaître l’effet des termes non-linéaires.

+++

## Position du problème
Nous allons chercher à résoudre numériquement l'équation d'évolution traduisant la vibration d'une molécule HCl. La différence de masse des deux atomes permet de supposer que l'atome de chlore est immobile. On travaillera donc dans son référentiel qu'on supposera galiléen. On suppose le mouvement de l'atome d'hydrogène rectiligne suivant un axe Ox (O étant la position du chlore)

Le système HCl est supposé isolé. On suppose que l'interaction intramoléculaire est modélisée par l'énergie potentielle :

$$
E_p = {C \over r^n} - \alpha {e^2 \over 4\pi \epsilon_0 r}
$$

avec : $C = 2.2 \times 10^{-138} J.m^{12}; \alpha = 0.40; n = 12; \epsilon_0 = 8.85 \times 10^{-12} SI; e=1.6\times 10^{-19}C$

et la masse de l'hydrogène : $m_H = 1.0 \times 10^{-27} kg$

Pour éviter de traiter des puissances trop importantes, on va changer les unités d'étude : la __masse__ sera en _unité de masse atomique_, les __distances__ en _Angstrom_, les __charges__ en nombre de fois _la charge élémentaire_ et  les __temps__ en _femtosecondes_. Les constantes précédentes prennent alors les valeurs suivantes (UA = Unité arbitraire):

$C = 1.4 \times 10^{-1} (UA); \alpha = 0.40; n = 12; \epsilon_0 = 3.45 \times 10^{-1} (UA); e=1 (UA); m_H = 1 (UA)$

De plus, 1 unité arbitraire d'énergie dans les résultats obtenus correspond à $100\rm{eV} = 1.6 \times 10^{-17} \rm{J}$ et 1 unité arbitraire de force correspond à $0.62 \times 10^{7} \rm{N}$
+++

### Etude de l'énergie potentielle.

> __Exercice 1__ :  
> Vous devez :
> 1. Ecrire une fonction `Ep` qui prend comme argument une distance `r` et qui renvoie l'énergie potentielle associée. _Il est conseillé d'enregistrer les variables C, alpha... comme des variables globales._
> 2. Ecrire une fonction `force` qui prend comme argument une valeur `x` et `pas` et qui renvoie la valeur de la force : $F = - \frac{dE_p}{dr}$ estimée en `x` par dérivation numérique en utilisant le pas `pas`.
> 3. Tracer $E_p(r)$ et $F(r)$ pour $r$ entre 1 et 10 Angstrom.
> 3. Déterminer, par une recherche de 0 par dichotomie, la distance `rE` correspondant à la position d'équilibre de la molécule avec une tolérance de $10^{-4} \mathring{A}$.

__Utiliser la notation scientifique 4e-4 pour entrer la valeur numérique $4\times 10^{-4}$.__

```{code-cell} ipython3
"""
N'oubliez pas les bibliothèques scientifiques 
et pensez à commenter votre code.
"""
```

## Schéma d'Euler pour un équation d'ordre 2

On rappelle le principe, on utilise deux fonctions inconnues :

$$
Y = \begin{pmatrix}
x(t)\\
v(t)
\end{pmatrix}
$$

On a alors la relation :

$$
{\rm{d} \over \rm{dt}} Y
=
{\rm{d} \over \rm{dt}}
\begin{pmatrix}
x(t)\\
v(t)
\end{pmatrix}
=
\begin{pmatrix}
v(t)\\
{\sum F_{ext}(t, Y) \over m} = f(t, Y)
\end{pmatrix}
$$

On peut alors implémenter le schéma d'Euler explicite sur le vecteur précédent :

$$
Y_{k+1} =
\begin{pmatrix}
x_{k+1}\\
v_{k+1}
\end{pmatrix}
=
\begin{pmatrix}
x_{k} + h \times v_k\\
v_k + h \times f(t, Y)
\end{pmatrix}
$$

où $h$ est le pas d'intégration.

+++

> __Exercice 2__:
> 1. Préciser l'expression de $f(t,Y(t))$ pour notre système et définir une fonction `f_hcl(t,Y)` qui renvoie cette expression.

```{code-cell}
:tags: [remove-output,hide-input]
"""
Pensez à réutiliser les fonctions déjà définies.
"""
```

## Application à l'étude de la vibration

### Effets de non linéarité
Le but est d'observer les vibrations de la molécule autour de sa position d'équilibre pour :
* une vibration de très faible amplitude : $(r - r_E) = 0.01 r_E$
* une vibration plus importante : $(r - r_E) = 0.2 r_E$

On cherchera à observer par les tracés temporelles et le portrait de phase (tracé des points $(r(t), \frac{\rm{d}r}{\rm{dt}}(t))$) si l'approximation linéaire de l'équation pourrait être valable et quelle sont les effets de non linéarité. _Note : pour un oscillateur harmonique, on attend une ellipse pour le portrait de phase__.

> __Exercice 3:__  
> Vous devez :
> 1. Définir une fonction `Ec(v)` qui renvoient l'énergie cinétique du système pour une vitesse donnée.
> 2. Utiliser `odeint` pour obtenir les temps $t_k$, positions $x(t_k)$ et vitesses $v(t_k)$ pour les deux cas étudiées puis les énergies potentielles $E_p(t_k)$, énergie cinétique $E_c(t_k)$ et énergie mécanique $E_m(t_k)$ aux temps $t_k$.
> 3. Tracer alors une fenêtre avec 4 graphiques : l'un donnant $x(t)$, le second $v(t)$, le troisième le portrait de phase $v(x)$ et le quatrième l'évolution des 3 termes énergétiques $E_p(t), E_c(t), E_m(t)$. _Adapter le pas d'intégration pour une intégration correcte._
> 5. Observer si ces évolutions sont cohérentes avec l'approximation linéaire et sinon quelles sont les différences.

```{code-cell}
:tags: [remove-output,hide-input]
"""Ne pas oublier d'importer la fonction odeint"""

```

## Trajectoire de diffusion
> __Exercice 5:__  
> 1. Comment choisir les conditions initiales pour placer l'hydrogène dans un état de diffusion ?
> 2. Réaliser l'intégration numérique dans ces conditions et déterminer numériquement l'énergie cinétique à l'infini. Obtient-on ce qu'on attend ?

```{code-cell} ipython3

```
