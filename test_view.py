import tkinter as tk
from image_display import ImageViewerCanvas

# Create the main window
root = tk.Tk()
root.title("Academia usac")

# Define the header frame with a modified height
header = tk.Frame(root, bg="white", height=60)  # Adjusted height to 60 pixels
header.pack(fill=tk.X, side=tk.TOP)

# Header text
header_text = tk.Label(header, text="Asignar Cursos", bg="white", fg="black", font=("Helvetica", 16))
header_text.pack(side=tk.LEFT, padx=10)

# Define the profile section frame
profile_section = tk.Frame(header, bg="white")
profile_section.pack(side=tk.RIGHT, padx=10, pady=10)

# Username label, packed to the left within the profile section
username = tk.Label(profile_section, text="Username", bg="white", fg="black", font=("Helvetica", 16))
username.pack(side=tk.LEFT)

image_viewer_canvas = ImageViewerCanvas(master=profile_section, json_file_path='users.json', username='user', width=40, height=40)
image_viewer_canvas.pack(side=tk.RIGHT, padx=10)

# Start the GUI event loop
root.mainloop()
