import librosa
import numpy as np


def generate_chirp(duration_ms=1000) -> np.ndarray:
    audio = librosa.chirp(duration=duration_ms/1e3, fmin=200, fmax=4000, sr=16000, linear=True)
    return audio.astype('float32')
