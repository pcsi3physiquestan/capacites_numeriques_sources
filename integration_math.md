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
La page ci-présente existe en version notebook téléchargeable grâce au bouton ![Bouton](./images/bouton_tl.png) (choisir le format `.ipynb`). On rappelle qu'il faut ensuite l'enregistrer dans un répertoire adéquat sur votre ordinateur (`capa_num` par exemple dans votre répertoire personnel) puis lancer Jupyter Notebook depuis Anaconda pour accéder au notebook, le modifier et exécutez les cellules de code adéquates.

# Intégration numérique

> __Exercice 1:__  
> 1. Ecrire quatre fonctions `i_g(f:callable, x0:float, xf:float, N:int)`, `i_d(f:callable, x0:float, xf:float, N:int)`, `i_c(f:callable, x0:float, xf:float, N:int)` et `i_t(f:callable, x0:float, xf:float, N:int)` qui renvoie respectivement l'intégrale de $f$ entre $x_0$ et $x_f$ estimée par des rectangles à gauche, à droite, centrée puis par des trapèzes avec $N$ rectangles.
> 2. L'appliquer pour déterminer l'intégrale entre $x=0$ et $x=2$ des fonctions suivantes:
* $f(x) = \sqrt{\frac{3x^2 + 2x + 1}{x + 1 + \ln(1 + x)}}$ avec un pas de $10^{-3}$
* $g(x) = \exp{\cos(x^2 + 2)}$  avec un pas de $10^{-3}$
> 3. Tracer la représentation graphique des primitives des deux fonctions précédentes sur $[0,2]$ avec le même pas que précédemment en imposante que la primitive s'annule en $x_0$. On utilisera les fonctions crées précédemment.
> 4. Reprendre la question précédente mais en utilisation une récurrence pour calculer chaque point de la primitive.

__NOTE : Pour permettre le calcul de nombreuses valeurs de $f'$ sans avoir besoin d'utiliser une boucle, il faut travailler avec numpy et que la fonction `f` écrite en Python soit _vectorialisable._ On pensera pour cela à utiliser les fonctions usuelles (`sin, cos, log, exp`) issues _de la bibliothèque `numpy`_.__

```{code-cell}
:tags: [remove-output,hide-input]

```

> __Exercice 2:__  
> Télécharger le fichier de [données suivant](https://github.com/pcsi3physiquestan/donnees_exp/blob/main/circuit_rc.dat?raw=true) et l'ouvrir depuis pyzo (possible même si ce n'est pas un .py). Obtenir alors le chemin absolu vers ce fichier (clic droit sur l'onglet du nom de fichier et copier le chemin).
> 1. Dans votre script python, importer la fonction `chdir` du module `os` puis avec la commande `chdir(nom_du_repertoire_precedent_SANS_LE_NOM_DU_FICHIER)`, définir le _répertoire de travail_ (le répertoire dans lequel Python va chercher les fichiers).
> 2. Importer les données dans deux vecteurs numpy `temps` et `tension` avec la méthode expliquée [ici](https://pcsi3physiquestan.github.io/intro_python/notebook/import_file.html#preparer-l-importation).
> 3. Ecrire une fonction integ(x:numpy.ndarray, y:numpy.ndarray) -> numpy.ndarray qui doit calculer les intégrales $\int_{x=x_0}^{x_i} y(x')dx'$ par la méthode des trapèzes où $x_0$ est le premier terme de `x` et les `x_i` sont les valeurs successives de `x_i` (cela revient à estimer la primitive de $y$ qui s'annule en $x_0$ aux points $x_i$).
> 4. Utiliser la fonction précédente pour obtenir la primitive de la fonction tension(temps) s'annule $t_0$ le premier temps de mesures puis la tracer.

```{code-cell}
:tags: [remove-output,hide-input]

```