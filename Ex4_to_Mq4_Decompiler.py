import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def convert_ex4_to_mq4():
    ex4_file_path = filedialog.askopenfilename(filetypes=[("EX4 Files", "*.ex4")])
    if not ex4_file_path:
        return

    mq4_output_path = filedialog.asksaveasfilename(defaultextension=".mq4", filetypes=[("MQ4 Files", "*.mq4")])
    if not mq4_output_path:
        return

    decompiler_path = 'path_to_decompiler/Ex4_to_Mq4_Decompiler.exe'
    
    # Check if the decompiler file exists
    if not os.path.exists(decompiler_path):
        messagebox.showerror("Error", "Decompiler file not found. Please check the path.")
        return

    command = f'"{decompiler_path}" "{ex4_file_path}" "{mq4_output_path}"'

    try:
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("Success", f"Successfully converted {ex4_file_path} to {mq4_output_path}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error converting {ex4_file_path} to {mq4_output_path}: {e}")
    except Exception as e:
        messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {e}")

def create_gui():
    root = tk.Tk()
    root.title("EX4 to MQ4 Converter")

    browse_button = tk.Button(root, text="Browse EX4 File", command=convert_ex4_to_mq4)
    browse_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
