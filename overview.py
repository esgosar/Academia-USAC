# Your main file

import tkinter as tk
from main_view import MainView  # Import the MainView class

# Configuration of the main window
ventana = tk.Tk()  # Creates a new window using Tkinter
ventana.title("Academia USAC")  # Sets the window title
ventana.attributes('-fullscreen', True)  # Configures the window to open in fullscreen

# Building the main view:
main_view = MainView(ventana)  # Calls the constructor of the MainView class, passing the ventana object

# Running the application:
ventana.mainloop()  # Starts the main loop of the Tkinter application
