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
La page ci-présente existe en version notebook téléchargeable grâce au bouton ![Bouton](./images/bouton_tl.png) (choisir le format `.ipynb`). On rappelle qu'l faut ensuite l'enregistrer dans un répertoire adéquat sur votre ordinateur (`capa_num` par exemple dans votre répertoire personnel) puis lancer Jupyter Notebook depuis Anaconda pour accéder au notebook, le modifier et exécutez les cellules de code adéquates.

# Implémentation complète

## Implémentation du schéma d'Euler

> __Exercice 1__
> 1. Commencer par importer les bibliothèques scientifiques utiles : numpy, matplotlib.pyplot
> 2. Ecrire une fonction `euler` 
>     * qui prend en arguments :
>         * une variable `f` qui sera une fonction
>         * un flottant `h` qui sera le pas $h$ d'intégration
>         * deux flottants `t0` et `tf` donnant les temps initiaux et finaux de l'intervalle sur lesquels on va intégrer le signal (Note : `tf` ne sera pas forcément atteint)
>         * un flottant `y0` donnant la valeur de $y(t)$ à l'instant `t0` 
>     * et qui renvoie deux vecteurs numpy : 
>         * le premier contient les temps $t_k$ où on a évaluer la fonction (on commence à `t0`)
>         * le second contient les valeurs estimées de $y(t_k)$ ($y_k$).

```{code-cell} ipython3
"""Ne pas oublier d'importer les bibliothèques scientifiques"""
```

## Application au régime libre et à l'échelon de tension.
__On prendra $\tau = 1$.__ Il s'agit de vérifier que la fonction précédente fonctionne correctement. _Si vous avez fait la comparaison dans l'étude de base, vous pouvez réutiliser une bonne partie du code pour le tracé graphique en choisissant bien le nom de vos variables._

> __Exercice 2__
> 1. Préciser l'expression de la fonction $f(t, y)$  dans le cas d'un régime libre et d'un échelon de tension ($E = 1V$) puis implémenter deux fonctions `f_libre` et `f_echelon` correspondant à ces fonctions (mettre les arguments `t` et `y` même s'ils n'interviennent pas dans la fonction).
> 2. Définir deux fonctions `sol_libre` et `sol_echelon` qui prennent comme argument `t`, `t1` et `y0` et qui renvoient respectivement les solutions pour un régime libre puis pour un échelon de tension avec comme condition initiale $y(t1) = y0$.
> 3. Utiliser le schéma d'Euler que vous avez implémenté pour résoudre numériquement le cas d'un régime libre et d'un échelon de tension. Choisir un pas d'intégration $pas = \frac{1}{1000} \tau$
> 4. Tracer sur le même graphique la réponse numérique et la réponse analytique pour un régime libre puis pour un échelon de tension.

```{code-cell} ipython3
"""La fonction euler que vous avez défini précédemment est accessibles"""
```

## Erreur et pas d'intégration
__Inutile de faire cette partie si vous l'avez dans l'étude de base.__

> __Exercice 3__
> 1. Reprendre l'exercice précédent mais en affichant deux graphiques (1 colonne et deux lignes) : les solutions analytique et numérique précédentes sur le premier et la valeur absolue des écarts entre les deux solutions sur le second graphique.
> 2. Etudier l'évolution des erreurs en fonction du pas d'intégration (commencer par un pas égal à $\tau$ puis diviser successivement par 5 le pas).

Pour vous aider sur la manière de tracer une fenêtre multi-graphique, utiliser cet [élément de cours](https://pcsi3physiquestan.github.io/intro_python/notebook/plus_loin.html).

_Informations utiles_:
* Vous pouvez tout à fait créer un tracé (`ax[0].plot(...)`) à l'intérieur d'une boucle pour superposer plusieurs courbes.

```{code-cell} ipython3

```

## Rampe de tension

On va aussi réaliser une étude énergétique. Pour cela, il faut calculer l'intensité $i$ par dérivation numérique puis l'énergie (dissipée ou fournie) par intégration numérique.

### Dérivation numérique.

On va réaliser une dérivée numérique centrée. Pour un pas de temps $h$. On peut faire l'approximation de $y(t-h)$ et $y(t+h)$ par :

$$
\begin{cases}
y(t - h) &\approx y(t) - h \frac{\rm{d}y}{\rm{dt}}(t)\\
y(t + h) &\approx y(t) + h \frac{\rm{d}y}{\rm{dt}}(t)
\end{cases}
$$

soit par soustraction :

$$
\frac{\rm{d}y}{\rm{dt}}(t) \approx \frac{y(t+h) - y(t-h)}{2h}
$$

soit pour la suite des $y_k$ (on note la suite des valeurs de la dérivée $dy_k$):

$$
dy_k = \frac{\rm{d}y}{\rm{dt}}(t_k) = \frac{y_{k+1} - y_{k-1}}{2h}
$$

Seul problème : __on ne peut utiliser cette expression pour calculer la dérivée pour $k=0$ et $k=k_{\max}$__. Pour les deux valeurs extrêmes, on va utiliser l'expression :

$$
\begin{cases}
dy_0 &= \frac{y_{1} - y_{0}}{h} \textrm{ Dérivation à droite}\\
dy_{k_{\max}} &= \frac{y_{k_{\max}} - y_{k_{\max} - 1}}{h} \textrm{ Dérivation à gauche}\\
\end{cases}
$$

> __Exercice 4__
> 1. Définir une fonction `deriv` qui prend comme argument le vecteur `y` des valeurs à dériver et le `pas` de calcul et qui renvoie le vecteur des valeurs dérivées.
> 2. Vérifier son fonctionnement en calculant la dérivée des tensions pour les régimes libre et échelon de tension en traçant leur comparaison avec leurs expressions analytiques.

```{code-cell} ipython3

```

### Intégration numérique.
On applique la méthode des rectangles pour calculer numériquement l'intégrale de $y(t)$ entre $t_0$ et $t_k$. On note $s_k$ la valeur de cette intégrale et on prend $s_0 = 0$ (l'énergie échangé initialement sera nulle). On définit donc la récurrence :

$$
s_{k+1} = s_k + h * y_k
$$

> __Exercice 5__
> 1. Définir une fonction `integ` qui prend comme argument le vecteur `y` à intégrer et le `pas` de calcul et qui renvoie le vecteur des valeurs intégrées.
> 2. Vérifier son fonctionnement en calculant l'intégrale des tensions pour les régimes libre et échelon de tension en traçant leur comparaison avec leurs expressions analytiques.

```{code-cell} ipython3

```

### Application à la rampe.
On étudie un circuit RC série soumis à une tension $E(t)$ :

$$
E(t) = 
\begin{cases}
0 & \textrm{si t <= 0}\\
t / T0 & \textrm{si 0 < t <= T0}\\
1 & \textrm{si t > T0}\\
\end{cases}
$$

On prendra $R = 1\rm{k\Omega}; C = 1\rm{\mu F}; T0 = k \times \tau; u(t=0) = 0 \rm{V}$.

_Rappels :_
* L'__énergie__ stockée dans un condensateur est $E_{el} = \frac{1}{2}C u_c^2$
* La __puissance__ dissipée par effet Joule est $P_J(t) = R i^2(t)$

> __Exercice 6__
> 1. Procéder à l'intégration de l'équation différentielle pour $k=2$ en choisissant un pas de calcul adapté.
> 2. En déduire l'intensité circulant dans le condensateur, l'énergie stockée dans le condensateur (aux mêmes instants $t_k$), l'énergie dissipée par la résistance et l'énergie fournie par la source (entre t=0  et $t=t_k$).
> 3. Représenter quatre graphiques dans une même fenêtre (2 lignes, 2 colonnes) représentant :
>     * premier graphique : les tensions $E(t)$ et $u(t)$
>     * deuxième graphique : l'intensité $i(t)$
>     * troisième graphique ; le portrait de phase (ensemble des points de coordonnées ($u(t); \frac{du}{dt}(t)$))
>     * quatrième graphique ; l'évolution de l'énergie stockée dans le condensateur, celle délivrée par la source et celle dissipée par la résistance
> 4. Analyser physiquement les courbes obtenues.
> 5. Reprendre l'étude en augmentant $k$. On commentera notamment l'énergie dissipée par effet Joule.
> 6. Quantifier l'évolution du rendement $\eta = \frac{E_{stockee}(+\infty)}{E_{fournie}(+\infty)}$ par rapport à $k$ par un tracé graphique adapté. On réfléchira à comment estimer $\eta$ pour chaque valeur de $k$.

_Pour étudier le rendement sur plusieurs décades entre $k=0.01$ et $k=1000$. Deux syntaxes utiles :_
* `np.logspace(start, stop, N)` fonctionne comme `linspace` mais les points sont créés régulièrement sur un axe logarithmique entre $10^{start}$ et $10^{stop}$.
* `ax.set_xscale('log')` permet de représenter les abscisses suivant une échelle logarithmique.

```{code-cell} ipython3

```