# Input Statements
from IPython.display import Audio, display
import matplotlib.pyplot as plt
import numpy as np
import scipy

class AudioEdit: # Class decleration
    def __init__(self, wav_file): # Function when a new object is created
        self.sr, self.data = scipy.io.wavfile.read('String_Quart.wav')

    def shift(self, shift):
        """Shifts the data by specific frequencies"""
        data = self.data
        d = scipy.fft.dct(data)
        p = scipy.ndimage.shift(d,shift*2,cval=0.0)
        edit = scipy.fft.idct(p)
        self.data = edit

    def low_pass(self, fr):
        """Filtering High Frequencies and Leaving the Low"""
        sr = self.sr
        edit = self.data
        b,a  = scipy.signal.butter(2,fr/(sr/2.0),'low') #make a fr HZ cutoff low-pass filter
        edit = scipy.signal.filtfilt(b,a,edit)          #apply it to the data in RAM
        edit = np.asarray(edit,dtype=np.int16)          #convert back into int16
        self.data = edit

    def delay(self, ts):
        """Adding a Delay"""
        sr = self.sr
        edit = np.zeros(self.data.shape,dtype=np.int16)
        edit[:] = self.data[:]
        for s in ts:
            edit[:len(edit)-int(s*sr)] += self.data[int(s*sr):]//2
        self.data = edit

    def hi_pass(self, fr):
        """Filtering Low Frequencies and Leaving the High"""
        sr = self.sr
        edit = self.data
        b,a  = scipy.signal.butter(2,fr/(sr/2.0),'high') #make a fr HZ cutoff hi-pass filter
        edit = scipy.signal.filtfilt(b,a,edit)           #apply it to the data in RAM
        edit = np.asarray(edit,dtype=np.int16)           #convert back into int16
        self.data = edit

    def plot(self):
        """Plotting the audio file to visualize it"""
        edit = self.data
        sr = self.sr
        fig, ax = plt.subplots(1, 1, figsize=(8, 4))
        t = np.linspace(0.,len(edit)/sr,len(edit))
        ax.plot(t,edit,lw=1)
        plt.show() 

    def play(self):
        """Allows to play the audio file"""
        x = self.data
        sr = self.sr
        display(Audio(x,rate=sr, autoplay=False))

    def save(self, f_name):
        """Saves the audio file as a New File"""
        scipy.io.wavfile.write(f_name,self.sr,self.data)