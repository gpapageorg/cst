import customtkinter as ctk
import tkinter as tk
from tkinter import font
import interaction as i
# import commander as c
import ctypes

class Graphics():
    # Main Application Window
    def __init__(self):
        self.com = 0
        # Initialize the main window
        self.root = ctk.CTk()
        self.root.title("CsLab")
        self.root.geometry("1200x600")
        ctk.set_appearance_mode("dark")  # Set dark mode
        ctk.set_default_color_theme("dark-blue")  # Optional color theme

        # Terminal Output (Log Area)
        self.output_frame = ctk.CTkFrame(self.root)
        self.output_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Use tk.Text for colored text support
        self.output_text = tk.Text(self.output_frame, height=20, width=60, bg='black', fg='#F8F8F2', insertbackground='#F8F8F2',
                                   font=("Courier", 12), wrap='word', state=tk.DISABLED)
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # Create tags for different colors and bold text
        self.output_text.tag_configure("red", foreground="red")
        self.output_text.tag_configure("green", foreground="#019e77")
        self.output_text.tag_configure("blue", foreground="blue")
        self.output_text.tag_configure("yellow", foreground="yellow")
        self.output_text.tag_configure("white", foreground="white")  # Default color

        # Bold versions of the text colors
        bold_font = font.Font(self.output_text, self.output_text.cget("font"))
        bold_font.configure(weight="bold")

        self.output_text.tag_configure("bold_red", foreground="red", font=bold_font)
        self.output_text.tag_configure("bold_green", foreground="green", font=bold_font)
        self.output_text.tag_configure("bold_blue", foreground="#3a80a4", font=bold_font)
        self.output_text.tag_configure("bold_yellow", foreground="yellow", font=bold_font)
        self.output_text.tag_configure("bold_white", foreground="white", font=bold_font)

        # Input Frame (for command entry)
        self.input_frame = ctk.CTkFrame(self.root)
        self.input_frame.pack(fill=ctk.X, padx=10, pady=10)

        self.command_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Enter command...", font=("Courier", 12))
        self.command_entry.pack(fill=ctk.X, pady=5)
        self.command_entry.bind("<Return>", self.process_command)  # Bind Enter key

        # Control Buttons (Minimalist)
        self.button_frame = ctk.CTkFrame(self.root)
        self.button_frame.pack(fill=ctk.X, padx=10, pady=5)

        self.clear_button = ctk.CTkButton(self.button_frame, text="Clear all", command=self.clear_terminal_log)
        self.clear_button.grid(row=0, column=0, padx=5)
        


    # Function to update the terminal log with color and bold support
    def update_terminal_log(self, text, color="white", bold=False):
        self.output_text.config(state=tk.NORMAL)
        tag = color if not bold else f"bold_{color}"  # Use bold tag if bold=True
        # Insert the text with the color and/or bold tag
        self.output_text.insert(tk.END, f"{text}", tag)
        self.output_text.config(state=tk.DISABLED)
        self.output_text.see(tk.END)

    # Function to clear the terminal log
    def clear_terminal_log(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)

    # Function to process command input
    def process_command(self, event=None):
        command = self.command_entry.get()
        print(command)
        if command == "error":
            self.update_terminal_log(f">> {command} - Something went wrong\n", "red", bold=True)  # Display in bold red
        elif command == "success":
            self.update_terminal_log(f">> {command} - Operation successful\n", "green", bold=True)  # Display in bold green
        else:
            self.update_terminal_log(f">> {command}\n", "yellow")  # Display in yellow (not bold)
        
        self.command_entry.delete(0, ctk.END)  # Clear the input field
        self.com.getCommand(command)

# Run the application
def main():
    app = Graphics()
    com = c.Commander(app)
    app.com = com

    i.Interaction(app)


    app.root.mainloop()
if __name__ == "__main__":
    # libX11 = ctypes.cdll.LoadLibrary("libX11.so")
    # libX11.XInitThreads()

    main()