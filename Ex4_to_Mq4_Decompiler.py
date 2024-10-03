import tkinter as tk
from tkinter import filedialog
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
    if not os.path.exists(decompiler_path):
        result_label.config(text="Decompiler not found!", fg="red")
        return
    
    command = f'{decompiler_path} "{ex4_file_path}" "{mq4_output_path}"'

    try:
        subprocess.run(command, shell=True, check=True)
        result_label.config(text=f"Successfully converted {ex4_file_path} to {mq4_output_path}", fg="green")
    except subprocess.CalledProcessError as e:
        result_label.config(text=f"Error during conversion: {e}", fg="red")
    except Exception as e:
        result_label.config(text=f"An unexpected error occurred: {e}", fg="red")

def create_gui():
    root = tk.Tk()
    root.title("EX4 to MQ4 Converter")

    browse_button = tk.Button(root, text="Browse EX4 File", command=convert_ex4_to_mq4)
    browse_button.pack(pady=20)

    global result_label
    result_label = tk.Label(root, text="", fg="green")
    result_label.pack()

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
