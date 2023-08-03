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

# Implémentation basique

## Schéma d'euler - Système d'équations
On va chercher à résoudre le système suivant:

$$
\begin{cases}
\frac{\rm{d}u}{\rm{dt}} = - \frac{1}{\tau} v - \frac{2}{\tau}u\\
\frac{\rm{d}v}{\rm{dt}} = - \frac{1}{\tau} v - \frac{1}{\tau}u
\end{cases}
$$
avec $v(t=0) = 2$, $u(t=0) = 0$,  $\tau = 1$

> __Exercice 1 :__  
> 1. Copier-coller la fonction `euler` que vous avez écrite pour la séance précédente. Si le corps de la fonction ne change pas, sa signature change:
```{code-block}
euler(f:callable, y0: numpy.ndarray, t0: float, tf: float, pas: float) -> (numpy.ndarray, numpy.ndarray)
```
> 2. Ecrire une fonction `F(t:float, Y:numpy.ndarray) -> numpy.ndarray` qui renvoie la fonction $F$ du schéma d'Euler précédent. __Attention, cette fois, `Y` est un vecteur (dont les composantes sont $u_k$ et $v_k$) et $F$ renvoie un vecteur (dont les composantes sont $\frac{\rm{d}u}{\rm{dt}}(t_k)$ et $\frac{\rm{d}v}{\rm{dt}}(t_k)$ obtenus à partir du système d'équations). Veillez à renvoyer un vecteur et non une liste (pourquoi ?).__
> 3. Utiliser la fonction `euler` pour obtenir $Y(t)$ puis tracer $u(t)$ et $v(t)$ entre $t=0$ et $t=10$. A vous de choisir le pas d'intégration sachant que $\tau$ est à peu près le "temps caractéristique" du système.
> 4. Obtenir la solution grâce aux fonction `odeint` ou `solve_ivp` puis les tracer pour vérifier que vous obtenez le même tracé.

```{code-cell}
:tags: [remove-output,hide-input]
"""Ne pas oubliez d'importer les bibliothèques scientifiques."""

```
## Schéma d'Euler - Ordre 2
On veut résoudre l'équation différentielle suivante:

```{margin}
On pourra vérifier théoriquement qu'en éliminant $v(t)$ du système précédent, on obtient cette équation.
```
$$
\frac{\rm{d^2}u}{\rm{dt^2}} = - \frac{3}{\tau}\frac{\rm{d}u}{\rm{dt}} - \frac{1}{\tau}u
$$

On va donc travailler avec le vecteur :

$$ Y(t)=
\begin{pmatrix}
u(t)\\
\frac{\rm{d}u}{\rm{dt}}(t)
\end{pmatrix}
$$


> __Exercice 2 :__  
> 1. La fonction `euler` a-t-elle besoin d'être modifiée ?
> 2. Ecrire une fonction `F2(t, Y)` correspondant au schéma d'Euler comme [expliqué précédemment](sys_o2).
> 3. Obtenir la solution  sur le même intervale de temps que dans l'exercice précédent et vérifier que la solution coïncide avec la solution trouvée avec un système d'équations.


```{code-cell}
:tags: [remove-output,hide-input]

```
