import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Graphics():
    # Main Application Window
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CsLab")
        self.root.geometry("800x600")
        self.root.configure(bg='#2E2E2E')  # Dark background

        # Styles
        self.style = ttk.Style()
        self.style.configure("TLabel", background="#2E2E2E", foreground="#F8F8F2", font=("Courier", 12))
        self.style.configure("TButton", background="#44475A", foreground="#F8F8F2", font=("Courier", 12), borderwidth=0)
        self.style.map("TButton", background=[('active', '#6272A4')])

        # Terminal Output (Log Area)
        self.output_frame = tk.Frame(self.root, bg='#2E2E2E', bd=0)
        self.output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.output_text = tk.Text(self.output_frame, bg='#282A36', fg='#F8F8F2', insertbackground='#F8F8F2',
                            font=("Courier", 12), wrap='word', state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True)
        self.input_frame = tk.Frame(self.root, bg='#2E2E2E')
        self.input_frame.pack(fill=tk.X, padx=10, pady=10)

        self.command_entry = tk.Entry(self.input_frame, bg='#44475A', fg='#F8F8F2', font=("Courier", 12),
                                insertbackground='#F8F8F2', bd=1, relief=tk.FLAT)
        self.command_entry.pack(fill=tk.X, pady=5)
        self.command_entry.bind("<Return>", self.process_command)

        # Control Buttons (Minimalist)
        self.button_frame = tk.Frame(self.root, bg='#2E2E2E')
        self.button_frame.pack(fill=tk.X, padx=10, pady=5)

        self.start_button = ttk.Button(self.button_frame, text="Clear all", command=lambda: self.update_terminal_log("Clear all"))
        self.start_button.grid(row=0, column=0, padx=5)

        self.root.mainloop()

    # Function to update the terminal log
    def update_terminal_log(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, f"{text}\n")
        self.output_text.config(state=tk.DISABLED)
        self.output_text.see(tk.END)

    # Input Field for Commands or Parameters

    def process_command(self,event=None):
        command = self.command_entry.get()
        self.update_terminal_log(f">> {command}")  # Display the entered command
        self.command_entry.delete(0, tk.END)  # Clear the input field
        # Process the command here

    # Bind Enter key to the input field


