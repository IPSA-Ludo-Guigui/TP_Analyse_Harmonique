#on choisit un N arbitraire, N est la longueur du signal, en changeant la valeur de N on peut voir comment cela affecte la résolution fréquentielle
#génerer le signal

N = 1024
t = np.linspace(0, 1, N, endpoint=False)

#x = np.sin(2*np.pi*5*t) + 0.5 * np.random.randn(N) #signal + bruit   exemples random
#x = 2 * np.cos(10*np.pi*t) + 7 * np.cos(2*np.pi*t)
x = np.sin(2*np.pi*t)**2

# Calcul de la transformée de Fourier discrète
X = np.fft.fft(x)
freqs = np.fft.fftfreq(N, 1/N)

#Théorème de Parseval
parseval_domaine_temporel = np.sum(np.abs(x)**2)
parseval_domaine_freq = (1/N) * np.sum(np.abs(X)**2)

#afficher les résultats
print("Parseval dans le domaine temporel:", parseval_domaine_temporel)
print("Parseval dans le domaine fréquentiel:", parseval_domaine_freq)


# Vérification de la formule de Parseval
assert np.isclose(parseval_domaine_temporel, parseval_domaine_freq), "La formule de Parseval n'est pas vérifiée."

# Affichage du signal et de sa transformée de Fourier
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Signal dans le domaine temporel')

plt.subplot(2, 1, 2)
plt.plot(freqs, np.abs(X))
plt.title('Transformée de Fourier du signal')
plt.xlabel('Fréquence (Hz)')

plt.tight_layout()
plt.show()
