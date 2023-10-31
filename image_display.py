import base64
import json
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk

class ImageViewerCanvas(tk.Canvas):
    def __init__(self, master=None, username=None, image_size=(24, 24), **kwargs):
        super().__init__(master, width=image_size[0], height=image_size[1], **kwargs)
        self.config(highlightthickness=0)  # Set background color to white, remove border
        self.image_size = image_size  # Store the image size
        self.image_data = None
        self.json_file_path = 'users.json'  # The JSON file name is hardcoded
        self.username = username
        self.load_and_display_avatar_from_json()

    def load_and_display_avatar_from_json(self):
        if self.username:
            with open(self.json_file_path, 'r') as file:
                data = json.load(file)
                user_data = data.get(self.username)
                if user_data and user_data.get('avatar'):
                    self.display_avatar(user_data.get('avatar'))

    def display_avatar(self, image_base64):
        if image_base64:
            image_bytes = base64.b64decode(image_base64)
            image = Image.open(BytesIO(image_bytes))
            image = image.resize(self.image_size, Image.LANCZOS)  # Resize the image using the provided size
            photo = ImageTk.PhotoImage(image)
            # Center the image on the canvas
            self.create_image(self.image_size[0] // 2, self.image_size[1] // 2, image=photo, anchor=tk.CENTER)
            self.photo = photo  # Keep a reference to prevent garbage collection
        else:
            # If no image is provided, display placeholder text
            self.create_text(self.image_size[0] // 2, self.image_size[1] // 2, text="No Image", font=("Helvetica", 10))
