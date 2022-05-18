# -*- coding: utf-8 -*-
"""
Created on Tue Apr  13 23:52:57 2022

@author: arife
"""


#import librosa and load the audio file
import librosa
audio_path = 'C:/Users/arife/Desktop/genres/blues/blues.00000.au'
new_audio_path = 'http://localhost:8888/edit/Desktop/genres/blues/blues.00000.au'
x , sr = librosa.load(audio_path)
print(type(x), type(sr))

#display the audio
import IPython.display as ipd
ipd.Audio(audio_path)

#display wavefrom
import matplotlib.pyplot as plt
import librosa.display
plt.figure(figsize=(14, 5))
librosa.display.waveshow(x, sr=sr)

#display Spectrogram
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz') 
#Frekansları yazdırmak için
#librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()

x, sr = librosa.load(audio_path)
#Plot the Signal
plt.figure(figsize=(14, 5))
librosa.display.waveshow(x, sr=sr)

# Zooming in
n0 = 9000
n1 = 9100
plt.figure(figsize=(14, 5))
plt.plot(x[n0:n1])
plt.grid()

#ZCR output
zero_crossings = librosa.zero_crossings(x[n0:n1], pad=False)
print(sum(zero_crossings))

#spectral centroid -- centre of mass -- weighted mean of the frequencies present in the sound
import sklearn
spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]
spectral_centroids.shape
# Computing the time variable for visualization
frames = range(len(spectral_centroids))
t = librosa.frames_to_time(frames)
# Normalising the spectral centroid for visualisation
def normalize(x, axis=0):
    return sklearn.preprocessing.minmax_scale(x, axis=axis)
#Plotting the Spectral Centroid along the waveform
librosa.display.waveshow(x, sr=sr, alpha=0.4)
plt.plot(t, normalize(spectral_centroids), color='r')

#MFCC
mfccs = librosa.feature.mfcc(x, sr=sr)
print(mfccs.shape)
librosa.display.specshow(mfccs, sr=sr, x_axis='time')

