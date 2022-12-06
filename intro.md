---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,md:myst
  split_at_heading: true
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Introduction
Le but de cet activité est de se familiariser avec les tracés graphiques et la manipulation des listes classiques et des vecteurs. On se basera sur ce qui a été fait en optique.

Si vous n'êtes pas au point sur Python, revoir [l'introduction des bases](https://stanislas.edunao.com/mod/url/view.php?id=12821) et notamment la partie sur [les bibliothèques scientifiques](https://pcsi3physiquestan.github.io/intro_python/notebook/np_vecteurs.html).

## Position du problème
On considère un microscope constitué :
* d'un objectif réalisé par une lentille mince de distance focale $f_{obj} = 4mm$ placé au point O.
* d'un oculaire dit de Ramsden constitué de deux lentilles minces de même distance focale de distance focale $f_2 = f_3 = 3cm$ distantes de $\overline{O_2 O_3} = {2 \over 3}f_3$
* la distance entre l'objectif et la première lentille de l'oculaire est $\Delta = 18cm$ (on l'appellera _intervale optique_).

Le but de l'exercice est de trouver par simulation numérique où placer un objet (de taille 1(unité arbitraire)) pour que l'image finale soit à l'infini.

__On place l'origine de l'axe optique à l'emplacement de l'objectif et on suppose que le systèmes vérifient les conditions de Gauss.__
