import tkinter as tk
from tkinter import ttk

def generate_mad_libs():
    adjective = adjective_entry.get()
    noun = noun_entry.get()
    verb = verb_entry.get()
    adverb = adverb_entry.get()

    mad_libs = f"Once upon a time, there was a {adjective} {noun}. This {noun} liked to {verb} {adverb}."

    result_label.config(text=mad_libs)


root = tk.Tk()
root.title("Mad Libs Generator")


adjective_label = ttk.Label(root, text="Adjective:")
adjective_entry = ttk.Entry(root)

noun_label = ttk.Label(root, text="Noun:")
noun_entry = ttk.Entry(root)

verb_label = ttk.Label(root, text="Verb:")
verb_entry = ttk.Entry(root)

adverb_label = ttk.Label(root, text="Adverb:")
adverb_entry = ttk.Entry(root)

generate_button = ttk.Button(root, text="Generate Mad Libs", command=generate_mad_libs)

result_label = ttk.Label(root, text="")
adjective_label.grid(row=0, column=0)
adjective_entry.grid(row=0, column=1)
noun_label.grid(row=1, column=0)
noun_entry.grid(row=1, column=1)
verb_label.grid(row=2, column=0)
verb_entry.grid(row=2, column=1)
adverb_label.grid(row=3, column=0)
adverb_entry.grid(row=3, column=1)
generate_button.grid(row=4, column=0, columnspan=2)
result_label.grid(row=5, column=0, columnspan=2)
root.mainloop()
