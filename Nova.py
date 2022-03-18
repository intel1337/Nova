import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

def credits():
    """Displaying Nova Credits"""
    messagebox.showinfo("Credits", "Dev By $hz, Logo By YourNotGG")


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Nøva - Text {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Nøva - Text {filepath}")

window = tk.Tk()
window.title("Nøva - Text")

window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=300, weight=1)

txt_edit = tk.Text(window)
txt_edit.configure(bg='#856ff8')

fr_buttons = tk.Frame(window, relief=tk.FLAT, bd=1)
fr_buttons.configure(bg='#6E58E5')

btn_open = tk.Button(fr_buttons, text="Open", command=open_file, relief=tk.FLAT)
btn_open.configure(bg='#836CFF')

btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file, relief=tk.FLAT)
btn_save.configure(bg='#836CFF')

btn_credits = tk.Button(fr_buttons, text="Credits", command=credits, relief=tk.FLAT)
btn_credits.configure(bg='#836CFF')

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_credits.grid(row=2, column=0, sticky="ew", padx=5, pady=6)




fr_buttons.grid(row=0, column=0, sticky="ns")

txt_edit.grid(row=0, column=1, sticky="nsew")
txt_edit.insert("1.0", "You're Using Nova Notepad !")

# Shortcuts

window.bind('<Control-x>', save_file)
window.iconbitmap('Nova.ico')
window.mainloop()