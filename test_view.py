import tkinter as tk
from image_display import ImageViewerCanvas

# Create the main window
root = tk.Tk()
root.title("Academia usac")

# Define the header frame with a modified height
header = tk.Frame(root, bg="white", height=60)  # Adjusted height to 60 pixels
header.pack(fill=tk.X, side=tk.TOP)

# Header text
header_text = tk.Label(header, text="Academia usac", bg="black", fg="white", font=("Helvetica", 16))
header_text.pack(side=tk.LEFT)

# Define the profile section frame
profile_section = tk.Frame(header, bg="blue")
profile_section.pack(side=tk.RIGHT, padx=10)

# Username label, packed to the left within the profile section
username = tk.Label(profile_section, text="Username", bg="blue", fg="white", font=("Helvetica", 12))
username.pack(side=tk.LEFT)

# Profile image, packed to the right within the profile section
image_viewer_canvas = ImageViewerCanvas(master=profile_section, username='username', image_size=(24, 24))
image_viewer_canvas.pack(side=tk.RIGHT, padx=5)

# Start the GUI event loop
root.mainloop()
