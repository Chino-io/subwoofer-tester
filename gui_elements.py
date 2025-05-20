import tkinter as tk
from config import distortion_threshold, playing_sounds
from audio_engine import generate_sub_bass

def toggle_note(freq, button):
    if freq in playing_sounds:
        playing_sounds[freq].stop()
        del playing_sounds[freq]
        button.config(bg="SystemButtonFace")
    else:
        sound = generate_sub_bass(freq)
        sound.play(loops=-1)
        playing_sounds[freq] = sound
        button.config(bg="lightgreen")

def set_volume(val, warn_label):
    import config
    config.volume = float(val)
    if config.volume > distortion_threshold:
        warn_label.config(text="⚠️ Distortion Risk!", fg="red")
    else:
        warn_label.config(text="✓ Clean", fg="green")

def update_marker(slider, marker):
    x_pos = distortion_threshold * slider.winfo_width()
    marker.place(x=x_pos, y=-5)
