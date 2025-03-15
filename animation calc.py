import tkinter as tk
from tkinter import ttk
import math

class AnimatedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Superhero Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg='#1A1A2E')  # Dark theme background like Batman
        
        self.expression = ""
        self.create_widgets()
        
    def create_widgets(self):
        self.display_var = tk.StringVar()
        self.display_label = ttk.Label(self.root, textvariable=self.display_var, font=("Arial", 24), anchor="e", background='#E63946', foreground='white', padding=10)  # Red like Iron Man
        self.display_label.pack(fill='both', padx=10, pady=10)
        
        button_frame = ttk.Frame(self.root)
        button_frame.pack(expand=True, fill='both')
        
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+')
        ]
        
        colors = {"number": "#3498DB", "operator": "#F4D03F", "special": "#27AE60"}  # Blue (Superman), Gold (Wonder Woman), Green (Hulk)
        
        for row in buttons:
            row_frame = ttk.Frame(button_frame)
            row_frame.pack(expand=True, fill='both')
            for char in row:
                color = colors["number"] if char.isdigit() else colors["operator"] if char not in ('C', '=') else colors["special"]
                btn = tk.Button(row_frame, text=char, font=("Arial", 18, "bold"), width=5, height=2, bg=color, fg="black", bd=0, relief='ridge', command=lambda c=char: self.on_button_click(c))
                btn.pack(side='left', expand=True, fill='both', padx=5, pady=5)
                self.animate_button(btn, color)
        
    def animate_button(self, button, default_color):
        def on_enter(e):
            button.configure(bg="#FF5733")  # Fiery effect like Human Torch
        def on_leave(e):
            button.configure(bg=default_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += char
        self.display_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedCalculator(root)
    root.mainloop()
