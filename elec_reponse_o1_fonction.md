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

# Utilisation de la bibliothèque scipy
__Si vous vous sentez suffisamment à l'aise,__ vous pouvez passer directement à l'[étude approfondie](elec_reponse_o1_complet).

## Définition des fonctions pour le schéma d'Euler
On va commencer par définir la fonction $f(t,y)$ pour les deux types d'étude : le régime libre et l'échelon de tension.

__Attention : Même si $f$ ne dépend pas explicitement du temps, on gardera $t$ comme argument de la fonction car cet argument est nécessaire quand on utilise les fonctions natives de `numpy` pour intégrer une équation différentielle.__

> __Exercice A__  
> Dans la cellule ci-après, vous devez:
> 1. Importer les deux bibliothèques `numpy` et `matplotlib.pyplot`
> 2. Créer deux fonction `f_libre` et `f_echelon` prenant deux arguments `t` et `u` (correspondant à un instant $t_k$ et à $u_k = u(u_k)$) et qui renvoie la valeur $f(t_k, u_k)$ pour chaque cas (régime libre et échelon de tension) (u est la tension aux bornes du condensateur comme dans l'étude présentée dans l'[exemple](pospb)). _Vous pouvez définir $R,C$ et $\tau$ comme des variables globales que vous utilisez dans les fonctions._

```{code-cell} ipython3
:tags: [hide-input, remove-output]
"""Ne pas oublier d'importer les bibliothèques scientifiques et d'éxécuter la cellule."""
```

## Solve_ivp
La fonction `solve_ivp` appartient à la bibliothèque `scipy.integrate`, sa signature est la suivante:

```
solve_ivp(f:callable, t_span:tuple, y0:nd.array, t_eval=t_eval:nd.array) -> dict
```
* Arguments :
    * `f` est la fonction du schéma d'Euler définie précédemment
    * `t_span` est un tuple de élément `(t0, tf)` donnant l'instant initial et l'instant final de l'intégration.
    * `y0` est __un vecteur numpy__ (ou une liste classique) contenant les conditions initiales. Ceci __même quand il n'y a qu'une condition initiale.__
    * `t_eval` (argument optionnel donc impératif de le nommer `t_eval = ...`) est un vecteur numpy contenant les instants $t_k$ où l'on veut estimer la fonction solution. Même s'il est optionnel, il faudra toujours le donner.
* Retour :
    * Un __dictionnaire__ dont les clés _utiles_ sont:
        * `dict['t']`: les instants $t_k$ (donc l'argument de `t_eval`...)
        * `dict['y']`: un __tableau__ numpy contenant à chaque ligne la solution $y_k = y(t_k)$. Comme il n'y a qu'une seule ligne pour une équation différentielle de degré 1, on obtiendra les $y_k$ par `dict['y'][0]`
### Cas du régime libre


> __Exercice B__ : Avec une boucle for  
> 1. Définir un vecteur numpy contenant les instants $t_k$.
> 2. Utiliser la fonction `solve_ivp` pour intégrer l'équation dans le cas d'un régime libre puis tracer $y_k$ en fonction $t_k$ avec les avoir extraits du dictionnaire renvoyé par la fonction.
> 3. Le comparer graphiquement à la solution analytique donnée ci-dessous.

On rappelle que la solution analytique est:

$$
y(t) = y_0 \exp^{- t / \tau}
$$
_Note : Certaines étapes pourraient être raffinées (création du vecteur temps par exemple)._

```{code-cell} ipython3
:tags: [hide-input, remove-output]
# On rappelle que la fonction f_libre est accessible et que les bibliothèques scientifiques ont été créés.
```

### Cas de la réponse à un échelon de tension.
> __Exercice C__ : Avec une boucle for  
> 1. Définir un vecteur numpy contenant les instants $t_k$.
> 2. Utiliser la fonction `solve_ivp` pour intégrer l'équation dans le cas de la réponse à un échelon de tension puis tracer $y_k$ en fonction $t_k$ avec les avoir extraits du dictionnaire renvoyé par la fonction.
> 3. Le comparer graphiquement à la solution analytique donnée ci-dessous.

On rappelle que la solution analytique est:

$$
y(t) = E(1 -  \exp^{- t / \tau})
$$

```{code-cell} ipython3
:tags: [hide-input, remove-output]
```
