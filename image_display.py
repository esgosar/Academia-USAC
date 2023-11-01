import base64
import json
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk

class ImageViewerCanvas(tk.Canvas):
    def __init__(self, master=None, json_file_path=None, username=None, width=40, height=40, **kwargs):
        super().__init__(master, width=width, height=height, bg='white', **kwargs)
        self.config(highlightthickness=0)
        self.image_data = None
        self.width = width
        self.height = height
        self.json_file_path = json_file_path
        self.username = username
        self.load_and_display_avatar_from_json()

    def load_and_display_avatar_from_json(self):
        if self.json_file_path and self.username:
            with open(self.json_file_path, 'r') as file:
                data = json.load(file)
                user_data = data.get(self.username)
                if user_data and user_data.get('avatar'):
                    self.display_avatar(user_data.get('avatar'))

    def display_avatar(self, image_base64):
        if image_base64:
            image_bytes = base64.b64decode(image_base64)
            image = Image.open(BytesIO(image_bytes))
            resized_image = image.resize((self.width, self.height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(resized_image)
            self.create_image(20, 20, image=photo)  # Adjust coordinates to center image
            self.photo = photo  # Keep a reference so it's not garbage collected
        else:
            self.create_text(100, 100, text="No Image", font=("Helvetica", 10))

# Usage example
# Assuming you have a JSON file named 'users.json' with the structure provided
# image_viewer_canvas = ImageViewerCanvas(master=root, json_file_path='users.json', username='username')
# image_viewer_canvas.pack()
