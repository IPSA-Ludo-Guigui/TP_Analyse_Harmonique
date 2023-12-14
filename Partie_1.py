import numpy as np
import matplotlib.pyplot as plt

N = 128

#Les différents cas
x_cas = {
    'cas1': np.zeros(N),
    'cas2': np.zeros(N),
    'cas3': np.zeros(N),
    'cas4': np.zeros(N),
    'cas5': np.zeros(N)
}

x_cas['cas1'][:] = 1  # Tous les éléments doivent être 1
x_cas['cas2'][0] = 1  # x0 = 1 et pour 1 <= k < N, xk = 0
x_cas['cas3'][1] = 1  # x1 = 1 et pour k != 1, xk = 0
x_cas['cas4'] = np.cos((2 * np.pi * np.arange(N)) / N)  # xk = cos(2*pi*k/N)
x_cas['cas5'][:N//2] = 1  # xk = 1 pour k < N/2 et xk = 0 pour k >= N/2

# Calculer la TFD pour chaque cas
dft_results = {cas: np.fft.fft(x) for cas, x in x_cas.items()}

def plot_dft_results(dft_results, cas):
    x = np.arange(N)
    y = dft_results[cas]
    fig, axs = plt.subplots(4, 1, figsize=(10, 8))

    axs[0].plot(x, y.real, label='Partie réel')
    axs[0].set_title(f'Partie réel du {cas}')
    axs[0].legend()

    axs[1].plot(x, y.imag, label='Partie Imaginaire', color='orange')
    axs[1].set_title(f'Partie imaginaire du {cas}')
    axs[1].legend()

    axs[2].plot(x, np.abs(y), label='Module', color='green')
    axs[2].set_title(f'Module du {cas}')
    axs[2].legend()

    axs[3].plot(x, np.angle(y), label='Argument', color='red')
    axs[3].set_title(f'Argument du {cas}')
    axs[3].legend()

    plt.tight_layout()
    plt.show()

for cas in dft_results:
    plot_dft_results(dft_results, cas)
