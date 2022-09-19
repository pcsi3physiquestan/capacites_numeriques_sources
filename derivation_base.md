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

# Dérivation et intégration : Méthode de base

On se propose de mettre en place les calculs d'intégration et de dérivation sur des cas simples basés sur l'électrocinétique. On considère un circuit RC soumis à un échelon de tension $E$. La tension aux bornes du condensateur est alors:

$$
u(t) = E (1 - e^{- t / \tau})
$$

avec $\tau = RC$.

Pour la suite, on prendra $E = 1\rm{V}; R = 10 \rm{k\Omega}; C=10^{-4} \rm{F}$ et donc $\tau = 1\rm{s}$. On rappelle que:
* L'intensité qui circule à travers le condensateur (et donc aussi la résistance) est donné par $i = C \frac{\rm{d}u}{\rm{dt}}$
* La puissance dissipée à un instant $t$ par effet Joule est donné par $P(t) = R i^2(t)$. L'énergie dissipée par effet Joule entre $t_0$ et $t_1$ est donc:

$$
E_J = \int_{t_0}^{t_1} Ri^2(t) dt
$$

Dans ce cas, simple, on peut calculer analytiquement $i(t)$ et $E_J$. Mais on va réaliser une dérivation puis une intégration numérique. L'intérêt sera de comparer ce qu'on trouve aux expressions analytiques.

## Calcul de l'intensité.

> __Exercice A:__  
> 1. Importer les bibliothèques scientifiques `numpy` et `matplotlib.pyplot`.
> 2. Ecrire deux instructions pour créer deux vecteurs `tk` et `uk` contenant respectivement les instants $t_k$ équirépartis entre 0 et 5s et les valeurs $u_k = u(t_k)$ à ces instants. On prendra 1000 valeurs pour chaque vecteur.
> 3. Ecrire une boucle __avec son initialisation__ qui calcule les $i_k = i(t_k)$ par un calcul dérivée à gauche avec un pas $h=10^{-3}\rm{s}$ puis les ajoute à une liste `ik`.
> 4. Transformer la liste `ik` en un vecteur `numpy`.
> 5. Tracer sur un même graphique $i(t)$ obtenu par dérivation numérique et $i(t)$ obtenu par calcul analytique puis jouer sur le pas $h$ pour voir si la dérivation est encore acceptable si on augmente $h$.

_On rappelle que analytiquement, on trouve:_

$$
i(t) = \frac{E}{R} e^{-t / \tau}
$$

```{code-cell}
:tags: [remove-output,hide-input]

```

> __Exercice B:__  
> 1. Reprendre les instructions précédentes et réaliser le calcul de la dérivation numérique par intégration à droite puis centrée. Comparer graphiquement à la solution analytique.

```{code-cell}
:tags: [remove-output,hide-input]

```

## Calcul de l'énergie dissipée
> __Exercice C:__  
> 1. Ecrire une instruction pour créer un vecteur `Pk` contenant les puissances $P_k = P_J(t_k)$ dissipées par effet Joule dans R à chaque instant.
> 3. Ecrire une boucle __avec son initialisation__ qui calcule les $E_k = E_J(t_k)$, énergie dissipée entre $t=0$ et $t=t_k$, par la méthode des rectangles à gauche avec un pas $h=10^{-3}\rm{s}$ puis les ajoute à une liste `Ek`. Pensez à utiliser une récurrence.
> 4. Transformer la liste `Ek` en un vecteur `numpy`.
> 5. Tracer sur un même graphique $E_J(t)$ obtenu par dérivation numérique et $E_J(t)$ obtenu par calcul analytique puis jouer sur le pas $h$ pour voir si la dérivation est encore acceptable si on augmente $h$.

_On rappelle que analytiquement, on trouve:_

$$
E_J(t) = \frac{CE^2}{2} \left(1 -  e^{-2 t / \tau}\right)
$$

```{code-cell}
:tags: [remove-output,hide-input]

```

> __Exercice D:__  
> 1. Reprendre les instructions précédentes et réaliser le calcul de l'intégration numérique par intégration à droite, centrée puis par les trapèzes. Comparer graphiquement à la solution analytique.

```{code-cell}
:tags: [remove-output,hide-input]

```

(cas_exp)=
## A partir de données expérimentales.
Les données expérimentales sont celle déjà utilisée précédemment et accessible par [ce lien](https://github.com/pcsi3physiquestan/donnees_exp/blob/main/circuit_rc.dat?raw=true). On rappelle que la méthode d'importation d'un fichier est disponible [ici](https://pcsi3physiquestan.github.io/intro_python/notebook/import_file.html).

````{note}
Si votre navigateur ouvre le fichier au lieu de le télécharger, faites un clic droit sur le lien et choisir `Enregistrer la cible du lien`.
````

> __Exercice E:__  
> 1. Après avoir télécharger le fichier __et l'avoir placé dans le bon répertoire__, ouvrez le pour lire l'en-tête et la structure du fichier. Ecrire alors deux instructions : la première importe le fichier et crée deux vecteurs `tk` et `ukb` contenant les temps de mesure et les mesures de tension en bits et la seconde instruction qui transforme la liste `ukb` en une liste `uk` contenant les valeurs de tension en volt. _S'aider de la ligne de commande proposée ci-dessous et de la description du fichier._
> 3. Ecrire une boucle __avec son initialisation__ qui calcule les $i_k = i(t_k)$ par dérivation numérique (cf. remarque après) et qui le stocke dans une liste `ik` puis transformer la liste en un vecteur.
> 3. Ecrire une boucle __avec son initialisation__ qui calcule les $E_k = E_J(t_k)$, énergie dissipée entre $t=0$ et $t=t_k$ par intégration numérique et qui le stocke dans une liste `Ek` puis transformer la liste en un vecteur. On utilisera la méthode des rectangles (cf. remarque après).
> 5. Tracer trois graphiques: $u(t), i(t), E_J(t)$ sur trois graphiques différents (on utilisera soit trois fenêtres graphiques, soit un graphique multiple si on se sent à l'aise avec ce dernier).

* Pour l'import, on rappelle la commande permettant de séparer les colonne en plusieurs variables:

```temps, ucb = np.loadtxt('chemin_vers_fichier', skiprows=nlignes_a_sauter, delimiter="delimiteur de colonne", unpack=True)```

* Pour les méthodes numériques, on ne peut choisir ici le pas d'intégration car on ne connaît que des valeurs discrètes.
    * Dérivation numérique: le pas est imposé par les écarts entre les $t_k$. De plus, comme précisé précédemment, vous devez utiliser une dérivée à droite en $t_0$ et une dérivée à gauche en $t_{final}$. Pour les instants intermédiaires, il est __demandé d'utiliser une dérivée centrée.__
    * Intégration numérique: le pas est à nouveau imposé par les $t_k$. On utilisera __la méthode des trapèzes__ pour l'intégration.

```{code-cell}
:tags: [remove-output,hide-input]

```