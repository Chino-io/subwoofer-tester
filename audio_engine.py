import numpy as np
import pygame
from config import SAMPLE_RATE, volume, boost_gain

pygame.mixer.pre_init(SAMPLE_RATE, -16, 2)
pygame.init()

def apply_envelope(wave, fade_len=300):
    fade_in = np.linspace(0, 1, fade_len)
    fade_out = np.linspace(1, 0, fade_len)
    wave[:fade_len] *= fade_in
    wave[-fade_len:] *= fade_out
    return wave

def generate_sub_bass(freq, duration=2.0):
    from config import volume  # re-imported in case updated dynamically
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    waveform = np.sin(2 * np.pi * freq * t) * volume * boost_gain
    waveform = apply_envelope(waveform)
    waveform = np.clip(waveform, -1, 1)
    waveform_int16 = np.int16(waveform * 32767)
    stereo = np.column_stack((waveform_int16, waveform_int16))
    return pygame.sndarray.make_sound(stereo)
