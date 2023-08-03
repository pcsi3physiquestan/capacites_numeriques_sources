---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,py:light
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

_Les questions (Math) ne demande pas de code informatique._

# Etude abstraite
On se propose d'utiliser la méthode précédente pour déterminer la racine de la fonction :

$$
f(x) = \exp(x) + x
$$

Ce problème est ici purement mathématique aucune modélisation physique n'est associée à cette fonction. Le but est :
* d'utiliser un tracé graphique pour déterminer le nombre de solution et trouver un intervalle de recherche pour chaque solution.
* de coder, sous la forme d'une série d'instruction puis sous la forme d'une fonction, la méthode de dichotomie
* d'utiliser la fonction `scipy.optimize.bisect` qui réalise aussi la dichotomie.
* (facultatif) Tester d'autre terminaisons ou essayer de coder la méthode de dichotomie par une méthode récursive.

(math_prealable_eq)=
## Etude préalable.
__On ne peut se lancer dans une recherche de solution par dichotomie sans avoir d'abord vérifier l'existence d'une solution et avoir trouvé un intervalle (de taille finie) dans laquelle la solution se trouve.__

> __Exercice 1:__  
> 1. (Math) Montrer, par une étude théorique et mathématique que la fonction précédente admet une seule et unique racine et que cette racine est négative.
> 2. (Math) Que vaut $f(0)$ ? Proposer une valeur numérique $x_0$ telle que $f(x_0)$ soit de signe opposé à $f(0)$.
> 3. Tracer $f$ sur l'intervale $[x_0, 0]$ grâce à `matplotlib` et vérifier que la racine se trouve dans cette intervalle. On pourra pour la suite choisir un intervale $[a,b]$ de recherche par dichotomie plus petit que l'intervale précédent grâce au graphique ainsi tracé.

```{code-cell}
:tags: [remove-output,hide-input]
"""
Utiliser cette cellule pour définir la fonction f et tracer son allure sur [x0,0]

_Vous pouvez utiliser cette cellule pour trouver un x0 convenable._
"""
# Ne pas oublier d'importer les bibliothèques scientifiques

```


## Implémentation de la dichotomie.
Pour rappel, le principe de dichotomie consiste à :
1. Définir deux valeurs initiales `a0` et `b0` qui correspondent à l'intervale initial de recherche.
2. Tant que la largeur de l'intervalle $[a,b]$ est supérieure à une largeur $\epsilon$ choisie.
    1. Assigner à `c` la valeur médiane `(a+b)/2`.
    2. Si $f(c) = 0$, alors on peut remplacer l'intervale de recherche directement par $[c,c]$ et ainsi terminer la boucle avec la solution.
    3. Si $f(c) * f(b) <0$ alors le nouvel intervale de recherche devient `a,b <- c,b`.
    4. Si $f(c) * f(a) <0$ alors le nouvel intervale de recherche devient `a,b <- a,c`.
    5. Sinon, c'est que vous avez mal choisi l'intervale !
3. Une fois la boucle terminée, l'estimation de la racine (à $\epsilon /2$ près) sera le milieu du dernier intervale.


> __Exercice 2:__  
> _Si vous vous sentez à l'aise, vous pouvez passer et écrire directement une fonction (Exercice 3) pour réaliser la dichotomie._
> 1. Choisir un intervale de départ en choisissant `a0` et `b0` ainsi qu'une précision `prec`
> 2. Ecrire une série d'instructions qui réalise la dichotomie précédente et vérifier que la valeur de la racine trouvée est cohérente avec le tracé graphique.
> 3. (Math) Prévoir par le calcul le nombre d'itération de boucle nécessaire pour en fonction de $a, b$ et $\epsilon$ la précision recherchée.
> 4. Introduire un compteur dans la boucle et vérifier que le nombre d'itérations est bien celui attendu lorsqu'on chercher une précision à $10^{-12}$ près.

```{code-cell}
:tags: [remove-output,hide-input]
"""
Si vous avez exécutez la cellule précédente, la fonction f est déjà définie et les bibliothèques scientifiques sont déjà importées.
"""


```

> __Exercice 3:__  
> 1. En vous aidant du code précédent, écrire une fonction `racine(f:callable, a0:float, b0:float, prec:float) -> float` qui prend comme argument la fonction $f$ et les bornes $a0$ et $b0$ de l'intervale de recherche initial et qui renvoie la racine avec une précision $prec$.
__ATTENTION:__
* __Le premier argument est bien la FONCTION `f` et pas son _image_ f(x) en un point x.__ (`callable` est pour Python le type d'une fonction)
* __Une fonction (comme `racine`) NE DOIT PAS MODIFIER ses arguments (même si Python vous laissera faire). Votre fonction ne doit pas modifier `a0` et `b0`. Il faudra assigner leur valeur à deux autres variables dans le corps de la fonction.
> 2. Vérifier que vous obtenez bien une racine correcte puis utiliser cette fonction pour déterminer les racines des fonctions suivantes (il n'est pas demandé de démonstratino mathématique de l'unicité mais pensez TOUJOURS à tracer la fonction pour choisir un intervale de recherche):
* $g(x) = \sin (x) - x / 2$ avec $x > 0$ à $10^{-12}$ près.
* $h(x) = \ln (x) + x$ à $10^{-12}$ près.

```{code-cell}
:tags: [remove-output,hide-input]
"""A vous de coder"""

```

## Fonction scipy
La fonction `bisect` du sous-module `scipy.optimize` permet de réaliser une recherche de racine par dichotomie. __L'utilisation de cette fonction n'enlève pas la nécessité d'étudier au préalable la fonction pour choisir un intervalle de départ.__ La signature de la fonction est:

```
bisect(f:callable, a:float, b:float) -> float
```
_La précision est par défaut de $10^{-12}$. Elle peut-être modifiée avec l'argument optionnel `xtol=...:float`_

> __Exercice 4:__  
> 1. Utiliser la fonction `bisect` pour déterminer la racine des trois fonctions étudiées précédemment et comparer aux résultats précédents.

```{code-cell}
:tags: [remove-output,hide-input]
"""
Ne pas oublier d'importer la fonction bisect. Inutile d'importer tout le module scipy.optimize
"""

```

## (Facultatif) Pour aller plus loin

### Autres conditions
Pour terminer la boucle, on peut imposer d'autres conditions:
* on peut vérifier que $f(a)$ et $f(b)$ sont inférieur à une valeur $precy$ choisie arbitrairement.
* on peut aussi tester un écart relatif $\vert b-a \vert / \vert b \vert < rtol$

> 1. Modifier votre fonction `racine` pour tester l'une de ses deux conditions et afficher le nombre d'itérations (avec `print` dans la fonction, ne pas enlever le return !). L'efficacité des méthodes conditions précédentes et la précisions obtenues dépend de la fonction qu'on étudie. Il n'y a pas de solution miracle (sauf à tout tester mais bon...)

### Implémentation récursive
Une fonction récursive est une fonction qui s'appelle elle-même. La dichotomie s'y prête tout à fait car une fois le nouvel intervale $[a,b]$ crée, on va devoir refaire la même suite d'instruction. Il n'est alors plus nécessaire de faire une boucle. La récursivité s'en charge de manière implicite ce qui simplifie en général l'écriture de la fonction.

A titre d'exemple, on peut calculer $n! = n \times (n-1) \times \ldots \times 2 \times 1$ de manière récursive:
```
# Implémentation récursive
def factorielle(n):
  if n == 1:  # Initialisation nécessaire
    return 1
  else:
    return n * factorielle(n-1)

# au lieu de

def factorielle(n):
  s = 1
  for k in range(1,n + 1):
    s = s * k
  return s
```

> 1. Si vous comprenez ce concept (qui sera vu plus en détail en informatique), vous pouvez essayez de réécrire la fonction `racine`, mais de manière récursive.

_Un devoir avec modélisation physique sera proposé en électrocinétique._