#!/usr/bin/env python3

import customtkinter as ctk
from customtkinter import filedialog

"""
Setting up window frame for GUI
"""
app = ctk.CTk()
app.title("K-Mean Algorithm")
app.geometry("500x500")

frame = ctk.CTkFrame(master=app, width=300, height=250,
                     fg_color="white", corner_radius=0)
frame.pack(padx=20, pady=20)

def open_file():
    filepath = filedialog.askopenfilename(title="Select dataset file")
    print(filepath)

upload_button = ctk.CTkButton(master=frame, text="Upload File",
                              command = open_file)
upload_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

app.mainloop()
