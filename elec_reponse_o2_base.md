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

## Mise en pratique
> __Exercice :__  
> Pour les études numériques, on prend $R=1k\Omega$ et $C= 1nF$.
> 
> 2. Ecrire une fonction `F(Y, t)` qui prend comme argument le vecteur `Y` et l'instant `t` et qui renvoie un __vecteur__ numpy de taille 2 correspondant au vecteur donné précédemment.
> 3. Ecrire une fonction `euler(F, Y0, tf, pas)` qui prend comme argument la fonction `F`, un vecteur `Y0` donnant les conditions initiales $u(0), v(0)$, et qui réalise l'intégration d'Euler par `pas` d'intégration de $t=0$ à `tf`.Elle renverra un tableaux numpy à deux colonnes contenant pour chaque lignes les valeurs de Y aux temps $t_k$ et un vecteur numpy contenant les temps $t_k$. __S'inspirer de ce qui a été fait à l'ordre 1.__
> 4. Obtenir l'expression théorique de $u(t)$ et $v(t)$ par le calcul pour un jeu de conditions initiales $u0, v0$ puis créer deux fonctions `u_th(t, Y0)` et `v_th(t, Y0)` qui renvoie un vecteur des valeurs de u (ou v) par l'expression théorique obtenue pour un vecteur de valeurs de temps `t`.
> 5. Obtenir puis tracer l'évolution temporelle de $u(t)$ et $v(t)$ par intégration numérique ainsi que par calcul théorique et comparer les deux tracés. On adaptera le pas d'intégration pour limiter les écarts. On prend $u(0) = 0; v(0) = v_0 = 1V$.

```{code-cell}
:tags: [remove-output,hide-input]

```


## Vers l'ordre 2.
Remarquons que le problème précédent peut aussi s'appliquer à une équation linéaire d'ordre 2. Reprenons le système précédent et en éliminant $v(t)$, on obtient l'équation:

$$
\frac{\rm{d^2}u}{\rm{dt^2}} = - \frac{3}{RC}\frac{\rm{d}u}{\rm{dt}} - \frac{1}{RC}u
$$

Soit en posant $w = \dot u = \frac{\rm{d}u}{\rm{dt}}$:

>$$ {\rm{d} \over \rm{d}t}
\begin{pmatrix}
u\\
w
\end{pmatrix}
=
\begin{pmatrix}
w\\
- \frac{3}{RC}w - \frac{1}{RC}u
\end{pmatrix}
$$
avec $u(0) = u(0)$ et $w(0) = - \frac{v(0)}{RC}$
On retrouve donc la même vision vectorielle en posant:

$$ Y(t)=
\begin{pmatrix}
u(t)\\
v(t)
\end{pmatrix}
$$

> __Exercice :__  
> 1. Reprendre la fonction `euler` avec une fonction `G` qui correspondant à la dérivée du vecteur $Y = (u,\dot u)$ et retrouver ainsi l'expression de $u(t)$ (ainsi que $\dot u(t)$).

```{code-cell}
:tags: [remove-output,hide-input]

```
