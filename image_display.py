import base64
import json
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk

class ImageViewerCanvas(tk.Canvas):
    def __init__(self, master=None, username=None, width=40, height=40, **kwargs):
        super().__init__(master, width=width, height=height, bg='white', **kwargs)
        self.config(highlightthickness=0)
        self.image_data = None
        self.username = username
        self.width = width
        self.height = height
        self.load_and_display_avatar_from_json()

    def load_and_display_avatar_from_json(self):
        json_file_path = 'users.json'  # Directly specify the file name
        if self.username:
            with open(json_file_path, 'r') as file:
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
            self.create_image(self.width//2, self.height//2, image=photo)
            self.photo = photo  # Keep a reference so it's not garbage collected
        else:
            self.create_text(100, 100, text="No Image", font=("Helvetica", 10))

# Usage example
# image_viewer_canvas = ImageViewerCanvas(master=root, username='username', width=100, height=100)
# image_viewer_canvas.pack()
