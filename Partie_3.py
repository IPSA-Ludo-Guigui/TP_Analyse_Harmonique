import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Partie 3 :


#on choisit un N arbitraire, N est la longueur du signal, en changeant la valeur de N on peut voir comment cela affecte la résolution fréquentielle
#génerer le signal
N = 1024
t = np.linspace(0, 1, N, endpoint=False)

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
    # Calcul de la transformée de Fourier discrète
    X = np.fft.fft(fonctions[cles_liste[i]])
    freqs = np.fft.fftfreq(N, 1/N)

    #Théorème de Parseval
    parseval_domaine_temporel = np.sum(np.abs(fonctions[cles_liste[i]])**2)
    parseval_domaine_freq = (1/N) * np.sum(np.abs(fonctions[cles_liste[i]]**2))

    #afficher les résultats
    print("Parseval dans le domaine temporel:", parseval_domaine_temporel)
    print("Parseval dans le domaine fréquentiel:", parseval_domaine_freq)

    # Affichage du signal et de sa transformée de Fourier
    plt.subplot(2, 1, 1)
    plt.plot(t, fonctions[cles_liste[i]])
    plt.title('Signal dans le domaine temporel')

    plt.subplot(2, 1, 2)
    plt.plot(freqs, np.abs(X))
    plt.title('Transformée de Fourier du signal')
    plt.xlabel('Fréquence (Hz)')
    plt.tight_layout()
    #plt.savefig(f"figure_fct_pt3_parseval_{cles_liste[i]}") #sauvegarde les figures pour le dossier image
    plt.show()