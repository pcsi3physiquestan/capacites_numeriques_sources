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

# Dérivation numérique

> __Exercice 1:__  
> 1. Ecrire trois fonctions `d_g(f:callable, x0:float, pas:float)`, `d_d(f:callable, x0:float, pas:float)`, `d_c(f:callable, x0:float, pas:float)` qui renvoie respectivement le nombre dérivée estimé à gauche, à droite et centrée pour la fonction $f$ en $x = x_0$ avec un pas de calcul $pas$.
> 2. L'appliquer pour déterminer le nombre dérivé en $x=0$ des fonctions suivantes:
* $f(x) = \sqrt{\frac{3x^2 + 2x + 1}{x + 1 + \ln(1 + x)}}$ avec un pas de $10^{-6}$
* $g(x) = \exp{\cos(x^2 + 2)}$  avec un pas de $10^{-6}$
> 3. Tracer la représentation graphique des fonctions dérivées des deux fonctions précédentes sur $[0,2]$ avec le même pas que précédemment.

__NOTE : Pour permettre le calcul de nombreuses valeurs de $f'$ sans avoir besoin d'utiliser une boucle, il faut travailler avec numpy et que la fonction `f` écrite en Python soit _vectorialisable._ On pensera pour cela à utiliser les fonctions usuelles (`sin, cos, log, exp`) issues _de la bibliothèque `numpy`_.__

```{code-cell}
:tags: [remove-output,hide-input]

```

> __Exercice 2:__  
> Télécharger le fichier de [données suivant](https://github.com/pcsi3physiquestan/donnees_exp/blob/main/circuit_rc.dat?raw=true) et l'ouvrir depuis pyzo (possible même si ce n'est pas un .py). Obtenir alors le chemin absolu vers ce fichier (clic droit sur l'onglet du nom de fichier et copier le chemin).
> 1. Dans votre script python, importer la fonction `chdir` du module `os` puis avec la commande `chdir(nom_du_repertoire_precedent_SANS_LE_NOM_DU_FICHIER)`, définir le _répertoire de travail_ (le répertoire dans lequel Python va chercher les fichiers).
> 2. Importer les données dans deux vecteurs numpy `temps` et `tension` avec la méthode expliquée [ici](https://pcsi3physiquestan.github.io/intro_python/notebook/import_file.html#preparer-l-importation).
> 3. Ecrire une fonction derive(x:numpy.ndarray, y:numpy.ndarray) -> numpy.ndarray qui doit calculer le nombre dérivée de y(x) en chaque instant du vecteur `x`. On réalisera une dérivée au centre pour tous les points, sauf pour le premier (dérivée à droite) et le dernier (dérivée à gauche).
> 4. Utiliser la fonction précédente pour obtenir la dérivée de la fonction tension(temps) puis la tracer.

```{code-cell}
:tags: [remove-output,hide-input]

```