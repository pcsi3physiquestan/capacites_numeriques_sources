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

# Etude d'un système d'ordre 2 : le pendule

## Etude générale
On va étudier directement un système d'ordre 2 issu d'un problème de mécanique: le pendule simple sans frottement. L'équation qui régit l'évolution de l'angle $\theta(t)$ que fait le pendule avec un axe horizontal est:

$$
\frac{\rm{d^2}\theta}{\rm{dt^2}} = - \omega_0^2 \sin \theta
$$

avec $\omega_0 = \sqrt{\frac{g}{l}}$ ($l=1\rm{m}$ est la longueur du fil du pendule et $g=9.81 \rm{m.s^{-2}}$ l'intensité du champ de pesanteur).

> __Exercice 1:__  
> 1. Si l'on pose le vecteur $Y(t) = (\theta(t), \dot \theta(t))$, écrire la fonction `F` associée au schéma d'Euler puis utiliser la fonction `solve_ivp` (la réécrire dans la cellule suivante pour pouvoir l'utiliser) pour obtenir $\theta(t)$ si $\theta(0) = \pi /4$ et $\dot \theta(0) = 0$
> 2. Tracer sur deux graphiques différents l'évolution de $\theta(t)$ et de sa dérivée. Observe-t-on le comportement d'un oscillateur harmonique ?

```{code-cell}
:tags: [remove-output,hide-input]

```

## Petites et grandes oscillations
### Différences
Aux petits angles, l'équation différentielle devient:
$$
\frac{\rm{d^2}\theta}{\rm{dt^2}} = - \omega_0^2 \theta
$$
soit un oscillateur harmonique dont la solution analytique est:

\begin{equation}
\theta (t) = \theta_i \cos \omega_0 t + \frac{\omega_i}{\omega_0} \sin \omega_0 t
\end{equation}
avec $\theta_i = \theta(0)$ et $\omega_i = \dot \theta (0)$.

> __Exercice 3:__  
> 1. On considère le cas où on lâche le pendule de $\theta_i = 0$ avec une vitesse initiale $\omega_i$. Déterminer grâce à `solve_ivp` __sans approximation__ l'évolution de $\theta(t)$ pour cinq vitesses de départ différentes répartis entre 0 et $\sqrt{\frac{2g}{l}}$ et comparer graphiquement les solutions obtenues à la solutions théoriques aux petites angles. Cette approximation est-elle valable jusqu'à $\sqrt{\frac{2g}{l}}$ ?

```{code-cell}
:tags: [remove-output,hide-input]

```

### Anisochronisme
On se propose de déterminer la période des oscillations en fonction de l'amplitude des oscillations.  
__Méthode choisie__ : On va déterminer les temps $t_{0i}$ successifs des points où la solution numérique pour $\theta(t)$ s'annule (plus précisément les temps médians entre deux instants où le signal change de signe). Comme il n'y a que 2 annulations des angles dans une période (cf. étude des systèmes conservatifs), il suffira de compter le nombre $N_0$ de 0. La période $T$ du signal s'écrit alors :

$$
T = {t_{0N_0} - t_{01} \over {N_0 - 1 \over 2}}
$$

> __Exercice 4:__  
> 1. Ecrire une fonction `periode` qui prend en arguments deux vecteurs de mêmes taille `tk` et `thetak` et qui renvoie la période du signal `thetak` en considérant les `tk` comme les temps associés.
> 2. Tester votre fonction sur un signal intégré numériquement obtenu précédemment pour vérifier que vous trouvez bien la bonne période (prendre un cas de petites oscillations car vous connaissez alors la période).
> 3. Comment choisir les conditions initiales pour que $\theta_i$ soit l'amplitude des oscillations? Pour 49 valeurs comprises entre $\pi/50$ et $49\pi/50$, réaliser l'intégration numérique sans approximation et détermienr la période. Tracer alors la période en fonction de l'amplitude des oscillations.

```{code-cell}
:tags: [remove-output,hide-input]

```
### Trajectoire de diffusion
On s'intéresse au cas où le pendule part de sa position la plus basse avec une vitesse angulaire $\omega_i$.
La viteses angulaire initiale permettant au pendule (tige rigide) d'atteindre $\pi$ et de s'y arrêter est :

$$
\omega_{i,\lim} = \sqrt{\frac{4g}{l}}
$$
En dessous, le pendule oscille. Au dessus, il fait des tours complets.

> __Exercice 5 :__  
> 1. Intégrer l'équation du pendule avec une valeur de $\omega_i$ supérieure à à la valeur limite et observer l'allure de $\theta(t)$ et $\dot \theta(t)$. Commenter.
> 2. Intégrer l'équation du pendule avec la valeur de $\omega_i$ limite précédente et observer l'allure de $\theta(t)$ et $\dot \theta(t)$. Commenter. Reprendre avec une valeur de $\omega_i$^très légèrement inférieure.

```{code-cell}
:tags: [remove-output,hide-input]

```