import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.io.wavfile import write
import soundfile as sf
import os

# Répertoire de travail courant
folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(folder)

# Création du répertoire 'artificial_sound' dans le répertoire courant
artificial_sound_folder_path = os.path.join(folder, "compressed_sound")
os.makedirs(artificial_sound_folder_path, exist_ok=True)

os.chdir(folder)
audio_folder = os.path.dirname(os.path.abspath(__file__)) + "\son"

def generate_audio(fundamental_freq, harmonics, fundamental_amp, harmonics_amp, duration, sample_rate):
    # Créez un tableau de temps pour la durée spécifiée
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Initialisez le signal audio avec des zéros
    audio_data = np.zeros(len(t))

    # Ajoutez la composante fondamentale
    audio_data += fundamental_amp * np.sin(2 * np.pi * fundamental_freq * t)

    # Ajoutez les harmoniques
    for i, harmonic_freq in enumerate(harmonics):
        audio_data += harmonics_amp[i] * np.sin(2 * np.pi * harmonic_freq * t)

    # Normalisez le signal audio (facultatif)
    audio_data /= np.max(np.abs(audio_data))

    # Enregistrez le signal audio dans un fichier WAV
    write(f"compressed_sound/audio_{note}_{pourcentage_min}.wav", sample_rate, audio_data.astype(np.float32))

def filtrer_tuples_relative(liste_tuples, pourcentage_min):
    # Trouvez l'amplitude maximale
    ymax = max(liste_tuples, key=lambda x: x[1])[1]

    # Seuil relatif
    seuil_relatif = pourcentage_min * ymax

    # Filtrez les tuples et séparez les valeurs
    filtered_frequencies = [t[0] for t in liste_tuples if t[1] >= seuil_relatif]
    filtered_amplitudes = [t[1] for t in liste_tuples if t[1] >= seuil_relatif]

    return filtered_frequencies, filtered_amplitudes

audio_files = {
    'Note_01': 'Note_01.aiff',
    'Note_02': 'Note_02.aiff',
    'Note_03': 'Note_03.aiff',
    'Note_04': 'Note_04.aiff',
    'Note_05': 'Note_05.aiff',
    'Note_06': 'Note_06.aiff',
    'Note_07': 'Note_07.aiff',
    'Note_08': 'Note_08.aiff',
    'Note_09': 'Note_09.aiff',
    'Note_10': 'Note_10.aiff',
    'Note_11': 'Note_11.aiff',
    'Note_12': 'Note_12.aiff',
    'Note_13': 'Note_13.aiff',
    'Note_14': 'Note_14.aiff',
    'Note_15': 'Note_15.aiff',
    'Note_16': 'Note_16.aiff',
    'Note_17': 'Note_17.aiff',
    'Note_18': 'Note_18.aiff',
    'Note_19': 'Note_19.aiff',
    'Note_20': 'Note_20.aiff',
    'Note_21': 'Note_21.aiff',
    'Note_22': 'Note_22.aiff',
    'Note_23': 'Note_23.aiff',
    'Note_24': 'Note_24.aiff',
}

for note, file_name in audio_files.items():
    file_path = os.path.join(audio_folder, file_name)

    # Lecture du fichier audio
    data, samplerate = sf.read(file_path)

    # Si stéréo, prendre seulement le canal gauche
    if len(data.shape) > 1:
        data = data[:, 0]

    # Calcul du pas de temps
    dt = 1 / samplerate

    # Nombre d'échantillons
    n = len(data)

    # FFT
    yf = np.fft.fft(data)
    xf = np.fft.fftfreq(n, dt)[:n // 2]

    # Recherche des pics
    peaks, _ = find_peaks(np.abs(yf[:n // 2]), height=0)

    plt.figure(figsize=(12, 6))
    plt.plot(xf, 2.0 / n * np.abs(yf[:n // 2]))
    plt.plot(xf[peaks], 2.0 / n * np.abs(yf[:n // 2])[peaks], "x")
    plt.grid()
    plt.title(f"Spectre de {note}")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.xlim(0, 2000)
    plt.show()

    # Fréquence fondamentale et harmoniques
    fundamental_freq = xf[peaks][0]
    harmonics = xf[peaks][1:]
    fundamental_amp = (2.0 / n * np.abs(yf[:n // 2]))[peaks][0]
    harmonics_amp = (2.0 / n * np.abs(yf[:n // 2]))[peaks][1:]

    pourcentage_min = 0.1
    harmonics_compressed, harmonics_amp_compressed = filtrer_tuples_relative(list(zip(harmonics, harmonics_amp)), pourcentage_min)

    print(f"Note {note}:")
    print("Fundamental Frequency:", fundamental_freq, "Hz")
    print("Fundamental Amplitude:", fundamental_amp)
    print("Harmonics:", list(zip(harmonics_compressed, harmonics_amp_compressed)))

    generate_audio(fundamental_freq, harmonics_compressed, fundamental_amp, harmonics_amp_compressed, 1, 44100)