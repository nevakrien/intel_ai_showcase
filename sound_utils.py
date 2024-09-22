from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import simpleaudio as sa
import sounddevice as sd
from IPython.display import Audio
import librosa


def generate_sine(freq,duration):
    sample_rate = 44100
    frequency = freq  # 440 = Frequency of the sine wave (A4 note)

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = np.sin(2 * np.pi * frequency * t)

    # Normalize to 16-bit range
    y = np.int16(y * 32767)
    return y
    

def plot_2_sines(y1,y2,title1, title2, plot_duration, t):
    sample_rate = 44100
      
    # Limit the plot to only 0.1 seconds
    plot_samples = int(sample_rate * plot_duration)
    t_plot = t[:plot_samples]
    y1 = y1[:plot_samples]
    y2 = y2[:plot_samples]
    
    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Plot the sine wave for the first 0.1 seconds on the first subplot
    ax1.plot(t_plot, y1)
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Amplitude')
    ax1.set_title(title1)
    
    # Plot the entire sine wave on the second subplot
    ax2.plot(t_plot, y2)
    ax2.set_xlabel('Time [s]')
    ax2.set_ylabel('Amplitude')
    ax2.set_title(title2)
    
    plt.tight_layout()
    plt.show()

def plot_spectogram( y1, y2 ,title1, title2 ):
    sample_rate = 44100
    
    # Create subplots for spectrograms
    fig, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Plot the spectrogram for the first 0.1 seconds on the first subplot
    ax3.specgram(y1, Fs=sample_rate)
    ax3.set_xlabel('Time [s]')
    ax3.set_ylabel('Frequency [Hz]')
    ax3.set_title(title1)
    
    # Plot the spectrogram for the entire duration on the second subplot
    ax4.specgram(y2, Fs=sample_rate)
    ax4.set_xlabel('Time [s]')
    ax4.set_ylabel('Frequency [Hz]')
    ax4.set_title(title2)
    
    plt.tight_layout()
    plt.show()