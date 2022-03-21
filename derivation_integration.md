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

# Dérivation et intégration numérique

Les méthodes de dérivation et d'intégration numérique sont basées sur la définition même de ces concepts mais sans le passage à la limite.

## Dérivation numérique.

### Principe
> Rappel : Soit une fonction $f$ définie et dérivable en $x_0$. Le nombre dérivée de $f$ en $x_0$ est:
> 
> $$ f'(x_0) = \lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h}$$

L'idée de la dérivation numérique est d'approcher le nombre de dérivée $f'(x_0)$ par le calcul du taux de variation précédent pour un un $h$ non nul (on approxime donc géométriquement la tangente par la corde):

$$ f'(x_0) \approx \frac{f(x_0 + h) - f(x_0)}{h}$$

### Type de calcul
On distingue trois façon de calcul un nombre dérivé:

```{code-cell}
:tags: [remove-input, remove-output]
import numpy as np
import matplotlib.pyplot as plt
from myst_nb import glue

x = np.linspace(0, np.pi / 2, 1000)
y = np.sin(x) - x ** 3

Kd = 1.1
Kg = 2 - Kd
xd = np.array([np.pi / 4, np.pi / 4 * Kd])
yd = np.sin(xd) - xd ** 3
xg = np.array([np.pi / 4 * Kg, np.pi / 4])
yg = np.sin(xg) - xg ** 3
xc = np.array([np.pi / 4 * Kg, np.pi / 4 * Kd])
xc2 = [np.pi / 4 * Kg, np.pi / 4, np.pi / 4 * Kd]
yc = np.sin(xc) - xc ** 3

f, ax = plt.subplots()
f.suptitle("Dérivée à droite")
ax.plot(y, x, linewidth=1.3, color="blue")
ax.plot(yd, xd, linewidth=1, color="red")
ax.set_xticks(xd, label=["x0", "x0+h"])
glue("deriv_d", f, display="False")

f, ax = plt.subplots()
f.suptitle("Dérivée à gauche")
ax.plot(y, x, linewidth=1.3, color=blue)
ax.plot(yg, xg, linewidth=1, color=red)
ax.set_xticks(xg, label=["x0-h", "x0"])
glue("deriv_g", f, display="False")

f, ax = plt.subplots()
f.suptitle("Dérivée centrée")
ax.plot(y, x, linewidth=1.3, color=blue)
ax.plot(yc, xc, linewidth=1, color=red)
ax.set_xticks(xc2, label=["x0-h", "x0", "x0+h"])
glue("deriv_c", f, display="False")
```


````{tabbed} Dérivée à droite

$$ f'(x_0) \approx \frac{f(x_0 + h) - f(x_0)}{h}$$
```{glue:figure} deriv_d
:align: center
```
````

````{tabbed} Dérivée à gauche

$$ f'(x_0) \approx \frac{f(x_0) - f(x_0 - h)}{h}$$
```{glue:figure} deriv_g
:align: center
```
````

````{tabbed} Dérivée centrée

$$ f'(x_0) \approx \frac{f(x_0 + h) - f(x_0 - h)}{2h}$$
```{glue:figure} deriv_c
:align: center
```
````