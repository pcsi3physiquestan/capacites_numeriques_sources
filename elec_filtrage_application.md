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


# Application du filtre

## Fonctions utiles

Cette activité fait suite à l'activité où vous avez appris à reconstruire un signal à partir des ses composantes spectrales. Pour gagner du temps les fonctions utiles qui avaient déjà été implémentées sont redonnées ici.

```{code-cell} ipython3
from numpy.fft import fft, ifft
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read, write  # Pour importer et écrire un fichier son wav

def fonc_temp(t, fs, amps, phis):
    """
    Renvoie la somme des composantes spectrales définies par
    - leurs fréquences freqs
    - leurs amplitudes amprs
    - leurs phases à l'origine phis
    et le calcul à un temps t.
    Cette fonction est vectorialisable : t peut-être un vecteur numpy
    """
    n = len(fs)  # Nombre de composantes spectrales
    s = 0  # Initialisation de la valeur du signal
    for i in range(n):  # On va parcourir les composantes
        if i % 2000 == 0:
            print("{:.0f} %".format(i / n * 100))
        s += 2 * amps[i] * np.cos(2 * np.pi * fs[i] * t + phis[i])  # On ajoute la composante spectrale
    return s


def evalue_temp(fs, amps, phis, t1, t2, N):
    """
    Renvoie deux vecteurs : 
    - un vecteur de N valeurs de temps tk entre t1 et t2
    - un vecteur donnant le signal reconstruit à partir de 
    (fs(fréquence), amps(amplitudes), phis(phase à l"origine))
    calculé aux temps tk
    """
    ts = np.linspace(t1, t2, N)  # Création du vecteur temps
    return ts, fonc_temp(ts, fs, amps, phis)  # Les opérations de evalue_temp sont toutes vectorialisables


def eval_fft(s, fe):
    """
    Calcul la transformée de Fourier du signal donnée par le vecteur s et échantillonné à la fréquence fe
    Il renvoie :
    - la liste de fréquences
    - la liste des amplitudes (jusqu'à fe/2)
    - la liste des phases à l'origine
    Pour un vecteur s de taille N, la taille de la décomposition sera int(N/2) 
    avec un pas de fréquence fe / N
    """
    N = len(s)  # Taille de s pour le vecteur des fréquences
    freqs = np.arange(int(N / 2)) * fe / N  # Liste de fréquence
    sk = fft(s) / N  # Calcul de la TF
    return freqs, np.abs(sk)[:int(N/2)] * 2, np.angle(sk)[:int(N/2)]

```

## Filtre choisi

> Recopier dans la cellule ci-dessous la fonction `butterworth` précédemment créée ainsi que les valeur `nmin` et `fc` choisie pour le dimensionnement (remarque : vous pouvez même créer une fonction `butterworth(f)` et mettre nmin et fc comme variable locale car elles ne changeront plus.)

```{code-cell}
:tags: [remove-output,hide-input]
# Les bibliothèques scientifiques ont déjà été importées. PENSEZ A EXECUTER LA CELLULE PRECEDENTE.

```

## Application à des signaux simples.
Nous allons tester le filtre sur des signaux simples:
* un signal sinusoïdal de basse fréquence puis de haute fréquence
* un signal modulé en amplitude
* un signal créneau représenté par ses n premières composantes spectrales.


> __Exercice 1:__  
> 1. Définir trois __vecteurs__ `fs,amps, phis` représenter le spectre d'un signal d'entrée sinusoïdal de fréquence 100Hz puis utiliser la fonction `butterworth` pour obtenir les mêmes trois vecteurs `fss, ampss, phiss` pour le signal de sortie correspondant. Utiliser la fonctio `evalue_temp` pour tracer le signal d'entrée etle signal de sortie correspondant sur un même graphique. Obtient-on ce qu'on attend?
> 2. Refaire de même pour un signal sinusoïdal de fréquence 10kHz.
> 3. Refaire de même pour un signal modulé en amplitude contenant deux fréquences : l'une de 100Hz et l'autre de 10kHz et ayant la même amplitude.
> 4. Refaire de même pour un signal créneau de fréquence 10kHz défini par ses $n=10$ premières harmoniques. On rappelle la décomposition d'un signal créneau est:

$$
s_{creneau} = \sum_{i=1}^{m} {4 \over \pi (2i + 1)}\ \cos \left ( 2 \pi (2i + 1) f_0 t - \frac{\pi}{2}\right)
$$

## Application au signal sonore
### Importation d'un fichier wav
Le signal considéré est téléchargeable par [ce lien](https://github.com/pcsi3physiquestan/donnees_exp/blob/main/signal_bruitee.wav?raw=true). _Pensez à placer votre fichier au niveau du notebook pour pouvoir importer le fichier_. On rappelle que les tracés temporels et fréquentiels ont déjà été donné précédemment.


La cellule ci-dessous importe le signal sonore bruité et obtient le spectres (fréquence, amplitude et phase à l'origine) pour les deux signaux gauche et droite. Rien n'est à modifier mais __pensez à exécuter la cellule et à noter les variables à réutiliser pour la suite.__

```{code-cell} ipython3
:tags: [remove-output,hide-input]

filename = 'sources/signal_bruitee.wav'  # Entrer ici le chemin relatif vers le fichier sonore téléchargé
samplerate, datas = read(filename)

print('--------------')
print("Fréquence d'échantilonnage : {} ech/s".format(samplerate))
print('--------------')

"""Séparation des signaux gauche et droite"""
gauche = datas[:, 0]  # Signal gauche
droite = datas[:, 1]  # Signal droite
npt = len(gauche)  # Nombre de points du signal

freqs_g, amps_g, phis_g = eval_fft(gauche, samplerate)  # On utilise la fonction donnée
freqs_d, amps_d, phis_d = eval_fft(gauche, samplerate)  # On utilise la fonction donnée

```

### Réalisation du filtrage
> __Exercice 2 :__  
> 1. Ecrire une fonction `reponse(fs, amps, phis)` qui prend comme argument la décomposition spectrale d'un signal d'entrée (`fs`(fréquence), `amps`(amplitudes), `phis`(phase à l'origine). et qui renvoie la décomposition spectrale du signal de sortie sous la forme de 2 vecteurs : les amplitudes de chaque composantes et les phases à l'origine de chaque composante pour le filtre de Butterworth.
> 2. Appliquer la fonction `reponse` avec le filtre de Butterworth dimensionnée précédemment aux signaux gauche et droite de l'extrait sonore bruité.
> 3. Tracer le spectre des deux signaux gauche et droite __traités__ par le filtre. Vérifier que le filtre abien jouer son rôle.


```{code-cell} ipython3
:tags: [remove-output,hide-input]

```

> __Exercice 3:
> 4. Recréer les signaux temporels filtrés `s_gauche` et `s_droite` à partir des représentations fréquentielles obtenues précédemment. (Il est important de bien respecter ces deux noms.

__Attention, il y a plus de 10000 fréquences pour reconstruire le signal. Cela peut prendre un peu de temps. Pensez à sauvegarder votre travail avant d'exécuter la cellule.__ Un compteur affiche l'avancé de la reconstruction du signal temporel lors de l'utilisation de la fonction `evalue_temp`.

_Respecter les noms es variables pour les deux signaux temporels car ils vont servir à la création du signal sonore final._

```{code-cell}
:tags: [remove-output,hide-input]

```

### Création du fichier sonore
Si tout à été fait correctement, la cellule ci-dessous peut-être exécutée directement. Elle va créer un fichier sonore `.wav` à partir du signal filtré. Il ne vous reste plus qu'à écouter (VLC ou Audacity) le signal ainsi obtenu pour vérifier qu'on a bien filtré le bruit parasite.

Vous pourrez le comparer à l'[extrait original](https://github.com/pcsi3physiquestan/donnees_exp/blob/main/signal_court.wav?raw=true) (le bruit ayant été ajouté artificiel pour ce TD).

```{code-cell} ipython3
:tags: [remove-output,hide-input]
# On doit normaliser le signal pour que les valeurs soit comprises entre -1 et 1
# En pratique, on place les valeurs entre -0.5 et 0.5 pour éviter tout risque de saturation
reponse2 = []
reponse2.append(s_gauche / np.max(s_gauche) * 0.5)
reponse2.append(s_droite / np.max(s_droite) * 0.5)
reponse2 = np.array(reponse2)  # La fonction write impose l'utilisation d'un array


filesortie = 'signal_filtree.wav'  # Nom du fichier, il sera dans le même répertoire que votre notebook
write(filesortie, samplerate, reponse2)
```

## Conclusion
Nous avons donc pu réaliser le traitement d'un signal. Même s'il a été fait sur des signaux numériques, ce traitement reste "analogique" au sens où il suit exactement le même procédé qu'un filtre analogique étudié en TP.

Cette méthode est néanmoins problématique car elle demande beaucoup de ressource et du temps de calcul (on n'a ici traité que 2s secondes de musique échantilonnée à 8kHz, ce qui est peu et la reconstruction du signal était déjà longue).

En pratique, le traitement d'un signal numérique se fait par des filtres __numériques__ qui s'appliquent directement sur le signal temporel échantillonné ($s_k$). Certains de ces filtres seront vus en deuxième année suivant les options. La bibliothèques `scipy` propose notamment plusieurs fonctions natives et optimisées pour le traitement des signaux numériques (sous bibliothèques `scipy.signal`).

On ne présente pas ici ces méthodes qui ne sont pas au programme mais sachez qu'on peut notamment utiliser un filtre de Butterworth ou son équivalent numérique grâce à cette bibliothèque.

