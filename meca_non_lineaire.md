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

$C = 2.2 \times 10^{-1} (UA); \alpha = 0.40; n = 12; \epsilon_0 = 3.45 \times 10^{-1} (UA); e=1 (UA); m_H = 1 (UA)$

+++

### Etude de l'énergie potentielle.

> __Exercice 1__ :  
> Vous devez :
> 1. Ecrire une fonction `Ep` qui prend comme argument une distance `r` et qui renvoie l'énergie potentielle associée. _Il est conseillé d'enregistrer les variables C, alpha... comme des variables globales._
> 2. Ecrire une fonction `force` qui prend comme argument une valeur `x` et `pas` et qui renvoie la valeur de la force : $F = - \frac{dE_p}{dr}$ estimée en `x` par dérivation numérique en utilisant le pas `pas`.
> 3. Tracer $E_p(r)$^et $F(r)$ pour $r$ entre 1 et 10 Angstrom.
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
\begin{pmatrix}
x(t)\\
v(t)
\end{pmatrix}
$$

On a alors la relation :

$$
{\rm{d} \over \rm{dt}}
\begin{pmatrix}
x(t)\\
v(t)
\end{pmatrix}
=
\begin{pmatrix}
v(t)\\
{\sum F_{ext}(t, x, v) \over m} = f(t, x, v)
\end{pmatrix}
$$

On peut alors implémenter le schéma d'Euler explicite sur le vecteur précédent :

$$
\begin{pmatrix}
x_{k+1}\\
v_{k+1}
\end{pmatrix}
=
\begin{pmatrix}
x_{k} + h \times v_k\\
v_k + h \times f(t, x, v)
\end{pmatrix}
$$

où $h$ est le pas d'intégration.

+++

> __Exercice 2__:
> 1. Préciser l'expression de $f(t, x, v)$ pour notre système et définir une fonction `f_hcl(t, x, v)` qui renvoie cette expression.
> 2. Définir une fonction `euler` qui prend pour argument : 
>    * `f` : la fonction du schéma d'Euler
>    * `h` : le pas d'intégration choisi
>    * `x0` et `v0` : les conditions initiales sur la position et la vitesse au temps initial $t=0$
>    * `tf` : le temps final pour l'intégration.
>  
>    et qui renvoie trois vecteurs :  
>    * `tk` les temps où on calcule les positions vitesses
>    * `xk` les positions $x(t_k)$
>    * `vk` les vitesses $v(t_k)$
> 3. Vous pouvez tester votre fonction sur une chute libre ($f(t, x, v) = g = 10$) avec un faible nombre de points.

```{code-cell} ipython3
"""
Pensez à réutiliser les fonctions déjà définies.
"""
```

## Application à l'étude de la vibration

### Effets de non linéarité
Le but est d'observer les vibrations de la molécule autour de sa position d'équilibre pour :
* une vibration de très faible amplitude : $(r - r_E) < 0.01 r_E$
* une vibration plus importante : $(r - r_E) < 0.2 r_E$

On cherchera à observer par les tracés temporelles et le portrait de phase si l'approximation linéaire de l'équation pourrait être valable et quelle sont les effets de non linéarité.

> __Exercice 3:__  
> Vous devez :
> 1. Définir une fonction `Ec(v)` qui renvoient l'énergie cinétique du système pour une vitesse donnée.
> 2. Utiliser votre implémentation du schéma d'Euler pour obtenir les temps $t_k$, positions $x(t_k)$ et vitesses $v(t_k)$ pour les deux cas étudiées puis les énergies potentielles $E_p(t_k)$, énergie cinétique $E_c(t_k)$ et énergie mécanique $E_m(t_k)$ aux temps $t_k$.
> 3. Tracer alors une fenêtre avec 4 graphiques : l'un donnant $x(t)$, le second $v(t)$, le troisième le portrait de phase et le quatrième l'évolution des 3 termes énergétiques.
> 4. Observer l'influence du pas d'intégration et l'adapter pour une intégration correcte.
> 5. Observer si ces évolutions sont cohérentes avec l'approximation linéaire et sinon quelles sont les différences.

```{code-cell} ipython3

```

### Fonctions de la bibliothéque scipy
Nous allons utiliser la fonction `odeint` de la bibliothèque `scipy.integrate`. Sa signature est :

```
scipy.integrate.odeint(func, y0, t, tfirst=True)
```

* `func` : fonction qui renvoie le vecteur :

$$\begin{pmatrix}
v_k\\
f(t, x, v)
\end{pmatrix}
$$

Plus généralement, on utiliser la représentation matricielle :

$$
Y_{k+1} = Y_k + h * F(t, x, v)
$$

avec 

$$
Y_k = \begin{pmatrix}
x_k\\
v_k
\end{pmatrix}
$$

et $F$ une fonction qui renvoie un vecteur (deux valeurs). Ici le vecteur donné précédemment.
* `y0` est un __vecteur__ donnant les conditions initiales.
* `t` est le vecteur pour lequels les valeurs de $Y_k$ (positions et vitesses) seront calculées. (`t` doit être ordonné).

__Précision sur le vecteur `t` et le pas d'intégration.__  
_Vous remarquerez qu'on ne donne pas de pas d'intégration. Le vecteur `t` ne fait pas office de pas d'intégration. Les valeurs de position et vitesse à ces temps seront calculées ensuite par interpolation.  
C'est la fonction odeint elle-même qui va déterminer le pas d'intégration par comparaison d'erreurs entre plusieurs méthodes. Elles peut fait varier ce pas d'intégration au cours du calcul : on dit que c'est une méthode à __pas variable.__ On peut régler la tolérance sur l'erreur avec des arguments optionnels non présentés ici.  
Ce pas pouvant varier et quelles fois être grand, il est préférable de donner explicitement un vecteur avec des valeurs temps pour calculer les positions et vitesses a posteriori._

> __Exercice 4:__  
> 1. Créer une fonction `Fhcl(t, Y)` qui prend comme argument un temps `t` et le vecteur `Y` composé de deux éléments $(x_k, v_k)$ et qui renvoie le vecteur $F(t, Y)$ décrit précédemment.
> 1. A vous de comprendre et utiliser la fonction précédente pour réaliser l'intégration du problème et étudier les vibration de la molécule.

+++

## Trajectoire de diffusion
> __Exercice 5:__  
> 1. Comment choisir les conditions initiales pour placer l'hydrogène dans un état de diffusion ?
> 2. Réaliser l'intégration numérique dans ces conditions et déterminer numériquement l'énergie cinétique à l'infini. Obtient-on ce qu'on attend ?

```{code-cell} ipython3

```
