---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,py:light,md:myst
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


# Dimensionnement du filtre

On va considérer qu'il convient :
* de garder un gain supérieur à $G_1 = 0.9$ au dessous de $f_1 = 1500Hz$.
* d'avoir un gain inférieur à $G_2 = 0.1$ au dessus de $f_2 = 2500Hz$.

## Choix du filtre
Le filtre que nous allons choisir est un filtre passe-bas dit de Butterworth d'ordre n. Comme expliqué en devoir libre, il a les caractéristiques suivantes :
* son gain réel s'écrit sous la forme : $G = {1 \over \sqrt{1 + x^{2n}}}$ avec $x = {\omega \over \omega_c}$ et $\omega_c$ la pulsation de coupure du filtre.

L'intérêt est que quelque soit l'ordre choisi, la pulsation de coupure sera la même. On pourra donc étudier l'influence de l'ordre du filtre sans devoir réadapter sa pulsation de coupure.

Pour obtenir un tel gain réel, la fonction de transfert pour un filtre d'ordre $n$ doit s'écrire sous la forme :

$$
H(j\omega) = {1 \over \prod_{k=1}^{k=n} \left({j \omega \over \omega_c} - p_k\right)} = {1 \over \prod_{k=1}^{k=n} \left({j f \over f_c} - p_k\right)}
$$

avec $p_k = \exp\left( {j (2k + n -1 }) \pi \over 2n\right)$ et $f_c$ la fréquence de coupure du filtre.

## Ordre du filtre
> __Exercice 1:__  
> (Pensez à bien lire les indications après l'énoncé)
> 1. Ecrire une fonction `butterworth` qui renvoie la fonction de transfert complexe d'un filtre de Butterworth d'ordre `n` calculé en une fréquence `f` et qui prend comme argument :
>     * `f` la fréquence où on veut calculer la fonction de transfert.
>     * `fc` la fréquence du coupure du filtre.
>     * `n` l'ordre du filtre
> 2. En utilisant la fonction `logspace` de `numpy`, créer un vecteur de fréquence régulièrement répartie sur un axe logarithmique entre 100Hz et 10kHz. Puis utiliser ce vecteur pour tracer le diagramme de Bode en gain pour un filtre de Butterworth d'ordre 1 et de fréquence de coupure $f_c = 1kHz$. Vérifier qu'on a bien le tracé de la fonction de transfert $H(j\omega) = {1 \over 1 + j {f \over f_c}}$.
> 
> La grandeur $\eta = {G(f_2)^{-2} - 1 \over G(f_1)^{-2} - 1}$ pour un filtre de Butterworth d'ordre $n$ ne dépend pas de la fréquence de coupure, mais uniquement du rapport $f_2 /f_1$ et de l'ordre $n$ du filtre (on s'entraînera chez soi à le démontrer).  
> On peut montrer de plus que le cahier des charges impose que $\eta > {G(f_2)^{-2} - 1 \over G(f_1)^{-2} - 1}$
> 
> 3. Utiliser le calcul numérique de $\eta$ et écrire un script qui détermine l'ordre $n_{min}$ minimal que doit avoir le filtre pour le cahier des charges choisi. On travaillera par la suite avec l'ordre $n_{min}$.
>     

_Indications utiles :_
* La fonction `butterworth` ne doit pas être nécessairement vectorialisable en `f`, vous réaliserez une boucle pour créer un vecteur de valeurs pour plusieurs valeurs de `f`.
* Le nombre complexes $j$ tel $j^2 = -1$ s'écrit sous Python `1j` (le 1 est obligatoire et il est collé au j). Pour écrire $variable \times j$, on écrira : `variable * 1j` (ou évidemment `1j * variable`).
* Pour le diagramme de Bode :
    * Signature de `logspace` : `logspace(start, stop, N)` crée `N` fréquences uniformément répartie sur un axe logarithmique entre $10^{start}$ et $10^{stop}$.
    * Le module d'un complexe s'obtient avec la fonction `np.abs` et le logarithme décimal s'obtient par la fonction `np.log10`.
    * Le tracé d'un diagramme semi-log se fait avec la fonction `semilogx`, elle a les mêmes caractéristiques que la fonction `plot`
    * (Esthétique) Utiliser la fonction `ax.grid(which='both', axis='both')` pour afficher une grille semblable à celles vu sur les diagrammes de Bode.

```{code-cell} ipython3
:tags: [remove-output,hide-input]
# Ne pas oublier d'importerles modules scientifiques.

```

## Choix de $f_c$
_Pour toute la suite, on travaillera avec un filtre d'ordre $n_{min}$._

> __Exercice 2:__  
> 1. Ecrire un script qui, par dichotomie entre deux valeurs de fréquence $f_1$ et $f_2$ détermine la fréquence de coupure telle que $G(f_1) = 0.9$. Vérifier alors que $G(f_2) < 0.1$. On s'autorise un écart de $10^{-1} Hz$ sur la fréquence.
> 2. Tracer le diagramme de Bode en gain du filtre pour $f_c$ trouvée précédemment et vérifier visuellement son ordre et que les gains en $f_1$ et $f_2$ suivent le cahier des charges.

```{code-cell} ipython3
:tags: [remove-output,hide-input]
# Vous pouvez utiliser (en la recopiant) la fonction `dicho` que vous avez créés dans les TP précédents.

```

Maintenant que le filtre est dimensionné, vous pouvez passer à son [utilisation](elec_filtrage_application)