import numpy as np
import matplotlib.pyplot as plt

# Paramètre
T = 10          # Intervalle de temps (1 seconde)
N = 1024         # Nombre d'échantillons
dt = T / N       # Intervalle d'échantillonnage

t = np.linspace(0.0, N*dt, N, endpoint=False) # Création de l'échelle de temps

#définitions des fonctions 
fonctions = {
    'x_t0': 2 * np.cos(10 * np.pi * t) + 7 * np.cos(2 * np.pi * t),
    'x_t1': np.sin(2 * np.pi * t)**2,
    'x_t2': np.abs(np.sin(np.pi * t)),
    'x_t3': np.exp(-t),
    'x_t4': np.sin(50 * t),
    'x_t5': np.sin(2 * np.pi * t) * np.cos(100 * np.pi * t),
    'x_t6': np.sin(2 * np.pi * t) + np.cos(100 * np.pi * t),
    'x_t7': np.sin(2046 * np.pi * t),
    'x_t8': np.sin(10 * np.pi * (10 + t) * t),
    'x_t9': np.exp(-(t - 4)**2)
}

cles = fonctions.keys()
cles_liste = list(cles)

for i in range(9, -1, -1):
    freq = np.fft.fftfreq(N, d=dt)
    x_f = np.fft.fft(fonctions[cles_liste[i]])
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(t, fonctions[cles_liste[i]])
    plt.title(f"Signal dans le domaine temporel de {cles_liste[i]}")
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitude")

    #spectre des fréquences
    plt.subplot(1, 2, 2)
    plt.stem(freq, np.abs(x_f), use_line_collection=True, markerfmt='')
    plt.title(f"Spectre de fréquences de {cles_liste[i]}")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Amplitude")

plt.show()