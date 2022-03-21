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

# Implémentation basique
__Si vous vous sentez suffisamment à l'aise,__ vous pouvez passer directement à l'[étude approfondie](elec_reponse_o1_complet).

## Définition des fonctions pour le schéma d'Euler
On va commencer par définir la fonction $f(t,y)$ pour les deux types d'étude : le régime libre et l'échelon de tension.

__Attention : Même si $f$ ne dépend pas explicitement du temps, on gardera $t$ comme argument de la fonction car cet argument est nécessaire quand on utilise les fonctions natives de `numpy` pour intégrer une équation différentielle.__

> __Exercice A__  
> Dans la cellule ci-après, vous devez:
> 1. Importer les deux bibliothèques `numpy` et `matplotlib.pyplot`
> 2. Créer deux fonction `f_libre` et `f_echelon` prenant deux arguments `t` et `u` (correspondant à un instant $t_k$ et à $u_k = u(u_k)$) et qui renvoie la valeur $f(t_k, u_k)$ pour chaque cas (régime libre et échelon de tension) (u est la tension aux bornes du condensateur comme dans l'étude présentée dans l'[exemple](pospb)). _Vous pouvez définir $R,C$ et $\tau$ comme des variables globales que vous utilisez dans les fonctions._

```{code-cell} ipython3
"""Ne pas oublier d'importer les bibliothèques scientifiques et d'éxécuter la cellule."""
```

## Implémentation du schéma d'Euler
### Cas du régime libre
L'implémentation suivante est à bien comprendre et à savoir refaire sans guide. Elle est la base des intégrations numériques. Dans un premier temps, on prendra $h= \tau / 1000$ et on prendra les valeurs $R$ et $C$ données [précédemment](miseq).

> __Exercice B__ : Avec une boucle for  
> 1. Ecrire une suite d'instructions qui:
>     * (Préparation) Définit le pas `h`, la constante de temps `tau`, le temps final `t_f` et le nombre d'intégration `N` à réaliser.
>     * (Initialisation) Créer deux __listes__ vide `tkf` et `ukf` dans lesquels on stockera les valeurs $t_k$ et $u_k$ puis ajouter à ces listes les conditions initiales $t_0$ et $u_0$. On prendra $u_0 = u(t_0) = 1 \rm{V}$ et $t_0 = 0$.
>     * (Boucle) Dans une boucle for, réalise plusieurs fois l'intégration numérique avec le pas `h` et la fonction `f_libre`. A chaque fois, vous devrez calculer la valeur $u_{k+1}$ que vous stockerez dans la liste `ukf` puis le nouveau temps $t_{k+1}$ que vous stockerez dans la liste `tkf`. Bien réfléchir aux bornes de la boucle.
>     * (Terminaison) Pour une utilisation plus simples ensuite des listes de valeurs `tkf` et `ukf`. Transformer les deux listes en deux vecteurs `numpy`.

```{code-cell} ipython3
# On rappelle que la fonction f_libre est accessible et que les bibliothèques scientifiques ont été créés.
```

> __Exercice C__ : Avec une boucle while  
> 1. Ecrire une suite d'instructions qui:
>     * (Préparation) Définit le pas `h`, la constante de temps `tau`, le temps final `t_f`.
>     * (Initialisation) Créer deux __listes__ vide `tkw` et `ukw` dans lesquels on stockera les valeurs $t_k$ et $u_k$ puis ajouter à ces listes les conditions initiales $t_0$ et $u_0$. On prendra $u_0 = u(t_0) = 1 \rm{V}$ et $t_0 = 0$.
>     * (Boucle) Dans une boucle while, réalise plusieurs fois l'intégration numérique avec le pas `h` et la fonction `f_libre`. A chaque fois, vous devrez calculer la valeur $u_{k+1}$ que vous stockerez dans la liste `ukw` puis le nouveau temps $t_{k+1}$ que vous stockerez dans la liste `tkw`. Bien réfléchir à la condition de sortie de la boucle.
>     * (Terminaison) Pour une utilisation plus simples ensuite des listes de valeurs `tkw` et `ukw`. Transformer les deux listes en deux vecteurs `numpy`.
> 2. Tracer $y(t)$ pour chaque intégration (for et while). Tracer sur le même graphique la solution analytique pour comparaison (utilisez les $t_k$ comme abscisses). __N'oubliez pas de légender la figure.__

On rappelle que la solution analytique est:
$$
y(t) = y_0 \exp^{- t / \tau}
$$
_Note : Certaines étapes pourraient être raffinées (création du vecteur temps par exemple)._
```{code-cell} ipython3
# On rappelle que la fonction f_libre est accessible et que les bibliothèques scientifiques ont été créés.
```

### Influence du pas d'intégration
> __Exercice D__ :
> 1. Reprendre la suite d'instructions précédente (avec for ou while peu importe) pour $h = \tau / 10$; $h = \tau / 2$; $h = \tau$; $h = 2 * \tau$. Réaliser le tracé $y(t)$ pour chaque cas ainsi que la comparaison avec la solution analytique.
> 2. En déduire comment choisir correctement le pas d'intégration.

### Cas de la réponse à un échelon de tension.
> __Exercice E__ :
> 1. Reprendre la suite d'instructions précédente (avec for ou while peu importe) avec un pas d'intégration correctement et obtenir la solution numérique pour un échelon de tension ($E = 1V$ et $y_0 = 0V$). Le comparer à la solution analytique.

On rappelle que la solution analytique est:
$$
y(t) = E(1 -  \exp^{- t / \tau})
$$

La nécessité de copier-coller le même code pour chaque test montre qu'il serait bien plus efficace de mettre ces instructions dans une fonction qu'on réutiliserait plusieurs fois. C'est l'objectif de la première partie de l'étude complète avant de l'utiliser pour la réponse à une entrée plus complexe : une rampe de tension.

