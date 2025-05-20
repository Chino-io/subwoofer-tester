import tkinter as tk
from config import volume
from gui_elements import toggle_note, set_volume, update_marker

root = tk.Tk()
root.title("Subwoofer Synth")

main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

main_freqs = [40, 50, 60, 70, 80, 90, 100]
for i, freq in enumerate(main_freqs):
    btn = tk.Button(main_frame, text=f"{freq} Hz", width=10)
    btn.grid(row=i // 2, column=i % 2, padx=5, pady=3)
    btn.config(command=lambda f=freq, b=btn: toggle_note(f, b))

toggle_btn = tk.Button(root, text="▶ Show Low Subs")
toggle_btn.pack(pady=(10, 5))

sub_frame = tk.Frame(root)
sub_freqs = [10, 15, 20, 25, 30]
for i, freq in enumerate(sub_freqs):
    btn = tk.Button(sub_frame, text=f"{freq} Hz", width=10)
    btn.grid(row=i // 2, column=i % 2, padx=5, pady=3)
    btn.config(command=lambda f=freq, b=btn: toggle_note(f, b))

def toggle_subs():
    if sub_frame.winfo_ismapped():
        sub_frame.pack_forget()
        toggle_btn.config(text="▶ Show Low Subs")
    else:
        sub_frame.pack()
        toggle_btn.config(text="▼ Hide Low Subs")

toggle_btn.config(command=toggle_subs)

tk.Label(root, text="Volume").pack(pady=(10, 0))
slider_frame = tk.Frame(root)
slider_frame.pack()

volume_slider = tk.Scale(slider_frame, from_=0, to=1, resolution=0.01, orient="horizontal", length=250)
volume_slider.set(volume)
volume_slider.pack(side="left")

marker = tk.Label(slider_frame, text="⚠️", fg="orange")
marker.place(x=200, y=-5)

warn_label = tk.Label(root, text="✓ Clean", fg="green", font=("Arial", 10, "bold"))
warn_label.pack(pady=5)

volume_slider.config(command=lambda v: set_volume(v, warn_label))
volume_slider.bind("<Configure>", lambda e: update_marker(volume_slider, marker))

root.mainloop()
