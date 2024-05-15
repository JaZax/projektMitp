# gui.py

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from card import Card
from templates import templates
from PIL import Image, ImageDraw, ImageFont
import textwrap

class CardGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Generator App")

        self.selected_template = tk.StringVar()
        self.card_name = tk.StringVar()
        self.card_description = tk.StringVar()
        self.front_text = tk.StringVar()
        self.back_image_path = tk.StringVar()
        self.back_text = tk.StringVar()

        self.create_widgets()

    def create_widgets():
        frame = ttk.Frame(self.root, padding="20")
        frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Template selection
        ttk.Label(frame, text="Select Template:").grid(column=0, row=0, sticky=tk.W)
        template_combo = ttk.Combobox(frame, textvariable=self.selected_template, values=list(templates.keys()))
        template_combo.grid(column=1, row=0, sticky=tk.W)

        # Card details input
        ttk.Label(frame, text="Card Name:").grid(column=0, row=1, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.card_name).grid(column=1, row=1, sticky=tk.W)

        ttk.Label(frame, text="Description:").grid(column=0, row=2, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.card_description).grid(column=1, row=2, sticky=tk.W)

        ttk.Label(frame, text="Front Text:").grid(column=0, row=3, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.front_text).grid(column=1, row=3, sticky=tk.W)

        # Back side customization
        ttk.Label(frame, text="Back Image:").grid(column=0, row=4, sticky=tk.W)
        ttk.Button(frame, text="Select Image", command=self.choose_image).grid(column=1, row=4, sticky=tk.W)

        ttk.Label(frame, text="Back Text:").grid(column=0, row=5, sticky=tk.W)
        ttk.Entry(frame, textvariable=self.back_text).grid(column=1, row=5, sticky=tk.W)

        ttk.Button(frame, text="Generate Card", command=self.generate_card).grid(column=0, row=6, columnspan=2, sticky=tk.W+tk.E)

    def choose_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.back_image_path.set(file_path)

    def generate_card(self):
        selected_template_name = self.selected_template.get()
        selected_template = templates[selected_template_name]

        # Create a Card instance with entered data
        card = Card(
            name=self.card_name.get(),
            description=self.card_description.get(),
            front_text=self.front_text.get(),
            template=selected_template
        )

        # Customize the back side of the card (if applicable)
        card.back_image_path = self.back_image_path.get()
        card.back_text = self.back_text.get()

        # Save the card image using Pillow
        save_card_image(card)

        # Reset fields after generating the card
        self.card_name.set("")
        self.card_description.set("")
        self.front_text.set("")
        self.back_image_path.set("")
        self.back_text.set("")

def save_card_image(card):
    # Load the user-supplied background image
    background_image = Image.open(card.back_image_path)

    # Create a drawing context
    draw = ImageDraw.Draw(background_image)
    font = ImageFont.load_default()  # Use default font

    wrapper = textwrap.TextWrapper(width=50) 
    word_list = wrapper.wrap(text=card.description) 
    caption_new = ''
    for ii in word_list[:-1]:
        caption_new = caption_new + ii + '\n'
    caption_new += word_list[-1]

    # Define text and position for each detail on the card
    details = [
        (f"Name: {card.name}", (50, 50)),
        (f"Description: {caption_new}", (50, 100)),
        (f"Front Text: {card.front_text}", (50, 150)),
        (f"Back Text: {card.back_text}", (50, 200))
    ]

    # Draw each detail on the background image
    for text, position in details:
        draw.text(position, text, fill=(0, 0, 0), font=font)

    # Save the composite image with overlaid text
    save_path = f"{card.name.replace(' ', '_')}_card.png"  # Generate filename based on card name
    background_image.save(save_path)

    # Provide feedback to the user (optional)
    print(f"Card '{card.name}' saved successfully as '{save_path}'")