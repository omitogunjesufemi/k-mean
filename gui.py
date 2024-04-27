#!/usr/bin/env python3

import customtkinter as ctk
from customtkinter import filedialog
from entry_point import main

"""
Setting up window frame for GUI
"""
app = ctk.CTk()
app.title("K-Mean CLustering GUI")
app.geometry("800x500")


def run_k_means(filepath, features, k, iterations):
    features = [x.strip() for x in features.split(",")]
    print(features)
    centroids, labels = main(file_name=filepath, features=features, k=int(k), iterations=int(iterations))
    clear_frame()
    result_label = ctk.CTkLabel(master=frame, text=centroids.to_string())
    result_label.grid(row=0, column=0, padx=10, pady=20)
    
    
def browse_file(filename_entry):
    filename = filedialog.askopenfilename(title="Select dataset file")
    filename_entry.delete(0, ctk.END)  # Clear any existing text
    filename_entry.insert(0, filename)  # Insert the selected filename into the entry widget

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()


# Create a frame to hold the widgets
frame = ctk.CTkFrame(master=app, bg_color="transparent", fg_color="transparent")
frame.pack(anchor=ctk.CENTER, pady=100, padx=50)

# To hold the filename or filepath upon upload
filename_label = ctk.CTkLabel(master=frame, text="Data Filename:")
filename_label.grid(row=0, column=0, padx=10, pady=20, sticky="e")  # Align to the right

filename_entry = ctk.CTkEntry(master=frame)
filename_entry.grid(row=0, column=1, padx=10, pady=20, sticky="w")  # Align to the left

# Features of the data to work on
features_label = ctk.CTkLabel(master=frame, text="Data Features:")
features_label.grid(row=0, column=2, padx=10, pady=20, sticky="e")  # Align to the right

features_entry = ctk.CTkEntry(master=frame,
                              placeholder_text="e.g.: overall, potential, wage_eur, value_eur, age")
features_entry.grid(row=0, column=3, padx=10, pady=20, sticky="w")  # Align to the left

# Number of clusters (k)
k_label = ctk.CTkLabel(master=frame, text="No. of clusters (k):")
k_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")  # Align to the right

k_entry = ctk.CTkEntry(master=frame)
k_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")  # Align to the left

# Maximum number of iterations
max_iter_label = ctk.CTkLabel(master=frame, text="Max iterations:")
max_iter_label.grid(row=1, column=2, padx=10, pady=5, sticky="e")  # Align to the right

max_iter_entry = ctk.CTkEntry(master=frame)
max_iter_entry.grid(row=1, column=3, padx=10, pady=5, sticky="w")  # Align to the left

# Button to upload file
upload_button = ctk.CTkButton(master=frame,
                              text="Upload File",
                              command=lambda: browse_file(filename_entry=filename_entry))
upload_button.grid(row=3, column=0, columnspan=2, pady=30)  # Span 2 columns and add padding

# Button to start clustering
start_button = ctk.CTkButton(master=frame,
                             text="Start Clustering",
                             command=lambda: run_k_means(filepath=filename_entry.get(), features=features_entry.get(), k=k_entry.get(), iterations=max_iter_entry.get()),
                             fg_color="green",
                             hover_color="darkgreen")
start_button.grid(row=3, column=2, columnspan=2, pady=30)  # Span 2 columns and add padding


app.mainloop()
