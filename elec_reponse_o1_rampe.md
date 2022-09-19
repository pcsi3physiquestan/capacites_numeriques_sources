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

# Réponse à une rampe de tension.

## Fonctions utiles

> 1. La fonction que vous avez définie dans l'autre notebook n'est pas défini ici. Copiez-collez votre fonction pour l'utiliser ici.
> 2. De même, les fonctions que vous avez créés dans la partie sur [l'intégration et la dérivation numérique](deriv_int_fn) vont être utiles ici. Recopiez les aussi pour pouvoir les utiliser.

```{code-cell} ipython3
"""Ne pas oublier d'importer les bibliothèques scientifiques"""
```

## Rampe de tension

On étudie un circuit RC série soumis à une tension $E(t)$ :

$$
E(t) = 
\begin{cases}
0 & \textrm{si t <= 0}\\
t / T0 & \textrm{si 0 < t <= T0}\\
1 & \textrm{si t > T0}\\
\end{cases}
$$

On prendra $R = 1\rm{k\Omega}; C = 1\rm{\mu F}; T0 = n \times \tau; u(t=0) = 0 \rm{V}$.

_Rappels :_
* L'__énergie__ stockée dans un condensateur est $E_{el} = \frac{1}{2}C u_c^2$
* La __puissance__ dissipée par effet Joule est $P_J(t) = R i^2(t)$

> __Exercice 6__
> 1. Ecrire une fonction `rampe(t)` qui renvoie la valeur de `E(t)` pour un instant donné puis l'utiliser pour créer la fonction `f_rampe` du schéma d'Euler.
> 1. Procéder à l'intégration de l'équation différentielle pour $n=2$ en choisissant un pas de calcul adapté.
> 2. En déduire l'intensité circulant dans le condensateur, l'énergie stockée dans le condensateur (aux mêmes instants $t_k$), l'énergie dissipée par la résistance et l'énergie fournie par la source (entre t=0  et $t=t_k$).
> 3. Représenter quatre graphiques dans une même fenêtre (2 lignes, 2 colonnes) représentant :
>     * premier graphique : les tensions $E(t)$ et $u(t)$
>     * deuxième graphique : l'intensité $i(t)$
>     * troisième graphique ; le portrait de phase (ensemble des points de coordonnées ($u(t); \frac{du}{dt}(t)$))
>     * quatrième graphique ; l'évolution de l'énergie stockée dans le condensateur, celle délivrée par la source et celle dissipée par la résistance
> 4. Analyser physiquement les courbes obtenues.
> 5. Reprendre l'étude en augmentant $n$. On commentera notamment l'énergie dissipée par effet Joule.
> 6. Quantifier l'évolution du rendement $\eta = \frac{E_{stockee}(+\infty)}{E_{fournie}(+\infty)}$ par rapport à $n$ par un tracé graphique adapté. On réfléchira à comment estimer $\eta$ pour chaque valeur de $n$.

_Pour étudier le rendement sur plusieurs décades entre $n=0.01$ et $n=1000$. Deux syntaxes utiles :_
* `np.logspace(start, stop, N)` fonctionne comme `linspace` mais les points sont créés régulièrement sur un axe logarithmique entre $10^{start}$ et $10^{stop}$.
* `ax.set_xscale('log')` permet de représenter les abscisses suivant une échelle logarithmique.

```{code-cell} ipython3

```
