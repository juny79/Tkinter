import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def install_program():
    source = "dist/network_security.exe"
    target_dir = filedialog.askdirectory(title="Select Installation Directory")
    if not target_dir:
        return
    try:
        shutil.copy(source, target_dir)
        messagebox.showinfo("Success", "Installation Completed!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Network Security Installer")
root.geometry("300x150")

label = tk.Label(root, text="Click 'Install' to install the program.")
label.pack(pady=10)

install_button = tk.Button(root, text="Install", command=install_program)
install_button.pack(pady=10)

root.mainloop()
