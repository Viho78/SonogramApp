import matplotlib
import scipy

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

from scipy.io import wavfile
import matplotlib.pyplot as plot

import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path

import os

import numpy as np


class PageThree(tk.Frame):

    def Hamming(self, button5,button8, button4):
        button5.config(state="disabled")
        button8.config(state="disabled")
        button4.config(state="disabled")

        if (self.canvas2 == None):
            self.x = 1

            rate, k = wavfile.read(filename)

            self.f1, self.a1 = plot.subplots(1)
            self.a1.clear()

            self.a1.set_title('Spectro')
            plot.xlabel("Time(s)")
            plot.ylabel("frequency(Hz)")

            try:
                self.a1.specgram(k, Fs=rate, window=scipy.hamming(256), NFFT=256, cmap='Purples')
            except ValueError:
                k = k[:,1]
                self.a1.specgram(k, Fs=rate, window=scipy.hamming(256), NFFT=256, cmap='Purples')

            self.canvas2 = FigureCanvasTkAgg(self.f1)
            self.canvas2.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            self.toolbar = NavigationToolbar2Tk(self.canvas2, app)
            self.toolbar.update()

            self.canvas2._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.f2, self.a2 = plot.subplots(1)
            Time = np.linspace(0, len(k) / rate, num=len(k))
            self.a2.clear()
            self.a2.set_title('Sound')
            self.a2.plot(Time, k, color="m")
            plot.xlabel("Time(s)")
            plot.ylabel("Amplitude")
            #formatter = matplotlib.ticker.FuncFormatter(lambda ms, x: time.strftime('%M:%S', time.gmtime(ms // 1000)))
            #self.a2.xaxis.set_major_formatter(formatter)

            self.canvas3 = FigureCanvasTkAgg(self.f2)
            self.canvas3.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            self.canvas3._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def gtsnd(self, button5, button8, button4):
        button5.config(state="disabled")
        button8.config(state="disabled")
        button4.config(state="disabled")

        if (self.canvas2 == None):
            self.x = 1

            rate, k = wavfile.read(filename)

            self.f1, self.a1 = plot.subplots(1)
            self.a1.clear()

            self.a1.set_title('Spectro')
            plot.xlabel("Time(s)")
            plot.ylabel("frequency(Hz)")

            try:
                self.a1.specgram(k, Fs=rate, cmap='Purples')
            except ValueError:
                k = k[:,1]
                self.a1.specgram(k, Fs=rate, cmap='Purples')

            self.canvas2 = FigureCanvasTkAgg(self.f1)
            self.canvas2.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            self.toolbar = NavigationToolbar2Tk(self.canvas2, app)
            self.toolbar.update()

            self.canvas2._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.f2, self.a2 = plot.subplots(1)
            Time = np.linspace(0, len(k) / rate, num=len(k))
            self.a2.clear()
            self.a2.set_title('Sound')
            plot.xlabel("Time(s)")
            plot.ylabel("Amplitude")
            #formatter = matplotlib.ticker.FuncFormatter(lambda ms, x: time.strftime('%M:%S', time.gmtime(ms // 1000)))
            #self.a2.xaxis.set_major_formatter(formatter)
            self.a2.plot(Time, k, color="m")

            self.canvas3 = FigureCanvasTkAgg(self.f2)
            self.canvas3.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


            self.canvas3._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    def ResetSono(self,button5, button8, button4):
        button5.config(state="enabled")
        button8.config(state="enabled")
        button4.config(state="enabled")
        self.canvas2.get_tk_widget().pack_forget()
        self.canvas3.get_tk_widget().pack_forget()
        self.toolbar.destroy()
        pom = 0
        if (pom == 0):
            pom = 1
            self.label3 = tk.Label(self, text="Please choose your sound file again")
            self.label3.pack(anchor="nw", side='left', padx=5)


    def SetCanv(self):
        self.canvas2 = None
        self.label3.destroy()

    def Play(self):
        os.startfile(filename)



    def __init__(self, parent, controller):
        self.x = 0
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="SONOGRAM", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)
        self.canvas2 = None

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack(anchor="nw",side='left', padx=5)

        button4 = ttk.Button(self, text="Get sound", command=lambda: [controller.show_frame(GetSound), self.SetCanv()])
        button4.pack(anchor="nw",side='left', padx=70)

        button5 = ttk.Button(self, text="SHOW", command=lambda: self.gtsnd(button5, button8, button4))
        button5.pack(anchor="nw",side='left', padx=5)

        button8 = ttk.Button(self, text="SHOW Hamming windowing", command=lambda: self.Hamming(button5, button8, button4))
        button8.pack(anchor="nw", side='left', padx=5)

        button7 = ttk.Button(self, text="Reset", command=lambda: self.ResetSono(button5, button8, button4))
        button7.pack(anchor="nw",side='left', padx=5)

        button7 = ttk.Button(self, text="Play Sound", command=lambda: self.Play())
        button7.pack(anchor="nw", side='left', padx=130)



LARGE_FONT = ("Helvetica", 12)


class GetSound(tk.Frame):

    def getsnd(self):
        global filename
        filename = None
        filename = fd.askopenfilename(filetypes=[("wav files", ".wav")])
        self.button6.config(state="disabled")
        if(filename != None and filename!= ""):
                self.label8 = tk.Label(self, text="Your file has been successfully uploaded")
                self.label8.pack(anchor="nw",side='left', padx=5)
        else:
                self.label7 = tk.Label(self, text="Your file has NOT been successfully uploaded. Return and try to load file again")
                self.label7.pack(anchor="nw", side='left', padx=5)

    def RecordPom(self):
        fs = 44100
        seconds = 5  # Duration of recording
        global filename
        sound = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()  # Wait until recording is finished
        self.label5 = tk.Label(self, text="Finished")
        self.label5.pack(anchor="nw", side='left', padx=5)
        write('output.wav', fs, sound)
        dirname = 'C:/Users/julek/Desktop/SonogramProjektPy'
        fname = 'output'
        suffix = '.wav'
        filename = Path(dirname, fname).with_suffix(suffix)


    def Record(self):
        self.button6.config(state="disabled")
        self.button1.config(state="disabled")
        self.label4 = tk.Label(self, text="Recording for 5 second. Click Start Recording")
        self.label4.pack(anchor="nw", side='left', padx=5)

        self.button8 = ttk.Button(self, text="Start Recording", command=lambda: self.RecordPom())
        self.button8.pack(anchor="nw", side='left', padx=5)


    def MsgDestr(self):
        self.button6.config(state="enabled")
        self.button1.config(state="enabled")

        self.label5.destroy()
        self.label7.destroy()
        self.label8.destroy()
        self.button8.destroy()
        self.label4.destroy()
        #tk.Frame.destroy()


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="SPECTROGRAM", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)
        self.label5 = tk.Label()
        self.label4 = tk.Label()
        self.label7 = tk.Label()
        self.label8 = tk.Label()
        self.button8 = ttk.Button()
        self.button6 = ttk.Button(self, text="Choose your file", command=self.getsnd)
        self.button6.pack(anchor="nw",side='left', padx=5)

        self.button1 = ttk.Button(self, text="Record your own sound", command=lambda: self.Record())
        self.button1.pack(anchor="nw", side='left', padx=5)

        self.button5 = ttk.Button(self, text="Return", command=lambda: [controller.show_frame(PageThree), self.MsgDestr()])
        self.button5.pack(anchor="nw",side='left', padx=50)



class MMain(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "Spetrogram")
        tk.Tk.wm_state(self,'zoomed')


        cont = tk.Frame(self)
        cont.pack(side="top", fill="both", expand=True)
        cont.grid_columnconfigure(0, weight=1)
        cont.grid_rowconfigure(0, weight=1)

        self.frames = {}

        for FR in (StartPage, PageOne, PageThree, GetSound):
            frame = FR(cont, self)

            self.frames[FR] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, contt):
        frame = self.frames[contt]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Hello", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="About",command=lambda: controller.show_frame(PageOne))
        button.pack()

        button3 = ttk.Button(self, text="Graph Page",command=lambda: controller.show_frame(PageThree))
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Author: ", font=LARGE_FONT)
        label = tk.Label(self, text="Juliusz Stańczyk 107408 ", font=14)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = MMain()
app.mainloop()
