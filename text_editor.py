import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_editor):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    text_editor.delete(1.0, tk.END)

    with open(filepath, "r") as f:
        content = f.read()
        text_editor.insert(tk.END, content)
    window.title(f"Open file: {filepath}")

def save_file(window, text_editor):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    with open(filepath, "w") as f:
        content = text_editor.get(1.0, tk.END)
        f.write(content)
    window.title(f"Save file: {filepath}")

def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_editor = tk.Text(window, font="Helvetica 18")
    text_editor.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_editor))
    open_button = tk.Button(frame, text='Open', command=lambda: open_file(window, text_editor))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
    open_button.grid(row=1, column=0, padx=5, sticky='ew')
    frame.grid(row=0, column=0, sticky="ns")

    # Corrected the usage of bind method
    window.bind("<Control-s>", lambda x: save_file(window, text_editor))
    window.bind("<Control-o>", lambda x: open_file(window, text_editor))

    window.mainloop()

main()
